import json
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        from django.conf import settings
        import sys
        from barman.models import Diagnose
   
        import subprocess
        process = subprocess.Popen(['barman', 'diagnose'],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        data = (json.loads(stdout))
        
        try:
            item = Dianose.objects.get(name='config')
        except Dianose.DoesNotExist:
            item = False
    
        dictionary = {}
        dictionary['data'] = data
        dictionary['name'] = 'config'
    
        #removed
        #dictionary['zone'] = data_pool.get('name_description')
    
        if item:
            serializer = DiagnoseSerializer(item, data=dictionary)
        else:
            serializer = DiagnoseSerializer(data=dictionary)
    
        try:
            if serializer.is_valid():
                serializer.save()
    
            else:
                print ("error")
#    
        except Exception as e:
            print (e)    
