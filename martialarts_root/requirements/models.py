from django.db import models
        
        
class Rank (models.Model):
    degree       = models.CharField(max_length = 20)
    color        = models.CharField(max_length = 20)
    position     = models.IntegerField()
    eligibility  = models.TextField(blank = True)
    # requirements = models.ManyToManyField(Requirement)
    #categories  = models.ManyToManyField(Category)

    def __str__(self):
        return self.color

    @property
    def rank_categories(self):
        return self.categories.all().order_by('position')


# Individual requirements (i.e. Ki Cho 4, Middle Block, Horse Kick, etc.)
class Requirement (models.Model):
    title       = models.CharField(max_length=20)
    position    = models.IntegerField()
    video_url   = models.CharField(max_length=20, blank = True)
    desc        = models.TextField(blank = True)
    # category    = models.ForeignKey(Category)
    # ranks       = models.ManyToManyField(Rank)

    def __str__(self):
        return self.title

    # @property
    # def requirement_categories(self):
    #     return self.category.order_by('position')

# One category may have the same name but with different ranks
class Category (models.Model):
    name            = models.CharField(max_length=20)
    position        = models.IntegerField()
    assoc_rank      = models.CharField(max_length=20)
    #requirements    = models.ManyToManyField(Requirement)
    ranks = models.ManyToManyField(Rank)

    def __str__(self):
        return self.ra1 self.name

    @property
    def category_ranks

    @property
    def cat_requirements(self):
        return self.requirements.all().order_by('position')