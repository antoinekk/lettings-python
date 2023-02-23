from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
]
