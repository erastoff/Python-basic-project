from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import ParentCreateForm
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
