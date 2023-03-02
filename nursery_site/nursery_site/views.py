from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    context = {
        "active_cont": [
            ("parents:index", "DOGS!"),
            ("parents:breeds", "BREEDS!"),
            ("puppies:index", "PUPPIES!"),
        ],
        # 'labels': ['label1', 'label2', 'label3'],
    }
    return render(request=request, template_name="index.html", context=context)
