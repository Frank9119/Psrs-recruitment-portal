from django.db import models
from psrs_auth.models import UserProfile
from psrs_mixin.models import BaseModel





JOBS_LOCATIONS = (
    ('REMOTE', 'Remote'),
    ('DAR_ES_SALAAM', 'Dar_es_salaam'),
    ('OTHERS', 'Others')
)


# Create your models here.
class Job(BaseModel):
    title = models.TextField(max_length=255)
    description =  models.TextField()
    location = models.CharField(max_length=40, choices=JOBS_LOCATIONS, default="OTHERS")
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    ## other added columns
    qualifications = models.TextField()
    responsibilities = models.TextField()
    deadline = models.DateTimeField()


    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['-primary_key']

    def __str__(self):
        return f"{self.title}"
    
    def get_applications_list(self):
        return self.jobs.filter(is_active=True)



class JobsApplications(BaseModel):
    applicant = models.ForeignKey(UserProfile, related_name="applicant_profile", on_delete=models.CASCADE)
    job = models.ForeignKey(Job, related_name="jobs", on_delete=models.CASCADE)
    cv = models.FileField(upload_to="cvs/", validators=[])
    cover_leter = models.FileField(upload_to="cover_leter/", validators=[])

    class Meta:
        verbose_name = 'Job_application'
        verbose_name_plural = 'Job_applications'
        ordering = ['-primary_key']

    def __str__(self):
        return f"{self.applicant} - {self.job.title}"