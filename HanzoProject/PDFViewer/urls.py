from django.urls import include, path
from rest_framework import routers

from PDFViewer import views

urlpatterns = [
    path('FrontPage', views.FrontPageView.as_view(), name='FrontPage'),
]




