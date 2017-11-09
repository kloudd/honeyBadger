from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^parserapp/', include('parserApp.urls')),
    url(r'^admin/', admin.site.urls),
]