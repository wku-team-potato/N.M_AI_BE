from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import SyncDetectionView

urlpatterns = [
    path('detection/', SyncDetectionView.as_view(), name='detection'),
]
