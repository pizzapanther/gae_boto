
import gae_boto.settings as settings

from .apis.sqs import SQS
from .apis.route53 import Route53

class AmazonConnection (object):
  def __init__ (self, aws_id, aws_key, aws_acct=None, region=None):
    self.aws_id = aws_id
    self.aws_key = aws_key
    self.aws_acct = aws_acct
    self.region = region
    
    if self.region is None:
      self.region = settings.DEFAULT_REGION
      
  @property
  def sqs (self):
    return self.build_api('sqs', SQS)
    
  @property
  def route53 (self):
    return self.build_api('route53', Route53)
    
  def build_api (self, api, api_class):
    attr = '_' + api
    if not hasattr(self, attr):
      setattr(self, attr, api_class(self))
      
    return getattr(self, attr)
    
    