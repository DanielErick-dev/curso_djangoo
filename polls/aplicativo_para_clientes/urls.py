from django.urls import path
from . import views

app_name = 'aplicativo_para_clientes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote/', views.Vote, name='vote')
]