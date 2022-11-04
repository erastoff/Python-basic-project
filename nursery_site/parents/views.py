from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Parent


class ParentsListView(ListView):
    template_name = "parents/index.html"
    context_object_name = "parents"
    model = Parent


class ParentDetailView(DetailView):
    template_name = "parents/details.html"
    context_object_name = "parent"
    # model = Parent
    queryset = (
        Parent.objects.select_related("breed", "color")
        # .prefetch_related('food')
    )
