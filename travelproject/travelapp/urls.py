import os

from django.conf.urls.static import static

from travelproject import settings
from travelproject.settings import BASE_DIR
from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    # path("result/",views.operation,name="operation"),
    # path("contact/",views.contact,name="contact")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
