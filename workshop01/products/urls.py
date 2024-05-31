from django.urls import path
from .views import (
    ProductCreateView,
    ProductListView,
    ProductDetailView,
    ProductDeleteView)

app_name = "products"

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create'),
    path('list/', ProductListView.as_view(), name='list'),
    path('show/<str:pk>/', ProductDetailView.as_view(), name='show'),
    path('delete/<str:pk>/', ProductDeleteView.as_view(), name='delete'),
]
