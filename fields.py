import re
import types

COUNTER = 'counter'
MULTI = 'multi'

class Field (object):
  def __init__ (self, field_type=None, url_param=False, values=[]):
    self.field_type = field_type
    self.url_param = url_param
    self.values = values
    
  def validate (self, value):
    raise NotImplementedError
    
  def stringify (self, value):
    raise NotImplementedError
    
  def set_attr (self, form_data, name, value, counter):
    if self.field_type == COUNTER:
      form_data['Attribute.%d.Name' % counter] = name
      form_data['Attribute.%d.Value' % counter] = self.stringify(value)
      counter += 1
      
    if self.field_type == MULTI:
      my_counter = 1
      if self.is_list(value):
        for v in value:
          form_data['%s.%d' % (name, my_counter)] = self.stringify(v)
          my_counter +=1
          
      else:
        form_data[name] = self.stringify(value)
        
    else:
      form_data[name] = self.stringify(value)
      
    return counter
    
  def is_list (self, value):
    return type(value) is types.ListType or type(value) is types.TupleType
    
  def valdidate_values (self, value):
    if self.values:
      if self.field_type == MULTI and self.is_list(value):
        for v in value:
          if v not in self.values:
            raise Exception('Not a valid value, must be: %s' % str(self.values))
            
      else:
        if value not in self.values:
          raise Exception('Not a valid value, must be: %s' % str(self.values))
          
class String (Field):
  def __init__ (self, field_type=None, url_param=False, values=[], max_length=None, min_length=None):
    self.max_length = max_length
    self.min_length = min_length
    super(String, self).__init__(field_type=field_type, url_param=url_param, values=values)
    
  def validate (self, value):
    self.valdidate_values(value)
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
  def __init__ (self, field_type=None, url_param=False, values=[], max_value=None, min_value=None):
    self.max_value = max_value
    self.min_value = min_value
    super(Integer, self).__init__(field_type=field_type, url_param=url_param, values=values)
    
  def validate (self, value):
    self.valdidate_values(value)
    if self.max_value and value > self.max_value:
      raise Exception('Exceeds Max Value: %d' % self.max_value)
      
    if self.min_value and value < self.min_value:
      raise Exception('Exceeds Min Value: %d' % self.min_value)
      
  def stringify (self, value):
    return str(value)
    
class ListofDicts (Field):
  def __init__ (self, required={}, optional={}):
    self.required = required
    self.optional = optional
    self.field_type = None
    self.url_param = False
    
  def validate (self, values_list):
    for dict_values in values_list:
      for key, field in self.required.items():
        if key in dict_values:
          field.validate(dict_values[key])
          
        else:
          raise Exception('%s is a required argument' % key)
          
      for key, field in self.optional.items():
        if key in dict_values:
          field.validate(dict_values[key])
          
  def set_attr (self, form_data, name, values_list, counter):
    my_counter = 1
    for dict_values in values_list:
      for key, field in self.required.items():
        my_name = '%s.%s.%s' % (name, str(my_counter), key)
        form_data[my_name] = field.stringify(dict_values[key])
        
      for key, field in self.optional.items():
        if key in dict_values:
          my_name = '%s.%s.%s' % (name, str(my_counter), key)
          form_data[my_name] = field.stringify(dict_values[key])
          
      my_counter += 1
      
    return counter
    