from google.appengine.api import urlfetch

import gae_boto.fields as fields
from .core import AwsApi

QueueName = fields.Slug(max_length=80, min_length=1, url_param=True)
SQS_PATH = '/%(aws_acct)s/%(QueueName)s/'

class SQS (AwsApi):
  parameters = {
    'Version': '2012-11-05'
  }
  
  host = 'sqs'
  method = 'GET'
  
  methods = {
    'CreateQueue': {
      'path': '/',
      
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
    },
    
    'SendMessage': {
      'path': SQS_PATH,
      
      'required': {
        'QueueName': QueueName,
        'MessageBody': fields.String(max_length=262144, min_length=1),
      },
      
      'optional': {
        'DelaySeconds': fields.Integer(max_value=900, min_value=0),
      }
    },
    
    'DeleteQueue': {
      'path': SQS_PATH,
      
      'required': {
        'QueueName': QueueName,
      },
      
      'optional': {}
    },
    
    'SendMessageBatch': {
      'path': SQS_PATH,
      
      'required': {
        'QueueName': QueueName,
        'SendMessageBatchRequestEntry': fields.ListofDicts(
          required={
            'Id': fields.String(min_length=1),
            'MessageBody': fields.String(max_length=262144, min_length=1)},
          optional={'DelaySeconds': fields.Integer(max_value=900, min_value=0)}
        ),
      },
      
      'optional': {}
    },
  }
  