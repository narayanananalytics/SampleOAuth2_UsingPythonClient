from django.urls import re_path
from django.views.generic.base import RedirectView
from . import views

app_name = 'app'

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^oauth/?$', views.oauth, name='oauth'),
    re_path(r'^openid/?$', views.openid, name='openid'),
    re_path(r'^callback/?$', views.callback, name='callback'),
    re_path(r'^connected/?$', views.connected, name='connected'),
    re_path(r'^qbo_request/?$', views.qbo_request, name='qbo_request'),
    re_path(r'^revoke/?$', views.revoke, name='revoke'),
    re_path(r'^refresh/?$', views.refresh, name='refresh'),
    re_path(r'^user_info/?$', views.user_info, name='user_info'),
    re_path(r'^chart_of_accounts/?$', views.chart_of_accounts, name='chart_of_accounts'),
    re_path(r'^journal_entries/?$', views.journal_entries, name='journal_entries'),
    re_path(r'^profit_and_loss/?$', views.profit_and_loss, name='profit_and_loss'),
    re_path(r'^migration/?$', views.migration, name='migration'),
]
