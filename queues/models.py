import uuid

from django.db import models


class Queue(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    section_code = models.CharField(max_length=5)
    section_name = models.TextField()
    division_code = models.CharField(max_length=5)
    division_name = models.TextField()
    group_code = models.CharField(max_length=10)
    group_name = models.TextField()
    class_code = models.CharField(max_length=10)
    class_name = models.TextField()
    subclass_code = models.CharField(max_length=15)
    subclass_name = models.TextField()
