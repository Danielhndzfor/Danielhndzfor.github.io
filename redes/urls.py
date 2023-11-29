import re
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tutoriales.urls')),
]

if settings.STATIC_URL.startswith("/"):
    urlpatterns += [
        re_path(
            r'^{STATIC_URL}(?P<path>.*)$'.format(STATIC_URL=re.escape(settings.STATIC_URL.lstrip('/'))),
            serve,
            {'document_root': settings.STATIC_ROOT},
        ),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
