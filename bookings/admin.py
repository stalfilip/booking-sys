from django.contrib import admin
from .models import Resource, Booking, Payment, Availability

admin.site.register(Resource)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Availability)

# Register your models here.
