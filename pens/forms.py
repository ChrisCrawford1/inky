from django import forms

from brands.models import Brand
from pens.enum import NibMaterial, NibSize


class PenForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control col-md-4 m-auto mb-md-3"}),
    )

    description = forms.CharField(
        label="Description",
        required=False,
        max_length=255,
        widget=forms.Textarea(attrs={"class": "form-control col-md-4 m-auto mb-md-3"}),
    )

    brand = forms.ChoiceField(
        choices=tuple(
            (brand.id, brand.name) for brand in Brand.objects.order_by("name")
        ),
        widget=forms.Select(attrs={"class": "form-control col-md-4 m-auto mb-md-3"}),
    )

    nib_size = forms.ChoiceField(
        choices=NibSize.to_tuple(),
        widget=forms.Select(attrs={"class": "form-control col-md-4 m-auto mb-md-3"}),
    )

    nib_material = forms.ChoiceField(
        choices=NibMaterial.to_tuple(),
        widget=forms.Select(attrs={"class": "form-control col-md-4 m-auto mb-md-3"}),
    )

    colour = forms.CharField(
        label="Colour",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control col-md-4 m-auto mb-md-3"}),
    )

    purchase_price = forms.FloatField(
        label="Purchased at price",
        min_value=0.0,
        widget=forms.TextInput(attrs={"class": "form-control col-md-4 m-auto mb-md-3"}),
    )

    purchase_currency = forms.CharField(
        label="Purchased Currency",
        max_length=3,
        widget=forms.TextInput(attrs={"class": "form-control col-md-4 m-auto mb-md-3"}),
    )

    purchased_date = forms.DateField(
        label="Purchased Date",
        widget=forms.DateInput(
            attrs={"type": "date", "class": "form-control col-md-4 m-auto mb-md-3"}
        ),
    )

    retailer = forms.CharField(
        label="Retailer",
        max_length=255,
        widget=forms.TextInput(attrs={"class": "form-control col-md-4 m-auto mb-md-3"}),
    )

    image = forms.ImageField(
        label="Image", required=False, widget=forms.FileInput(attrs={"class": ""})
    )
