from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^start_game/$',views.start_game, name = 'start_game'),
    url(r'^game/$',views.game, name = 'game'),
]
