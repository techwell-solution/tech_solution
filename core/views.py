from django.shortcuts import render
from .models import Platform, Service
from .forms import ContactForm

# Create your views here.
def home(request):

    platforms = Platform.objects.filter(
        is_active=True
    )

    services = Service.objects.filter(
        featured=True,
        is_active=True
    ).order_by("order")

    return render(request, "core/home.html",  
                  {"platforms": platforms,
                   "services": services,
                   })

def services(request):

    services = Service.objects.filter(
        is_active=True
    )

    platforms = Platform.objects.filter(
        is_active=True
    )
    return render( request, "core/services.html", {
            "services": services,
            "platforms": platforms, 
        },)

def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            return render(
                request,
                "contact_success.html",
            )

    else:

        form = ContactForm()

    return render(request, "core/contact.html", {"form": form,},)