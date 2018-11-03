from django.conf.urls import url, include
from portfolio.views import *


urlpatterns = [
    url(r'^portfolio/$', ProjectsList.as_view(), name='portfolio'),
    url(r'^portfolio(?P<id>\d+)/$', project_view, name='project'),
    url(r'^$', index, name='index'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^about/$', about, name='about'),
    url(r'^services/$', ServicesList.as_view(), name='services'),  # Возможно будет приложением, в случае имения готовых проектов для клиентов
    url(r'^sitemap/$', sitemap, name='sitemap'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
