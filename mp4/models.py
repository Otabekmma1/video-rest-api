from django.core.validators import FileExtensionValidator
from django.db import models

class DowloandVideo(models.Model):
    file = models.FileField(upload_to='media/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'WMV', 'png'])
    ])