from django.urls import path
from .views import (
    HomeView, 
    AboutView, 
    ContactView, 
    ProductIndexView,
    ProductShowView,
    ProductCreateView
    )

app_name = "pages"

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("about/", AboutView.as_view(), name='about'),
    path("contact/", ContactView.as_view(), name='contact'),

    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    


]
