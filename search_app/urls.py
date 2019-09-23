from django.urls import path
from search_app import views
urlpatterns = [
    path('',views.index,name="index"),
    path('requested_game/', views.requested_game, name='requested_game'),
]
