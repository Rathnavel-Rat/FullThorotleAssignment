from django.core.management.base import BaseCommand
from Apiend.models import user,activity

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self):
      obj1=user(id="dg45euh8",user="mac jons",tz="Asia/Russia")
      obj1.save()
      act1=activity(foriegn_id=obj1,start_time="march 29  2:00pm ",end_time="March 29 8.00pm")
      act1.save()
      act11=activity(foriegn_id=obj1,start_time="april 7  2:00pm ",end_time="april 7 8.00pm")
      act11.save()
      obj2=user(id="84hfish",user="Tom Grace",tz="Asia/china")
      obj2.save()
      act2=activity(foriegn_id=obj2,start_time="march 1  5:00am ",end_time="March 1 11.00am")
      act2.save()
      act22=activity(foriegn_id=obj2,start_time="april 9   5:00am ",end_time="april 9  11.00am")
      act22.save()
      obj3=user(id="bfn83f9",user="Kallena Prince",tz="Asia/India")
      obj3.save()
      act3=activity(foriegn_id=obj3,start_time="April 4  10:00am ",end_time="April 4 2.00am")
      act3.save()
      act33=activity(foriegn_id=obj3,start_time="may 5   5:00am ",end_time="may 5 11.00am")
      act33.save()
       
    def handle(self, *args, **options):
        self._create_tags()






      