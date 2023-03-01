from django.urls import path

from .views import (
    ParentsListView,
    ParentDetailView,
    ParentCreateView,
    ParentsByBreedList,
    AnimalKindListView,
    ParentDeleteView,
)

app_name = "parents"

urlpatterns = [
    path("", ParentsListView.as_view(), name="index"),
    path("<int:pk>/", ParentDetailView.as_view(), name="details"),
    path("create/", ParentCreateView.as_view(), name="create-parent"),
    path("breeds/", AnimalKindListView.as_view(), name="breeds"),
    path("<parent_breed>/", ParentsByBreedList.as_view(), name="breed_parents"),
    path("<int:pk>/confirm-delete/", ParentDeleteView.as_view(), name="delete"),
]
