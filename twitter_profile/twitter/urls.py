from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^login', auth_views.login, {"template_name":"login.html"}),
    url(r'^logout', views.logout),
    url(r'^follow', views.follow),
    url(r'^unfollow', views.unfollow),
    url(r'^profile', views.profile),
    url(r'^tweet/(?P<tweet_id>\d+)/delete', views.delete_tweet),
    url(r'^(?P<username>\w+)$', views.home),
    url(r'^$', views.home),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
