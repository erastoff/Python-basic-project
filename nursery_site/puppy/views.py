from django.shortcuts import render
from django.views.generic import ListView, DetailView

from puppy.models import PuppyBrood


class BroodListView(ListView):
    template_name = "puppy/index.html"
    context_object_name = "broods"
    model = PuppyBrood


class BroodDetailView(DetailView):
    template_name = "puppy/details.html"
    context_object_name = "brood"
    # model = Parent
    queryset = PuppyBrood.objects.select_related("sire", "bitch")
    # .prefetch_related('food')
