from django.contrib import admin
from .models import Requirement, Category, Rank, Media, Eligibility

# Register your models here.
class RankAdmin(admin.ModelAdmin):
    ordering = ('position')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('rank', 'name')
    ordering = ('position')
    search_fields = ('rank', 'name')

class RequirementAdmin(admin.ModelAdmin):
    list_display = ('category', 'title')

admin.site.register(Requirement, RequirementAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(Media)
admin.site.register(Eligibility)