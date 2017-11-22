from django.conf.urls import url
from blog.views import *


urlpatterns = [
    url(r'^posts/(?P<post_id>[0-9]+)/comments/$', add_com, name='add_com'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', post_view, name='post'),
    url(r'^posts/$', add, name='add'),
    url(r'^register/$', RegisterFormView.as_view()),
    url(r'^login/$', LoginFormView.as_view()),
    url(r'^logout/$', LogoutView.as_view()),

    url(r'^$', post_all, name='list'),

]