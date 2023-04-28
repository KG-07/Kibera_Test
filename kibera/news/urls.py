from django.urls import path
from . import views
urlpatterns = [
    path('', views.NewsListApiView.as_view()),
    path('create/', views.NewsCreateAPIView.as_view()),
    path('<int:pk>', views.NewsRetrieveAPIView.as_view()),
    path('<int:pk>/update', views.NewsUpdateAPIView.as_view()),
    path('<int:pk>/delete', views.NewsDestroyAPIView.as_view()),
]