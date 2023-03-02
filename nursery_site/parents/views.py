from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from .forms import ParentCreateForm
from .models import Parent, ParentBreed


class ParentsListView(ListView):
    template_name = "parents/index.html"
    context_object_name = "parents"
    model = Parent
    queryset = (
        Parent.objects.select_related("breed", "color")
        .order_by("pk")
        .filter(archived=False)
        .all()
    )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["help_text"] = "For your help!"
        return context


class ParentsBreedList(ListView):
    model = ParentBreed


class ParentsByBreedList(ListView):
    queryset = Parent.objects.select_related("breed")

    def get_queryset(self):
        qs = super().get_queryset()
        breed_name = self.kwargs["parent_breed"]
        breed: ParentBreed = get_object_or_404(ParentBreed, name=breed_name)
        return qs.filter(breed=breed)

    def get_context_data(self, **kwargs):
        context = super(ParentsByBreedList, self).get_context_data(**kwargs)
        if context["object_list"]:
            context["p_breed"] = context["object_list"][0].breed
        else:
            context["p_breed"] = None
        return context


class ParentDetailView(DetailView):
    template_name = "parents/details.html"
    context_object_name = "parent"
    model = Parent


class ParentCreateView(PermissionRequiredMixin, CreateView):
    model = Parent
    permission_required = "puppies.create_brood"
    form_class = ParentCreateForm
    success_url = reverse_lazy("parents:index")


class ParentDeleteView(PermissionRequiredMixin, DeleteView):
    model = Parent
    permission_required = "parents.delete_parent"
    success_url = reverse_lazy("parents:index")
    context_object_name = "parent"

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)
