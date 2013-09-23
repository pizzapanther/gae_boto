import re

COUNTER = 'counter'

class Field (object):
  def __init__ (self, field_type=None, url_param=False):
    self.field_type = field_type
    self.url_param = url_param
    
  def validate (self, value):
    raise NotImplementedError
    
  def stringify (self, value):
    raise NotImplementedError
    
  def set_attr (self, form_data, name, value, counter):
    if self.field_type == COUNTER:
      form_data['Attribute.%d.Name' % counter] = name
      form_data['Attribute.%d.Value' % counter] = self.stringify(value)
      counter += 1
      
    else:
      form_data[name] = self.stringify(value)
      
    return counter
    
class String (Field):
  def __init__ (self, field_type=None, url_param=False, max_length=None, min_length=None):
    self.max_length = max_length
    self.min_length = min_length
    super(String, self).__init__(field_type=field_type, url_param=url_param)
    
  def validate (self, value):
    if self.max_length and len(value) > self.max_length:
      raise Exception('Exceeds Max Length: %d' % self.max_length)
      
    if self.min_length and len(value) < self.min_length:
      raise Exception('Exceeds Min Length: %d' % self.min_length)
      
  def stringify (self, value):
    return value
    
class Slug (String):
  regex = re.compile('^[-\w]+$')
  
  def validate (self, value):
    if self.regex.match(value) is None:
      raise Exception('Must contain alphanumeric, hyphens, or underscore characters only.')
      
    super(Slug, self).validate(value)
    
class Integer (Field):
  def __init__ (self, field_type=None, url_param=False, max_value=None, min_value=None):
    self.max_value = max_value
    self.min_value = min_value
    super(Integer, self).__init__(field_type=field_type, url_param=url_param)
    
  def validate (self, value):
    if self.max_value and value > self.max_value:
      raise Exception('Exceeds Max Value: %d' % self.max_value)
      
    if self.min_value and value < self.min_value:
      raise Exception('Exceeds Min Value: %d' % self.min_value)
      
  def stringify (self, value):
    return str(value)
    