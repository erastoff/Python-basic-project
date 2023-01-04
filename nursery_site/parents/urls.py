from django.urls import path

from .views import (
    ParentsListView,
    ParentDetailView,
    ParentCreateView,
)

app_name = "parents"

urlpatterns = [
    path("", ParentsListView.as_view(), name="index"),
    path("<int:pk>/", ParentDetailView.as_view(), name="details"),
    path("create/", ParentCreateView.as_view(), name="create-parent"),
]
