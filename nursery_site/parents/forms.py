from django.forms import ModelForm, Widget

from parents.models import Parent
from nursery_site.settings import DEBUG


class ParentCreateForm(ModelForm):
    class Meta:
        model = Parent
        fields = (
            "name",
            "birth",
            "height",
            "weight",
            "description",
            "breed",
            "gender",
            "color",
        )

    # name = CharField(max_length=20, label="Animal name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"
            if DEBUG:
                print(name, field, field.widget)
