from django.http import HttpResponse
from wsgiref.util import FileWrapper

from django.http import FileResponse
from django.shortcuts import render
from rest_framework import permissions, viewsets, views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
# Create your views here.

class FrontPageView(views.View):
    def get(self, request):
        return render(request, 'frontPage.html')

