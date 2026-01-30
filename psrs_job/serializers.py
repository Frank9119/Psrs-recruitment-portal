from rest_framework import serializers
from .models import Job, JobsApplications




class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobsApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobsApplications
        fields = '__all__'