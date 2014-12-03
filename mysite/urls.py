from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'blog.views.index', name='index'),
    url('^blog/archive/(?P<year>[\d]+)/(?P<month>[\d]+)/$', 'blog.views.article.date_archive', name="blog-date-archive"),
    url('^blog/archive/(?P<slug>[-\w]+)/$', 'blog.views.article.category_archive', name="blog-category-archive"),
    url('^blog/(?P<slug>[-\w]+)/$', 'blog.views.article.single', name="blog-article-single"),
    url('^blog/$', 'blog.views.article.index', name="blog-article-index"),
    url(r'^admin/', include(admin.site.urls)),
)



