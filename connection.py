
import gae_boto.settings as settings

from .apis.sqs import SQS

class AmazonConnection (object):
  def __init__ (self, aws_id, aws_key, aws_acct=None, region=None):
    self.aws_id = aws_id
    self.aws_key = aws_key
    self.aws_acct = aws_acct
    self.region = region
    
    if self.region is None:
      self.region = settings.DEFAULT_REGION
      
    self.api_classes = {
      'sqs': SQS
    }
    
  @property
  def sqs (self):
    return self.build_api('sqs')
    
  def build_api (self, api):
    attr = '_' + api
    if not hasattr(self, attr):
      setattr(self, attr, SQS(self))
      
    return getattr(self, attr)
    
    