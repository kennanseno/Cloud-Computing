# This script created a queue
#
# Author - Paul Doyle  Nov 2015
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2
import pprint

# Get the keys from a specific url and then use them to connect to AWS Service

response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')

html=response.read()

result = html.split(':')

#print (result[0])
#print (result[1])

access_key_id = result[0]
secret_access_key = result[1]

#print (access_key_id,secret_access_key)
# Set up a connection to the AWS service.
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

student_number = 'D14123582_'
#conn.delete_queue(sys.argv[1])

# Get a list of the queues that exists and then print the list out
rs = conn.get_all_queues()
#Delete
queue = conn.get_queue(student_number+sys.argv[1])
conn.delete_queue(queue)
print "Queue deleted " + sys.argv[1]


		

