from django.urls import path
from .views import view_cart, add_cart, remove_cart, add_quantity, minus_quantity

urlpatterns = [
    path('', view_cart, name='view_cart'),
    path('add/<products_id>', add_cart, name='add_cart'),
    path('add_quantity/<products_id>', add_quantity, name='add_quantity'),
    path('minus_quantity/<products_id>', minus_quantity, name='minus_quantity'),
    path('remove/<products_id>', remove_cart, name='remove_cart')
]
