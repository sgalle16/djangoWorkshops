from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from .views import HomeView, AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Products app urls
    path('products/', include('products.urls', namespace='products')),
    # Pages urls
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)