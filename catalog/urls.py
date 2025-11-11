from django.urls import path

from catalog.views import (AddProductView, ContactsView, HomeView,
                           ProductDeleteView, ProductDetailView,
                           ProductUpdateView)

app_name = "catalog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("add/", AddProductView.as_view(), name="product_form"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_form"),
    path(
        "product/<int:pk>/delete/",
        ProductDeleteView.as_view(),
        name="product_confirm_delete",
    ),
]
