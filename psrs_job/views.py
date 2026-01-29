from django.shortcuts import render
from django.http import HttpResponse

## djangorestframework
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.
@api_view()
def get_jobs_list(request):
    return Response('Operation Successfully')

@api_view()
def get_applications_list(request, id):
    return Response(id)