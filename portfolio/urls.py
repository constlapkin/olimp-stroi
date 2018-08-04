from django.conf.urls import url
from portfolio.views import *


urlpatterns = [
    url(r'^$', ProjectsList.as_view(), name='portfolio'),
    url(r'^(?P<id>\d+)/$', project_view, name='project'),
]
