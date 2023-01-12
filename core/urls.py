from django.urls import path
from core import views

urlpatterns = [
    path("", views.main, name='main'),
    path("producto/<int:pk>/", views.product, name="product"),
    path("agregar_producto/", views.create_product, name="product-form"),
]