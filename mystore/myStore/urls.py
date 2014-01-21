from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myStore.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^category/list/$', 'webStore.views.categoryList'),
    url(r'^test/$', 'webStore.views.test'),
    url(r'^ajaxexample$', 'webStore.views.main'),
    url(r'^ajaxexample_json$', 'webStore.views.ajax'),
    url(r'^goods$', 'webStore.views.goods'),
    url(r'^ajax/goods$', 'webStore.ajax.goods'),
    url(r'^$', 'webStore.views.mainPage'),
)

urlpatterns += staticfiles_urlpatterns()