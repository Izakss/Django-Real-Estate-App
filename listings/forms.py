from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title",
            "price",
            "num_bathrooms",
            "num_bedrooms",
            "square_footage",
            "address",
        ]