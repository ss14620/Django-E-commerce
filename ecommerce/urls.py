"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url,include
from ecommerce.views import contact_page,home_page
from . import settings
from accounts.views import register_page,login_page,user_logout,login,guest_register_view
from django.conf.urls.static import static
from products import views
from addresses.views import checkout_address_create_view,checkout_address_reuse_view
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',home_page,name ='home'),
    url(r'^contact/',contact_page,name ='contact'),
    url(r'^login/',login_page,name ='login'),
    url(r'^register/guest/$',guest_register_view,name ='guest_register'),
    url(r'^checkout/address/create/$',checkout_address_create_view,name='checkout_address_create'),
    url(r'^checkout/address/resue/$',checkout_address_reuse_view,name='checkout_address_reuse'),
    url(r'^logout/',user_logout,name ='logout'),
    url(r'^register/',register_page,name ='register'),
    url(r'^cart/',include("carts.urls",namespace ='cart')),
    url(r'^products/',include("products.urls",namespace ='products')),
    url(r'^search/',include("search.urls",namespace ='search')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
