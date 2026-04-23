from django.urls import path

from . import views

urlpatterns = [
    path("", views.listings_page, name="listings_page"),
    path("create/", views.create_listing_form, name="create_listing_form"),
    path(
        "api/create/",
        views.create_listing_with_make_model,
        name="create_listing_with_make_model",
    ),
]
