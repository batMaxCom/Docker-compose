from django.urls import path
from .views import SensorView, SensorUpdateView, MeasurementView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorUpdateView.as_view()),
    path('measurements/', MeasurementView.as_view()),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
