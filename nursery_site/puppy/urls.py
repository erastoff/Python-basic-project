from django.urls import path

from .views import (
    BroodListView,
    BroodDetailView,
    # ParentCreateView,
)

app_name = "puppies"

urlpatterns = [
    path("", BroodListView.as_view(), name="index"),
    path("<int:pk>/", BroodDetailView.as_view(), name="details"),
    # path("create/", ParentCreateView.as_view(), name="create-parent"),
]
