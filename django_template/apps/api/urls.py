from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'test', 'django_template.apps.api.views.test'),
)