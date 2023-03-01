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


class AnimalKindListView(ListView):
    model = ParentBreed


class ParentsByBreedList(ListView):
    queryset = Parent.objects.select_related("breed")

    def get_queryset(self):
        qs = super().get_queryset()
        breed_name = self.kwargs["parent_breed"]
        breed: ParentBreed = get_object_or_404(ParentBreed, name=breed_name)
        # return qs.filter(kind__name=kind_name)
        return qs.filter(breed=breed)


class ParentDetailView(DetailView):
    template_name = "parents/details.html"
    context_object_name = "parent"
    model = Parent
    # queryset = Parent.objects.select_related("breed", "color")


class ParentCreateView(CreateView):
    model = Parent
    form_class = ParentCreateForm
    success_url = reverse_lazy("parents:index")

    # def post(self, request, *args, **kwargs):
    #     get_request_info.delay(url=request.path, method=request.method)
    #     return super().post(request, *args, **kwargs)
    #
    # def get(self, request, *args, **kwargs):
    #     get_request_info.delay(url=request.path, method=request.method)
    #     return super().get(request, *args, **kwargs)
    #
    # def test_func(self):
    #     return self.request.user.is_staff or self.request.user.is_superuser
    #
    # def get_success_url(self):
    #     task = notify.delay(self.object.name, self.object.kind.name)
    #     print("ID", task.id)
    #     get_request_info.delay(url="TEST", method="TEST")
    #     return reverse("animals:details", kwargs={"pk": self.object.pk})


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
