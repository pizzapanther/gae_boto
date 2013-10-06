#!/usr/bin/env python

import os
import sys

sys.path.insert(0, '..')

from gae_boto import AmazonConnection
from gae_boto.fields import ListofDicts

APIS = ('sqs', 'route53')

def write_field (attr, field, fh):
  if isinstance(field, ListofDicts):
    items = ', '.join(sorted(field.required.keys()))
    if field.optional.keys():
      items += ', optional: ('
      items += ', '.join(sorted(field.optional.keys()))
      items += ')'
      
    fh.write('      * %s: List of %s\n' % (attr, items))
    
  else:
    fh.write('      * %s\n' % attr)
    
def generate ():
  base_path = os.path.normpath(os.path.dirname(__file__))
  doc_path = os.path.join(base_path, 'docs')
  
  conn = AmazonConnection('DOCS', 'DUMMEYKEY')
  
  for key in APIS:
    api = getattr(conn, key)
    
    file_path = os.path.join(doc_path, key + '.md')
    fh = open(file_path, 'w')
    fh.write('# %s\n\n' % api.title)
    
    fh.write('* **[Product Page](%s)**\n' % api.product_url)
    fh.write('* **[API Documentation](%s)**\n\n' % api.doc_url)
    
    fh.write('## Actions\n\n')
    
    for method in sorted(api.methods.keys()):
      config = api.methods[method]
      url = api.method_url % method
      fh.write('* [%s](%s)\n' % (method, url))
      
      if config['required'] and config['required'].keys():
        fh.write('  * Required:\n')
        for attr in sorted(config['required'].keys()):
          field = config['required'][attr]
          write_field (attr, config['required'][attr], fh)
          
      if config['optional'] and config['optional'].keys():
        fh.write('  * Optional:\n')
        for attr in sorted(config['optional'].keys()):
          write_field(attr, config['optional'][attr], fh)
          
    fh.write('\n')
    fh.close()
    
    
if __name__ == '__main__':
  generate()
  