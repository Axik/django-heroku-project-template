from django.conf.urls import patterns, url

urlpatterns = patterns(
    'profiles.views',
    url(r'^$', 'user_detail', name='detail'),
)
