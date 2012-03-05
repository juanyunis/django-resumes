from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('resumes.views',
    url(r'^$', 'list_resume', name='resumes_list'),
    url(r'^view/(?P<resume_id>\d+)/$', 'view_resume', name='resumes_view'),
    url(r'^view/user/(?P<user_id>\d+)/$', 'view_resume', name='resumes_view_user'),

    url(r'^export/(?P<resume_id>\d+)/$', 'export_resume', name='resumes_export'),
    url(r'^export/user/(?P<user_id>\d+)/$', 'export_resume', name='resumes_export_user'),
)