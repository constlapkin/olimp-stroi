from django.conf.urls import url
from main.views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^contacts/$', contacts, name='contacts'),
    url(r'^about/$', about, name='about'),
    url(r'^services/$', ServicesList.as_view(), name='services'),  # Возможно будет приложением, в случае имения готовых проектов для клиентов
    url(r'^sitemap/$', sitemap, name='sitemap'),
]
