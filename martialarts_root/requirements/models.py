from django.db import models

# Create your models here.
class Requirement (models.Model):
    title       = models.CharField(max_length=20)
    position    = models.IntegerField()
    video_url   = models.CharField(max_length=20)
    desc        = models.TextField(blank = True)

    def __str__(self):
        return self.title

class Category (models.Model):
    name        = models.CharField(max_length=20)
    position    = models.IntegerField()
    requirement = models.ManyToManyField(Requirement)

    def __str__(self):
        return self.name

class Rank (models.Model):
    degree      = models.CharField(max_length = 20)
    color       = models.CharField(max_length = 20)
    position    = models.IntegerField()
    eligibility = models.TextField(blank = True)
    category    = models.ManyToManyField(Category)

    def __str__(self):
        return self.color