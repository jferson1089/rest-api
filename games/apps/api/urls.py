from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SystemListView, SystemUpdateView, SystemCreateView
from .views import GamesListView, GamesUpdateView, GamesCreateView

urlpatterns=[
    url(r'^systemlist/$', SystemListView.as_view(), name='systemlist'),
    url(r'^systemadd/$', SystemCreateView.as_view(), name='systemadd'),
    url(r'^systemupdate/(?P<pk>[0-9]+)/$', SystemUpdateView.as_view(), name='systemupdate'),
    url(r'^gamelist/$', GamesListView.as_view(), name='gamelist'),
    url(r'^gameadd/$', GamesCreateView.as_view(), name='gameadd'),
    url(r'^gameupdate/(?P<pk>[0-9]+)/$', GamesUpdateView.as_view(), name='gameupdate'),
]