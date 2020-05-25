from rest_framework import serializers
from .models import user,activity
class activitySerializer(serializers.ModelSerializer):
    class Meta:
        model=activity
        fields=('start_time',"end_time")
class userSerializer(serializers.ModelSerializer):
     activity_periods =activitySerializer(read_only=True, many=True)
     class Meta:
        model=user
        fields=('id','user','tz','activity_periods')