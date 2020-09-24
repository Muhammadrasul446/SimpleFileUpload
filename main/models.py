from django.db import models

class FormFile(models.Model):
    file = models.FileField(upload_to="data/form_files")

    def __str__(self):
        return self.file.url
    
    class Meta:
        verbose_name = "Form file"
        verbose_name_plural = "Form files"