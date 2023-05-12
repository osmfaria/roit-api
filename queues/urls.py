from django.urls import path

from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from . import views

urlpatterns = [
    path('cnae/', views.QueueView.as_view(), name="queue-view"),
    path('cnae/remove/', views.QueueDeleteView.as_view(), name="queue_delete-view"),
    path('cnae/filter/', views.QueueFilterView.as_view(), name="queue_filter-view"),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
