from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('form_files/', views.FormFileList.as_view()),
    path('form_files/<int:pk>/', views.FormFileDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)