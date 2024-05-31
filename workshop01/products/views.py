from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib import messages # import messages framework from django. https://docs.djangoproject.com/en/4.2/ref/contrib/messages/
from django.contrib.messages.views import SuccessMessageMixin
from .models import Product
from .forms import ProductForm


# CreateView is responsible for rendering the form on a GET request,
# handling form validation on a POST request, saving the object, and
# redirecting the user to success_url
class ProductCreateView(SuccessMessageMixin, CreateView):
    """ View to create a new product based on the Product model"""

    model = Product
    form_class = ProductForm
    template_name = 'products/create_product.html'
    success_url = reverse_lazy('products:list')
    # The success message to display after a successful form submission.
    success_message = "Elemento '%(name)s' creado satisfactoriamente" # Esta es la Actividad 3 donde muestro el mensaje de exito con SuccessMessageMixin

    # if the form is valid -> Save the object 
    def form_valid(self, form):

        form.save()
        return super().form_valid(form)

    # If the form is invalid form, render the form is invalid
    def form_invalid(self, form):
        messages.error(self.request, "Error al crear el producto")
        response = super().form_invalid(form)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Create a new product",
            "subtitle": "Formulario Creación - Taller 01 - TEIS",
        })
        return context


# ListView is a view that displays a list of products(objects).
# It is responsible for rendering a list of objects on a GET request,
# and it can also handle filtering the list of objects on a POST request.
class ProductListView(ListView):
    """View to list all products based on the Product model."""

    model = Product
    template_name = 'products/list_products.html'
    context_object_name = 'products'
    # The queryset of all products to use for the view
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "List of products",
            "subtitle": "Lista de Objetos - Taller 01 - TEIS",
        })

        return context


# ProductDetailView is a view that displays the details of an product(object).
# It is responsible for rendering the details of an object on a GET request,
# and provides the necessary context data to the template for rendering.
class ProductDetailView(DetailView):
    """ View to show the details of a product based on the Product model"""
    model = Product
    context_object_name = 'product'
    template_name = 'products/show_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Show product",
            "subtitle": "Vista objeto - Taller 01 - TEIS",
        })
        return context



# ProductDeleteView is a view that deletes an product(object).
# It is responsible for rendering a confirmation form on a GET request,
# handling the deletion confirmation on a POST request, deleting the object,
# and then redirecting the user to success_url.
class ProductDeleteView(DeleteView):
    """ View to delete a product based on the Product model"""
    model = Product
    context_object_name = 'product'
    template_name = 'products/confirm_delete.html'
    success_url = reverse_lazy('products:list')


    def form_valid(self, form):
        product = self.get_object()
        messages.info(self.request, f"Producto '{product.name}' eliminado satisfactoriamente")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Delete product",
            "subtitle": "Borrar Producto - Taller 01 - TEIS",
        })
        return context
