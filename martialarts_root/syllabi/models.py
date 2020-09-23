from django.db import models

# Forms to be completed in order to rank up
class Hyung (models.Model):
    name        = models.CharField(max_length = 20)     # Ki Cho 1, Pyong Ahn 4, Bassai So, etc.
    position    = models.IntegerField()                 # Position in series
    video_url   = models.CharField(max_length = 200)
    desc        = models.TextField(blank = True)        # Blocks, Hand Techniques, etc. used

    def __str__(self):
        return self.name

class Rank (models.Model):
    degree      = models.CharField(max_length = 20)     # 8th Gup, 2nd Dan, etc.
    beltColor   = models.CharField(max_length = 20)     # Yellow Stripe, Black Belt
    position    = models.IntegerField()                 # Position in ranking
    eligibility = models.TextField(blank = True)        # Rank up requirements
    hyung       = models.ManyToManyField(Hyung)         # Hyung associated with a particular rank 

    def __str__(self):
        return self.beltColor            # i.e. 7th Gup: Green Stripe

    @property
    def ranks(self):
        return self.ranks_set.all().order_by('position')

    # Hyung of previous ranks may be included in more advanced ranks.
    @property
    def rank_hyung(self):
        return self.hyung.all().order_by('position')