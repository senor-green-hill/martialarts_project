from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from django.http import HttpResponse
from .models import Rank, Category, Requirement


# Create your views here.
class RankListView(ListView):
    model = Rank

class RankDetailView(DetailView):
    model = Rank
    pk_url_kwarg = 'rank_id'

class CategoryDetailView(DetailView):
    model = Category
    pk_url_kwarg = 'category_id'

class RequirementDetailView(DetailView):
    model = Requirement
    pk_url_kwarg = 'requirement_id'