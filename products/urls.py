from django.urls import path
from .views import show_products, create_products, update_products, delete_products, confirm_delete_products

urlpatterns = [
    path('', show_products, name='show_products'),
    path('create/', create_products, name='create_products'),
    path('update/<products_id>/', update_products, name='update_products'),
    path('delete/<products_id>/', delete_products, name='delete_products'),
    path('confirm_delete/<products_id>/', confirm_delete_products, name='confirm_delete_products'),
    path('<category>/', show_products, name='show_products'),
]
