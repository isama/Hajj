from django.conf.urls import patterns, url
from Web import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^sign_in', views.sign_in, name='sign_in'),
    url(r'^sign_out', views.sign_out, name='sign_out'),

    url(r'^qa_view', views.qa_view, name='qa_view'),
    url(r'^camp_view', views.camp_view, name='camp_view'),
    url(r'^executive_view', views.executive_view, name='executive_view'),

    url(r'^log_action/(?P<activity_id>\d+)', views.log_action, name='log_action'),
    url(r'^supervisor_detail', views.supervisor_detail, name='supervisor_detail'),
    url(r'^camp_detail', views.camp_detail, name='camp_detail'),
)