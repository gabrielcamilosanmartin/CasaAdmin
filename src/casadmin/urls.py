from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('casadmin.core.urls')),
    path('users/', include('casadmin.users.urls')),
    path('credentials/', include('casadmin.credentials.urls')),
    path('admin/', admin.site.urls),
]