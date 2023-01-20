from datetime import datetime

from django.test import TestCase

from .models import Parent, ParentBreed, ParentGender, ParentColor


class TestParentBreed(TestCase):
    def setUp(self):
        self.breed = ParentBreed.objects.create(name="breed_test")

    def tearDown(self):
        print("OK: ", self.__str__())

    def test_str(self):
        self.assertTrue(isinstance(self.breed.name, str))
        self.assertEqual(self.breed.name, "breed_test")

    def test_wrong(self):
        breed = ParentBreed.objects.create(name="BREED")
        self.assertEqual(breed.name, "BREED")


class TestParents(TestCase):
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
        # print("Completed successfully!")
        print("OK: ", self.__str__())

    def test_str(self):
        self.assertEqual(str(self.parent.name), "test_name")
        self.assertEqual(str(self.parent.color), "test_color")
        self.assertNotEqual(self.parent.birth, datetime(2000, 1, 1, 1, 1, 1, 11111))
