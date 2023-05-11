from django.urls import path

from . import views

urlpatterns = [
    path('cnab/', views.QueueView.as_view(), name="queue-view"),
    path('cnab/remove/', views.QueueDeleteView.as_view(), name="queue_delete-view")
]