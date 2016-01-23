from django.conf.urls import include, url, patterns
from django.contrib import admin
from restaurante import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'restaurante.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# static files (images, css, javascript, etc.)
urlpatterns += patterns('',
    (r'^docs/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}
    ))
urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root':settings.STATIC_ROOT}
    ))