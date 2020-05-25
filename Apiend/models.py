from django.db import models

# Create your models here.
class user(models.Model):
    id=models.CharField(max_length=10,primary_key=True)
    user=models.CharField(max_length=10)
    tz=models.CharField(max_length=10)
class activity(models.Model):
    foriegn_id=models.ForeignKey(user,related_name="activity_periods",on_delete=models.CASCADE)
    start_time=models.CharField(max_length=40)
    end_time=models.CharField(max_length=40)
    def __str__(self):
        return 'start_time:%s, end_time:%s' %(self.start_time,self.end_time)
