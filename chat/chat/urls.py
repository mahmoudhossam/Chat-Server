from django.conf.urls import patterns, include, url
from api import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/$', views.UserView.as_view()),
    url(r'^messages/$', views.MessageView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
