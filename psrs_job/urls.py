from django.urls import path
from . import views



# URL Configurations
urlpatterns = [
    path('jobs/', views.get_jobs_list),
    path('applications/<id>/', views.get_applications_list),
]
