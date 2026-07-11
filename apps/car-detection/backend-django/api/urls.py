from django.urls import path
from . import views

urlpatterns = [
    path('detect/image/', views.DetectImageView.as_view(), name='detect_image'),
    path('detect/frame/', views.DetectFrameView.as_view(), name='detect_frame'),
    path('model/info/', views.ModelInfoView.as_view(), name='model_info'),
    path('health/', views.HealthView.as_view(), name='health'),
]
