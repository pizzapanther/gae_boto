import hmac
import hashlib
import base64
import urllib
import time
import datetime

class S3Key (object):
  def __init__ (self, bucket, key, connection=None):
    self.bucket = bucket
    self.key = key
    self.connection = connection
    
  def url (self, https=False, sign=False, expires=0, method='GET'):
    http = 'http'
    if https:
      http = 'https'
      
    url = u'{http}://{bucket}.s3.amazonaws.com/{key}'.format(http=http, bucket=self.bucket, key=self.key)
    
    if sign:
      now = datetime.datetime.utcnow()
      expire = int(time.mktime(now.utctimetuple())) + expires
      sign_me = u"{method}\n\n\n{expire}\n/{bucket}/{key}".format(method=method, bucket=self.bucket, key=self.key, expire=expire)
      h = hmac.new(key=self.connection.aws_key, msg=sign_me, digestmod=hashlib.sha1)
      signature = base64.b64encode(h.digest()).decode()
      
      url += u"?AWSAccessKeyId={aws_id}&Expires={expire}&Signature={signature}".format(
        aws_id=urllib.quote(self.connection.aws_id),
        expire=expire,
        signature=urllib.quote(signature),
      )
      
    return url
    