from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse


def trigger_error(request):
    try:
        division_by_zero = 1 / 0
    except Exception:
        division_by_zero = "Hello World"
    return HttpResponse(division_by_zero)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('sentry-debug/', trigger_error),
]
