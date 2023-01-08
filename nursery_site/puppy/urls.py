from django.urls import path

from .views import (
    BroodListView,
    BroodDetailView, BroodCreateView, PuppyCreateView,
    # ParentCreateView,
)

app_name = "puppies"

urlpatterns = [
    path("", BroodListView.as_view(), name="index"),
    path("create_brood/", BroodCreateView.as_view(), name="create-brood"),
    path("<int:pk>/", BroodDetailView.as_view(), name="details"),
    path("<int:brood_pk>/add_puppy/", PuppyCreateView.as_view(), name="add-puppy"),
]