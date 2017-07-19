from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^trails/', include('trails.urls')),
    url(r'^admin/', admin.site.urls),
]
