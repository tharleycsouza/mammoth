import subprocess
import json
process = subprocess.Popen(['barman', 'diagnose'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
print (json.loads(stdout))
