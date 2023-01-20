from django.urls import path, include
from . import views

app_name = 'cardgame'

urlpatterns = [
    path('list_game/', views.list_game, name='list_game'),
    path('<int:pk>/delete_game/', views.delete_game, name='delete_game'),
    path('<int:pk>/detail_game/',views.detail_game,name='detail_game'),
    path('attack', views.attack_game, name="attack"),
    path('defense', views.defense_game, name="defense"),
    ]
