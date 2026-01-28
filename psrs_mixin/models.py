import uuid
from django.db import models


# Create the Basemodel
class BaseModel(models.Model):
    primary_key = models.AutoField(primary_key=True)
    unique_id = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    # created_by = 


    class Meta:
        abstract = True



