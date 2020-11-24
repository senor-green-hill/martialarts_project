from django.db import models

class Rank (models.Model):
    slug        = models.SlugField(blank=True)
    degree       = models.CharField(max_length = 20)
    color        = models.CharField(max_length = 20)
    position     = models.IntegerField()
    #eligibility  = models.TextField(blank = True)

    def __str__(self):
        return self.color

    @property
    def categories(self):
        return self.category_set.all().order_by('position')
    
    @property
    def rank_elegibility(self):
        return self.elegibility_set.all().order_by('position')

class Eligibility (models.Model):
    summary     = models.CharField(max_length = 20)
    position    = models.IntegerField()
    desc        = models.TextField(blank = True)
        
# Categories for a Rank. (i.e. Yellow Belt Hand Techniques, Black Belt Hand Techniques)
class Category (models.Model):
    slug            = models.SlugField(blank = True)
    name            = models.CharField(max_length=20)
    position        = models.IntegerField()
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "%s %s" % (self.rank, self.name)

    @property
    def requirements(self):
        return self.requirement_set.all().order_by('position')

# Individual requirements (i.e. Ki Cho 4, Middle Block, Horse Kick, etc.)
class Requirement (models.Model):
    slug        = models.SlugField(blank = True)
    title       = models.CharField(max_length=100)
    position    = models.IntegerField()
    desc        = models.TextField(blank = True)
    category    = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    @property
    def media(self):
        return self.media_set.all().order_by('position')

# Images, videos, etc. associated with a particular requirement.
class Media (models.Model):
    file_name   = models.CharField(max_length=20)
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    desc        = models.TextField(blank=True)
    position    = models.IntegerField()

    def __str__(self):
        return self.file_name