from datetime import datetime

from django.test import TestCase
from .models import Parent, ParentBreed, ParentGender, ParentColor


# Create your tests here.
class TestParent(TestCase):
    def setUp(self):
        self.breed = ParentBreed.objects.create(name="breed_test")
        print("Run before each test")

    def tearDown(self):
        print("Run after each test")

    def test_str(self):
        self.assertTrue(isinstance(self.breed.name, str))
        self.assertEqual(self.breed.name, "breed_test")

    def test_wrong(self):
        breed = ParentBreed.objects.create(name="BREED")
        self.assertEqual(breed.name, "BREED")


class TestAnimals(TestCase):
    def test_str(self):
        birth = datetime(2011, 11, 11, 23, 55, 59, 342380)
        height = 0.5
        weight = 2
        breed = ParentBreed.objects.create(name="test_breed")
        gender = ParentGender.objects.create(name="test_gender")
        color = ParentColor.objects.create(name="test_color")

        animal = Parent.objects.create(
            name="test_name",
            birth=birth,
            height=height,
            weight=weight,
            breed=breed,
            gender=gender,
            color=color,
        )
        self.assertEqual(str(animal), "test_name")


# class TestProfile(TestCase):
#     def test_phone_number_overflow(self):
#         kind = AnimalKind.objects.create(name="bear")
#         animal = Animal.objects.create(name="John", kind=kind, age=1)
#         # print('MUST BE ERROR!')
#         # with self.assertRaises(Exception):
#         #     profile = AnimalProfile.objects.create(animal=animal, phone_number='12345678910')
#         #     print(profile.phone_number)
#         #     print(profile)
