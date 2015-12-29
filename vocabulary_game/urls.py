from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
            url(r'^create/$', views.WordCreate.as_view(), name='word-create'),
            #url(r'^update/(?P<pk>\d+)$', login_required(views.LotteryUserUpdate.as_view()), name='lotteryuser-update'),
            #url(r'^delete/(?P<pk>\d+)$', login_required(views.LotteryUserDelete.as_view()), name='lotteryuser-delete'),
            #url(r'^logout/$', auth_views.logout, name="logout"),
            #url(r'^$', auth_views.login, name="login"),
            ]
