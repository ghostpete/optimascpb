
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.conf.urls import handler404
from django.http import FileResponse
import os

from django.views.generic import TemplateView


admin.site.site_header = "JPCiti Bank Administration"
admin.site.site_title = "JPCiti Bank Admin Portal"
admin.site.index_title = "Welcome to JPCiti Bank Admin Portal"


def serve_google_verification(request):
    file_path = os.path.join(os.path.dirname(__file__), "../googlec0404b193ee28243.html")
    print(file_path)
    return FileResponse(open(file_path, 'rb'))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('googlec0404b193ee28243.html', serve_google_verification),
    path('api/', include('api.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Error Pages -- ATTEND TO THIS LATER

def not_found(request, exception):
    # return render(request, 'not_found.html', {})
    return render(request, 'main/404.html', {})

handler404 = 'online_b_f.urls.not_found'
