from django.urls import path

from .views import RankListView, RankDetailView, HyungDetailView
from . import views

urlpatterns = [
    path('', RankListView.as_view(), name = 'rank_list_view'),
    #path('<int:rank_id>/', RankDetailView.as_view(), name = 'rank_detail_view'),
    #path('<int:rank_id>/<int:hyung_id>/', HyungDetailView.as_view(), name= 'hyung_detail_view'),
]