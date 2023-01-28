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
    success_url = reverse_lazy("puppies:index")
    # brood = get_object_or_404(PuppyBrood, pk=brood_pk)

    # def get(self, request, *args, **kwargs):
    #     self.brood_pk = kwargs['brood_pk']
    #     # print(self.brood_pk)
    #     return super().get(request, *args, **kwargs)
    #
    # def form_valid(self, form):
    #     current_brood = PuppyBrood.object.get(pk=self.brood_pk)  # Этот pk мы сохранили в методе get
    #     print(current_brood, "!!!!!!!!")
    #     form.instance.brood = 1
    #     return super().form_valid(form)
    #
    # def get_success_url(self):
    #     print("BROOD PK:    ", self.object.brood.pk)
    #     print("OBJECT:      ", self.object)
    #     return reverse("puppies:add-puppy", kwargs={"brood_pk": self.object.brood.pk})
