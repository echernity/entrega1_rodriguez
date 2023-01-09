from django.urls import path
from core import views

urlpatterns = [
    path("", views.main, name='main'),
    path("producto/<str:pk>/", views.product, name="product"),
    path("agregar_producto/", views.add_product, name="product-form")
]