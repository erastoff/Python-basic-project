from django.test import TestCase
from django.utils.datetime_safe import datetime

from parents.models import Parent, ParentBreed, ParentGender, ParentColor


class ParentListView(TestCase):
    def setUp(self):
        self.birth = datetime(2011, 11, 11, 23, 55, 59, 342380)
        self.height = 0.5
        self.weight = 2
        self.breed = ParentBreed.objects.create(name="test_breed")
        self.gender = ParentGender.objects.create(name="test_gender")
        self.color = ParentColor.objects.create(name="test_color")

        self.parent = Parent.objects.create(
            name="test_name",
            birth=self.birth,
            height=self.height,
            weight=self.weight,
            breed=self.breed,
            gender=self.gender,
            color=self.color,
        )

    def tearDown(self):
        print("OK: ", (self))

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

        response = self.client.get(f"/parents/{self.parent.pk}/")
        self.assertEqual(response.status_code, 200)
