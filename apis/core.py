import hmac
import base64
import urllib
import hashlib
import datetime

from google.appengine.api import urlfetch

class MethodProxy (object):
  def __init__ (self, api, action_name, config):
    self.api = api
    self.action_name = action_name
    self.config = config
    
  def run_action (self, **kwargs):
    return self.api.action(self.action_name, self.config, **kwargs)
    
class AwsApi (object):
  methods = {}
  parameters = {}
  
  def __init__ (self, connection):
    self.connection = connection
    
    self.generate_methods()
    
  def generate_methods (self):
    for method, config in self.methods.items():
      mp = MethodProxy(self, method, config)
      setattr(self, method, mp.run_action)
      
  def signature (self, value):
    h = hmac.new(key=str(self.connection.aws_key), msg=value, digestmod=hashlib.sha256)
    return base64.b64encode(h.digest()).decode()
    
  def action (self, action_name, config, **kwargs):
    async = False
    if 'async' in kwargs:
      async = kwargs['async']
      del kwargs['async']
      
    callback = None
    if 'callback' in kwargs:
      callback = kwargs['callback']
      del kwargs['callback']
      
    form_data = {'Action': action_name}
    method = self.method
    path = '/'
    host = '%s.%s.amazonaws.com' % (self.host, self.connection.region)
    url = 'https://' + host + path
    counter = 1
    
    if config.has_key('method'):
      method = config['method']
      
    for key, value in self.parameters.items():
      form_data[key] = value
      
    for key, field in config['required'].items():
      if key in kwargs:
        field.validate(kwargs[key])
        counter = field.set_attr(form_data, key, kwargs[key], counter)
        del kwargs[key]
        
      else:
        raise Exception('%s is a required argument' % key)
        
    for key, field in config['optional'].items():
      if key in kwargs:
        field.validate(kwargs[key])
        counter = field.set_attr(form_data, key, kwargs[key], counter)
        del kwargs[key]
        
    if len(kwargs.keys()) > 0:
      keywords = ", ".join(kwargs.keys())
      raise Exception('Unknown API Parameters: %s' % keywords)
      
    d = datetime.datetime.utcnow()
    
    if method in ('POST', 'PUT', 'PATCH'):
      dateValue = d.strftime('%a, %d %b %Y %H:%M:%S GMT')
      form_data = urllib.urlencode(form_data)
      headers = {'Content-Type': 'application/x-www-form-urlencoded'}
      headers['Date'] = dateValue
      headers['X-Amzn-Authorization'] = \
      'AWS3-HTTPS AWSAccessKeyId=%s, Algorithm=HMACSHA256, Signature=%s' % (self.connection.aws_id, 
        self.signature(dateValue))
        
      url_kwargs = dict(url=url, payload=form_data, method=getattr(urlfetch, method), headers=headers)
      
    else:
      d = d + datetime.timedelta(seconds=60)
      dateValue = d.strftime('%Y-%m-%dT%H:%M:%SZ')
      form_data['SignatureVersion'] = '2'
      form_data['SignatureMethod'] = 'HmacSHA256'
      form_data['AWSAccessKeyId'] = self.connection.aws_id
      form_data['Expires'] = dateValue
      
      params = [(key, form_data[key]) for key in sorted(form_data.keys())]
      form_data = urllib.urlencode(params)
      
      url += '?' + form_data
      url += '&Signature=' + urllib.quote(self.signature("\n".join([method, host, path, form_data])))
      
      url_kwargs = dict(url=url, method=getattr(urlfetch, method))
      
    return self.fetch(async, callback, **url_kwargs)
    
  def fetch (self, async, callback, **kwargs):
    if async:
      rpc = urlfetch.create_rpc()
      if callback:
        rpc.callback = lambda: callback(rpc)
        
      return urlfetch.make_fetch_call(rpc, **kwargs)
      
    return urlfetch.fetch(**kwargs)
    