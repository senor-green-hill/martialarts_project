from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from django.http import HttpResponse
from .models import Rank, Hyung

# Create your views here.
class RankListView(ListView):
    model = Rank

class RankDetailView(DetailView):
    model = Rank
    pk_url_kwarg = 'rank_id'

class HyungDetailView(LoginRequiredMixin, DetailView):
    model = Hyung
    pk_url_kwarg = 'hyung_id'