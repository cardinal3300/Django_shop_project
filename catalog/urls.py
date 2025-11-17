from django.urls import path

from .views import (AddProductView, ContactsView, HomeView,
                           ProductDeleteView, ProductDetailView,
                           ProductUpdateView, can_unpublish_product, CategoryProductsView)

app_name = "catalog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("add/", AddProductView.as_view(), name="product_form"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_form"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_confirm_delete"),
    path("unpublished/<int:pk>/", can_unpublish_product, name="can_unpublish_product"),
    path("category/<int:category_id>/", CategoryProductsView.as_view(), name="category_products")
]
