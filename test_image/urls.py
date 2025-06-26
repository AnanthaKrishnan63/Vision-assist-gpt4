from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import picture_view, success, submit_text

urlpatterns = [
    path('submit_text', submit_text, name='submit_text'),
	path('Vision', picture_view, name='Vision'),
	path('success', success, name='success'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
						document_root=settings.MEDIA_ROOT)

