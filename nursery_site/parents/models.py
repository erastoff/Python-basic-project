from django.db import models


class ParentBreed(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name


class ParentGender(models.Model):
    name = models.CharField(max_length=6)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name


class ParentColor(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name


class Parent(models.Model):
    name = models.CharField(max_length=64)
    breed = models.ForeignKey(ParentBreed, on_delete=models.PROTECT, related_name="parent")
    gender = models.ForeignKey(ParentGender, on_delete=models.PROTECT, related_name="parent")
    color = models.ForeignKey(ParentColor, on_delete=models.PROTECT, related_name="parent")
    birth = models.DateTimeField()
    height = models.FloatField()
    weight = models.FloatField()
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name

    # kind = models.ForeignKey(AnimalKind, on_delete=models.PROTECT, related_name="animal")
    # food = models.ManyToManyField("parents.AnimalFood", related_name="parents")


class ParentKennel(models.Model):
    dog = models.OneToOneField(Parent, on_delete=models.CASCADE, related_name="kennel")
    number = models.PositiveIntegerField(unique=True)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return f"Dog #{self.dog.pk} from {self.number} kennel"
