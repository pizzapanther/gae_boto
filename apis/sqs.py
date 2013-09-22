from google.appengine.api import urlfetch

import gae_boto.fields as fields
from .core import AwsApi

class SQS (AwsApi):
  parameters = {
    'Version': '2012-11-05'
  }
  
  host = 'sqs'
  method = 'GET'
  
  methods = {
    'CreateQueue': {
      'required': {
        'QueueName': fields.Slug(max_length=80, min_length=1)
      },
      
      'optional': {
        'DelaySeconds': fields.Integer(max_value=900, min_value=0, field_type=fields.COUNTER),
        'MaximumMessageSize': fields.Integer(max_value=262144, min_value=1024, field_type=fields.COUNTER),
        'MessageRetentionPeriod': fields.Integer(max_value=1209600, min_value=60, field_type=fields.COUNTER),
        'Policy': fields.String(),
        'ReceiveMessageWaitTimeSeconds': fields.Integer(max_value=20, min_value=0, field_type=fields.COUNTER),
        'VisibilityTimeout': fields.Integer(max_value=43200, min_value=0, field_type=fields.COUNTER)
      }
    }
  }
  