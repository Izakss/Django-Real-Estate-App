from django.shortcuts import render
from.models import Listing
from.forms import ListingForm

# Create your views here.

#CRUD-- Create, retrieve(specific), Update, Delete and list(all multiple records)

def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings":listings
    }
    return render(request, "listings.html", context)

def listing_retrieve(request, pk):

    listing = Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, "listing.html", context)

def listing_create(requests):
    form = ListingForm()
    context = {
        "form": form
    }
    return render(requests,"listing_create.html",context)