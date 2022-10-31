from django.db import models
from parents.models import Parent as Parent


class PuppyGender(models.Model):
    class Meta:
        verbose_name_plural = "Puppy gender"

    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name


class PuppyStatus(models.Model):
    class Meta:
        verbose_name_plural = "Puppy status"

    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name


class PuppyBreed(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=False)
    color = models.ManyToManyField("PuppyColor", related_name="breed")

    def __str__(self):
        return self.name


class PuppyColor(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name


class PuppyBrood(models.Model):
    date = models.DateTimeField()
    sire = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        limit_choices_to={"gender": 1},
        related_name="sire",
    )
    bitch = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        limit_choices_to={"gender": 2},
        related_name="bitch",
    )


class Puppy(models.Model):
    class Meta:
        verbose_name_plural = "Puppy"

    name = models.CharField(max_length=64)
    birth = models.DateTimeField(null=True)
    status = models.ForeignKey(
        PuppyStatus, on_delete=models.CASCADE, null=True
    )  # OneToMany
    breed = models.ForeignKey(
        PuppyBreed, on_delete=models.CASCADE, null=True
    )  # OneToMany
    color = models.ForeignKey(PuppyColor, on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey(PuppyGender, on_delete=models.CASCADE, null=True)
    brood = models.ForeignKey(
        PuppyBrood, on_delete=models.CASCADE, related_name="puppy", null=True
    )

    description = models.TextField(blank=True, null=False)
