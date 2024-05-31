from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """A form for creating or updating a product"""

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category', 'images']

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_price(self):
        """Clean and validate the price field """
        price = self.cleaned_data.get('price')
        price = int(price)
        if price <= 0:
            raise forms.ValidationError('Price must be greater than 0')
        return price
