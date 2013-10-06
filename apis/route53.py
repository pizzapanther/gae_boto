import gae_boto.fields as fields

from .core import AwsApi
from .templates.route53 import ChangeResourceRecordSetsTemplate

ROUTE_PATH = '/%(Version)s/hostedzone/%(HostedZoneId)s/rrset'

HostedZoneId = fields.String(url_param=True)

class Route53 (AwsApi):
  title = 'Route53: Highly available and scalable DNS Service'
  product_url = 'http://aws.amazon.com/route53/'
  doc_url = 'http://docs.aws.amazon.com/Route53/latest/APIReference/Welcome.html'
  method_url = 'http://docs.aws.amazon.com/Route53/latest/APIReference/API_%s.html'
  
  host = 'route53'
  method = 'POST'
  no_region = True
  
  parameters = {
    'Version': '2012-12-12'
  }
  
  methods = {
    'ChangeResourceRecordSets': {
      'path': ROUTE_PATH,
      'template': ChangeResourceRecordSetsTemplate,
      
      'required': {
        'HostedZoneId': HostedZoneId,
        'Action': fields.String(values=('CREATE', 'DELETE')),
        'Name': fields.String(),
        'Type': fields.String(values=('A', 'AAAA', 'CNAME', 'MX', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT')),
        'TTL': fields.Integer(),
        'Value': fields.String(),
      },
      
      'optional': {}
    }
  }
  