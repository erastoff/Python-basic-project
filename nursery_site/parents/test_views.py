from datetime import datetime

from django.test import TestCase

from parents.models import Parent, ParentBreed, ParentGender, ParentColor


class ParentListView(TestCase):
    def test_response_status_code(self):
        response = self.client.get("/parents/")
        self.assertEqual(response.status_code, 200)

    def test_response_context(self):
        response = self.client.get("/parents/")
        self.assertIn("help_text", response.context)
        self.assertEqual(response.context["help_text"], "For your help!")
        self.assertEqual(response.status_code, 200)

    def tests_parent_detail(self):
        response = self.client.get("/parents/999/")
        self.assertEqual(response.status_code, 404)
        birth = datetime(2011, 11, 11, 23, 55, 59, 342380)
        height = 0.5
        weight = 2
        breed = ParentBreed.objects.create(name="test_breed")
        gender = ParentGender.objects.create(name="test_gender")
        color = ParentColor.objects.create(name="test_color")

        parent = Parent.objects.create(
            name="test_name",
            birth=birth,
            height=height,
            weight=weight,
            breed=breed,
            gender=gender,
            color=color,
        )

        response = self.client.get(f"/parents/{parent.pk}/")
        self.assertEqual(response.status_code, 200)
