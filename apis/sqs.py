import gae_boto.fields as fields
from .core import AwsApi

QueueName = fields.Slug(max_length=80, min_length=1, url_param=True)

MessageAttrs = ('All', 'SenderId', 'SentTimestamp', 'ApproximateReceiveCount', 'ApproximateFirstReceiveTimestamp')

SQS_PATH = '/%(aws_acct)s/%(QueueName)s/'

class SQS (AwsApi):
  title = 'SQS: Simple Queue Service'
  product_url = 'http://aws.amazon.com/sqs/'
  doc_url = 'http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Welcome.html'
  method_url = 'http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_Query%s.html'
  
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
    
    'DeleteMessage': {
      'path': SQS_PATH,
      
      'required': {
        'QueueName': QueueName,
        'ReceiptHandle': fields.String(min_length=1),
      },
      
      'optional': {}
    },
    
    'ReceiveMessage': {
      'path': SQS_PATH,
      
      'required': {
        'QueueName': QueueName,
      },
      
      'optional': {
        'AttributeName': fields.String(values=MessageAttrs, field_type=fields.MULTI),
        'MaxNumberOfMessages': fields.Integer(max_value=10, min_value=1),
        'VisibilityTimeout': fields.Integer(max_value=43200, min_value=0),
        'WaitTimeSeconds': fields.Integer(max_value=20, min_value=0),
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
  