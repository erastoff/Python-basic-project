from django.db import models


class ParentBreed(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return str(self.name)


class ParentGender(models.Model):
    name = models.CharField(max_length=6)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return str(self.name)


class ParentColor(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return str(self.name)


class Parent(models.Model):
    name = models.CharField(max_length=64)
    birth = models.DateTimeField()
    height = models.FloatField()
    weight = models.FloatField()
    description = models.TextField(blank=True, null=False)

    breed = models.ForeignKey(
        ParentBreed, on_delete=models.PROTECT, related_name="parent", null=True
    )
    gender = models.ForeignKey(
        ParentGender, on_delete=models.PROTECT, related_name="parent", null=True
    )
    color = models.ForeignKey(
        ParentColor, on_delete=models.PROTECT, related_name="parent", null=True
    )
    archived = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)


class ParentKennel(models.Model):
    dog = models.OneToOneField(Parent, on_delete=models.CASCADE, related_name="kennel")
    number = models.PositiveIntegerField(unique=True, null=True)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return f"Dog #{self.dog.name} from {self.number} kennel"
