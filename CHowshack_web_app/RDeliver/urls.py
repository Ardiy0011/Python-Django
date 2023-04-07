"""RDeliver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings 
from django.conf.urls.static import static
from customer.views import Indexpage, Orderpage1,Orderpage2, Storespage, Contactpage, Menupage,Orderconfirmationpage, Paymentconfirmationpage, breakfastpage, drinkpage, lunchpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  Indexpage.as_view(), name='index'),
    path('order1/', Orderpage1.as_view(), name='order1'),
    path('order2/', Orderpage2.as_view(), name='order2'),
    path('break/', breakfastpage.as_view(), name='break'),
    path('drink/', drinkpage.as_view(), name='drink'),
    path('lunch/', lunchpage.as_view(), name='lunch'),
    path('stores/', Storespage.as_view(), name='stores'),
    path('contact/', Contactpage.as_view(), name='contact'),
    path('menu/', Menupage.as_view(), name='menu'),
    path('orderconfirmation/<int:pk>', Orderconfirmationpage.as_view(), name='orderconfirmation'),
    path('payment/', Paymentconfirmationpage.as_view(), name='payment'),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
