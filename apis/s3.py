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
    
  def url (self, https=False, sign=False, expires=0):
    http = 'http'
    if https:
      http = 'https'
      
    url = '{http}://{bucket}.s3.amazonaws.com/{key}'.format(http=http, bucket=self.bucket, key=self.key)
    
    if sign:
      now = datetime.datetime.utcnow()
      expire = int(time.mktime(now.utctimetuple())) + expires
      sign_me = "GET\n\n\n{expire}\n/{bucket}/{key}".format(bucket=self.bucket, key=self.key, expire=expire)
      h = hmac.new(key=self.connection.aws_key, msg=sign_me, digestmod=hashlib.sha1)
      signature = base64.b64encode(h.digest()).decode()
      
      url += "?AWSAccessKeyId={aws_id}&Expires={expire}&Signature={signature}".format(
        aws_id=urllib.quote(self.connection.aws_id),
        expire=expire,
        signature=urllib.quote(signature),
      )
      
    return url
    