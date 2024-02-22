from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, ListView
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
from .models import Product


class HomeView(TemplateView):
    template_name = 'pages/home.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page ...",
            "author": "Developed by: Santiago Gallego",
        })

        return context


class ContactView(TemplateView):
    template_name = 'pages/contact.html'


class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.objects.all()

        return render(request, self.template_name, viewData)


class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        # check if product id is a valid integer
        try:
            product_id = int(id)
            if product_id < 1:
                raise ValueError("Product id must be 1 or greater")
            product = get_object_or_404(Product, pk=product_id)
        except (ValueError, IndexError):
            # if product id is not a valid, redirect to home
            return HttpResponseRedirect(reverse('pages:home'))

        # context
        viewData = {
            "pk": product_id,
            "title": f"{product.name} - Online Store",
            "subtitle": f"{product.name} - Product information",
            "product": product
        }

        return render(request, self.template_name, viewData)


class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero")
        return price


class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():

            return render(request, 'products/product_created.html')

        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)


class ProductListView(ListView):
    template_name = 'products/index.html'
    model = Product
    # this allows to use the product's object  in the template
    context_object_name = 'products'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Products - Online Store",
            "subtitle": "List of products",
        })

        return context
