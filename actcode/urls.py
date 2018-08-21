from django.conf.urls import url

from actcode.views import ProjectView, CodeView, ProjectListView

app_name = 'reviews'
urlpatterns = [
    url("^$", ProjectListView.as_view(), name="projectlist"),
    url("^project/(?P<project>[0-9]+)/$", ProjectView.as_view(), name="project"),
    url("^project/(?P<project>[0-9]+)/code-gold/(?P<label>[0-9]+)/$", CodeView.as_view(), name="code-gold"),
]