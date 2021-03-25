import json
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        from django.conf import settings
        import sys
        from barman.models import Diagnose
        from barman.serializers import DiagnoseSerializer
   
        import subprocess
        process = subprocess.Popen(['barman', 'diagnose'],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        data = (json.loads(stdout))
        
        try:
            item = Diagnose.objects.get(name='config')
        except Diagnose.DoesNotExist:
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
