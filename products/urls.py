from django.urls import path, include
from. import views as my_views

urlpatterns = [
    path('', my_views.products, name='products-url'),
    path('add-products/', my_views.products, name='add-products-url'),
    path('update-products/', my_views.products, name='update-products-url'),

]