"""nextgen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include, path
from django.conf import settings
from django.conf.urls.static import static

from user_registration.views import Homepage

from blog.views import blog, blogdetails, blogcategories
from store.views import home, about, contact, services, shop, details, subcategory, form, add_to_cart,update_cart,remove_from_cart,cart

#from blog.views import blog, blogdetails, blogcategories


urlpatterns = [
     re_path(r'^admin/', admin.site.urls),
     re_path(r'^$', home, name='home'),
     re_path(r'^index', home, name='home'),
     re_path(r'^quotationreq', form, name='form'),
     path('subcategory/<id>', subcategory, name='subcategory'),
     re_path(r'^about', about, name='about'),
     re_path(r'^contact', contact, name='contact'),
     re_path(r'^services', services, name='services'),  
     re_path(r'^shop', shop, name='shop'),     
  
     re_path(r'^blog/', blog, name='blog'),
     path('blogdetails/<id>', blogdetails, name='blogdetails'),
     path('blogcategories/<id>', blogcategories, name='blogcategories'),
     path('product/details/<id>', details, name='details' ),
     path('', Homepage.as_view(), name="homeview"),
     path('accounts/', include('user_registration.urls')),    
     path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
     path('update-cart/<int:cart_item_id>/', update_cart, name='update_cart'),
     path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
     path('cart/', cart, name='cart'),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)