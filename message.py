#Send SMS using PYTHON
from subprocess import *

try:
    import urllib # Python URL functions
    import urllib2

    authkey = "221378ArPexh2OaX5b29a485" # Your authentication key.

    with open('message.txt', 'r') as f:
        lines = f.read().splijuggutlines()
        last_line = lines[-1]

    mobiles = last_line # Multiple mobiles numbers separated by comma.

    message = "Test message" # Your message to send.

    sender = "112233" # Sender ID,While using route4 sender id should be 6 characters long.

    route = "default" # Define route

    # Prepare you post parameters
    values = {
              'authkey' : authkey,
              'mobiles' : mobiles,
              'message' : message,
              'sender' : sender,
              'route' : route
              }

    url = "https://control.msg91.com/api/sendhttp.php" # API URL

    postdata = urllib.urlencode(values) # URL encoding the data here.

    req = urllib2.Request(url, postdata)

    response = urllib2.urlopen(req)

    output = response.read() # Get Response

    print(output) # Print Response
    print(mobiles)
except:
    print("Message Error")

call('python3 login.py',shell=True)