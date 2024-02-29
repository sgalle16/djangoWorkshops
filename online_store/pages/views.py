from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, ListView
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import ProductForm
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
        viewData = {
            "title": "Products - Online Store",
            "subtitle": "List of products",
            "products": Product.objects.all()
        }

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


class ProductCreateView(View):
    template_name = 'products/create.html'
    model = Product
    form_class = ProductForm

    def get(self, request):
        form = self.form_class()
        viewData = {
            "title": "Create product",
            "form": form
        }
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'products/product_created.html')

        else:
            viewData = {
                "title": "Create product",
                "form": form
            }
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


# Cart System

class CartView(View):
    template_name = 'cart/index.html'

    def get(self, request):
        # Simulated database for products
        products = {}
        products[121] = {'name': 'Tv samsung', 'price': '1000'}
        products[11] = {'name': 'Iphone', 'price': '2000'}

        # Get cart products from session
        cart_products = {}
        cart_product_data = request.session.get('cart_product_data', {})

        for key, product in products.items():
            if str(key) in cart_product_data.keys():
                cart_products[key] = product

        # Prepare data for the view
        view_data = {
            'title': 'Cart - Online Store',
            'subtitle': 'Shopping Cart',
            'products': products,
            'cart_products': cart_products
        }

        return render(request, self.template_name, view_data)

    def post(self, request, product_id):
        # Get cart products from session and add the new product
        cart_product_data = request.session.get('cart_product_data', {})
        cart_product_data[product_id] = product_id
        request.session['cart_product_data'] = cart_product_data

        return redirect('pages:cart_index')


class CartRemoveAllView(View):
    def post(self, request):
        # Remove all products from cart in session
        if 'cart_product_data' in request.session:
            del request.session['cart_product_data']

        return redirect('pages:cart_index')


# Image Storage

def ImageViewFactory(image_storage):
    class ImageView(View):
        template_name = 'images/index.html'

        def get(self, request):
            image_url = request.session.get('image_url', '')
            return render(request, self.template_name, {'image_url': image_url})

        def post(self, request):
            image_url = image_storage.store(request)
            request.session['image_url'] = image_url
            return redirect('pages:image_index')

    return ImageView
