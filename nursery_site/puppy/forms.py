from django.forms import ModelForm, Widget

from puppy.models import PuppyBrood, Puppy


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
            # widget.attrs["aria - label"] = "Username"
            # widget.attrs["aria - describedby"] = "basic-addon1"


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name, field, field.widget)
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"
