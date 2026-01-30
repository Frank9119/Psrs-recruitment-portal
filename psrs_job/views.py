from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from psrs_job.serializers import JobsApplicationsSerializer, JobSerializer
from .permission import IsApplicant, IsAdmin, IsRecuiter
from .models import Job, JobsApplications




# Create your views here.
class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsApplicant]
    



class JobApplicationViewSet(ModelViewSet):
    queryset = JobsApplications.objects.all()
    serializer_class = JobsApplicationsSerializer
    permission_classes = [IsAuthenticated, IsApplicant]

    def get_queryset(self):
        return JobsApplications.objects.filter(applicant__user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user.profile)

     
