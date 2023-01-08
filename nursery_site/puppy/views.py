from django.http import request
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView

from puppy.forms import BroodCreateForm, PuppyCreateForm
from puppy.models import PuppyBrood, Puppy


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


class BroodCreateView(CreateView):
    model = PuppyBrood
    form_class = BroodCreateForm
    success_url = reverse_lazy("puppies:index")


class PuppyCreateView(CreateView):
    model = Puppy
    form_class = PuppyCreateForm
    success_url = reverse_lazy("puppies:add-puppy")

    def get_success_url(self):
        return reverse("puppies:add-puppy", kwargs={"brood_pk": self.object.brood.pk})
