from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
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
    url(r'^addGood$', 'webStore.views.addGoods', name = 'addGood'),
    url(r'^ajax/addGoods', 'webStore.ajax.uploadimage'),
    url(r'^ajax/goods$', 'webStore.ajax.goods'),
    url(r'^ajax/goodsList$', 'webStore.ajax.goodsList'),
    url(r'^specification$', 'webStore.views.specification'),
    url(r'^ajax/comments$', 'webStore.ajax.comments'),
    url(r'^$', 'webStore.views.mainPage'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

