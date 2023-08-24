from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ResourceForm
from django.contrib import messages

@login_required
def add_resource(request):
    if not request.user.is_staff:
        messages.error(request, "Du har inte behörighet att se denna sida.")
        return redirect('some_other_view_name')  # Redirect to a page that says they don't have permission

    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Resursen har lagts till!")
            return redirect('name_of_this_view')  # Redirect to the same page to add another resource
    else:
        form = ResourceForm()

    return render(request, 'add_resource.html', {'form': form})

