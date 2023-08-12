from django.db import models, transaction
from django.contrib.auth.models import User

class Resource(models.Model):
    """
    Model for a bookable resource.
    """
    TYPE_CHOICES = [
        ('room', 'Room'),
        ('equipment', 'Equipment'),
        # Add more choices if necessary
    ]

    name = models.CharField(max_length=255, verbose_name="Name")
    description = models.TextField(verbose_name="Description")
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='room', verbose_name="Type")
    availability = models.TextField(blank=True, null=True, verbose_name="Availability")
    duration = models.IntegerField(verbose_name="Duration")
    price = models.IntegerField(verbose_name="Price")
    currency = models.CharField(max_length=50, default='SEK', verbose_name="Currency")

    def __str__(self):
        return self.name


class Booking(models.Model):
    """
    Model to handle bookings.
    """
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('conducted', 'Conducted'),
        ('cancelled', 'Cancelled'),
        # Add more choices if necessary
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, verbose_name="Resource")
    start_time = models.DateTimeField(verbose_name="Start Time")
    end_time = models.DateTimeField(verbose_name="End Time")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='scheduled', verbose_name="Status")
    comments = models.TextField(blank=True, null=True, verbose_name="Comments")

    def __str__(self):
        return f"{self.user} - {self.resource} - {self.start_time} to {self.end_time}"


from django.db import models
from django.conf import settings
from .models import Booking


class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='payment')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User")
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming a max amount of 99999999.99
    transaction_id = models.CharField(max_length=255, null=True, blank=True)  # ID from Stripe
    status = models.CharField(max_length=50, choices=PAYMENT_STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    stripe_charge_id = models.CharField(max_length=50, blank=True, null=True)  # To keep reference of Stripe's charge ID

    def charge(self, token):
        import stripe
        stripe.api_key = 'YOUR_STRIPE_SECRET_KEY'

        try:
            charge = stripe.Charge.create(
                amount=int(self.amount * 100),  # Stripe deals in cents
                currency="SEK",  # Adjust according to your currency
                source=token,
                description=f"Charge for {self.user.email}",
            )

            if charge["paid"] == True:
                self.status = 'completed'
                self.stripe_charge_id = charge["id"]
                self.save()
                return True
            else:
                self.status = 'failed'
                self.save()
                return False

        except stripe.error.CardError as e:
            self.status = 'failed'
            self.save()
            return False
    def refund(self, amount=None):
        import stripe
        stripe.api_key = 'YOUR_STRIPE_SECRET_KEY'

        if self.status != 'completed':
            raise ValueError("Only completed payments can be refunded.")
        
        if not self.stripe_charge_id:
            raise ValueError("Missing Stripe charge ID.")
        
        if not amount:
            amount = self.amount
        
        try:
            refund = stripe.Refund.create(
                charge=self.stripe_charge_id,
                amount=int(amount * 100)  # Stripe deals in cents
            )

            if refund["status"] == "succeeded":
                self.status = 'refunded'
                self.save()
                return True

            else:
                return False

        except stripe.error.StripeError as e:
            # Handle other Stripe errors (e.g., API connection errors, API errors)
            return False

    def fetch_from_stripe(self):
        """
        Fetch payment details from Stripe.
        """
        import stripe
        stripe.api_key = 'YOUR_STRIPE_SECRET_KEY'

        if not self.stripe_charge_id:
            raise ValueError("Missing Stripe charge ID.")
        
        return stripe.Charge.retrieve(self.stripe_charge_id)

    @transaction.atomic
    def handle_webhook(self, payload):
        """
        Handle webhook events from Stripe.
        For now, let's assume the webhook is for payment disputes.
        This method can be extended to handle other types of webhook events.
        """
        event = payload["type"]
        if event == "charge.dispute.created":
            # Handle the payment dispute
            # Mark the payment status as disputed in your database, notify the user, etc.
            pass
        # You can add other event types as needed