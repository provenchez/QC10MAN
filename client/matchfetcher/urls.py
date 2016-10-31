from django.conf.urls import url

from . import views

app_name = 'matchfetcher'
urlpatterns = [
    # ex: /matchfetcher/
    url(r'^$', views.index, name='index'),
    # ex: /matchfetcher/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /matchfetcher/5/results/
    url(r'^/results', views.results, name='results'),
    # ex: /matchfetcher/5/vote/
    url(r'^getMatch', views.getMatch, name='getMatch'),
]