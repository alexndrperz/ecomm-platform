"""
URL configuration for API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import ProductView, SellerView, TransactsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductView.as_view({'get':'get_all_products', 'post':'post_product'})),
    path('products/<int:id>', ProductView.as_view({'get':'get_one_product', 'delete':'delete_product'})),
    path('products/<int:sell_id>/<int:prod_id>', ProductView.as_view({'get':'get_url_product'})),
    path('products/<str:sell_tokn>/<str:prod_tokn>', ProductView.as_view({'get':'get_url_based_product'})),
    
    path('sellers/', SellerView.as_view({'get':'get_sellers','post':'create_seller'})),

    path('seller/<str:tokn>', SellerView.as_view({'get':'get_seller_profile'})),

    path('transacts/', TransactsView.as_view({'get':'get_all_transacts','post':'create_transact'}))

]
