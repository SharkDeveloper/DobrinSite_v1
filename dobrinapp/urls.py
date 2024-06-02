from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('gal/', views.gal, name='gal'),
    path('picture/', views.picture, name='picture'),
    path('nov/', views.nov, name='nov'),
    path('bio/', views.bio, name='bio'),
    path('vid/', views.vid, name='vid'),
    path('nov_page/', views.nov_page, name='nov_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)