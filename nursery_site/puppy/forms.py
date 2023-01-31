from django.forms import ModelForm, Widget

from puppy.models import PuppyBrood, Puppy
from nursery_site.settings import DEBUG


class BroodCreateForm(ModelForm):
    class Meta:
        model = PuppyBrood
        fields = (
            "date",
            "sire",
            "bitch",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"
            if DEBUG:
                print(name, field, field.widget)


class PuppyCreateForm(ModelForm):
    class Meta:
        model = Puppy
        fields = (
            "name",
            "birth",
            "status",
            "breed",
            "color",
            "gender",
            "brood",
            "description",
        )
        # widgets = {
        #     'brood': forms.HiddenInput(),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"
            if DEBUG:
                print(name, field, field.widget)
