from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms


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


class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV", "price": 2200},
        {"id": "2", "name": "iPhone", "description": "Best iPhone", "price": 2800},
        {"id": "3", "name": "Chromecast",
            "description": "Best Chromecast", "price": 70},
        {"id": "4", "name": "Glasses", "description": "Best Glasses", "price": 20}
    ]


class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)


class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        viewData = {}
        try:
            product = Product.products[int(id)-1]
            viewData["title"] = product["name"] + " - Online Store"
            viewData["subtitle"] = product["name"] + " - Product information"
            viewData["product"] = product

            return render(request, self.template_name, viewData)

        except IndexError:
            return HttpResponseRedirect(reverse('pages:home'))


class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)


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

            return HttpResponseRedirect(reverse('pages:index'))

        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)
