from django.db import models

# Create your models here.
class Speaker(models.Model):
    sid = models.CharField(max_length=20)
    fname= models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    topic = models.CharField(max_length=200)

    def __str__(self) -> str:
        return "%s"% (self.fname)
    class Meta:
        db_table = "speaker"

