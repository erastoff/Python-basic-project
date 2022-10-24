from django.db import models


class PuppyStatus(models.Model):
    class Meta:
        verbose_name_plural = "Puppy status"
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name


# class PuppyBreed(models.Model):
#     class Meta:
#         verbose_name_plural = "Puppy breed"
#     name = models.CharField(max_length=32)
#     description = models.TextField(blank=True, null=False)
#
#     def __str__(self):
#         return self.name


class Puppy(models.Model):
    class Meta:
        verbose_name_plural = "Puppy"
    name = models.CharField(max_length=64)
    status = models.ForeignKey(PuppyStatus, on_delete=models.PROTECT, related_name="puppy") # OneToMany
    # breed = models.ForeignKey(PuppyBreed, on_delete=models.PROTECT, related_name="puppy") # OneToMany
    # color = models.ForeignKey(ParentColor, on_delete=models.PROTECT, related_name="parent")
    birth = models.DateTimeField()
    # height = models.FloatField()
    # weight = models.FloatField()
    description = models.TextField(blank=True, null=False)
