from django.shortcuts import render
from.models import Listing

# Create your views here.

#CRUD-- Create, retrieve(specific), Update, Delete and list(all multiple records)

def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings":listings
    }
    return render(request, "listings.html", context)
