# GAE Boto

Even though Google has a lot of great services sometimes it is still necessary to use Amazon Web Services.  The official Amazon library for Python, Boto, does not work on Google App Engine.  GAE Boto attempts to implement the AWS API's in manner that will work in the Google App Engine environment.  Specifically, GAE Boto implements Amazon APIs with the AppEngine URL Fetch API.

Right now GAE Boto supports the following APIs:

* [SQS](docs/sqs.md)

If you don't see the API you need, please contribute or ask nicely in the Issue Tracker :-)

**Example Usage:**

```python
from gae_boto import AmazonConnection

connection = AmazonConnection('AWS_ID', 'AWS_KEY', 'AWS_ACCOUNT_NUMBER')
# Note: Account number is not always required for all API's

result = connection.sqs.CreateQueue(QueueName='Narf-Queue', DelaySeconds=50)

# Or run call asynchronously
rpc = connection.sqs.CreateQueue(async=True, QueueName='Narf-Queue', DelaySeconds=50)
result = rpc.get_result()

# Send a message to the Queue
result = connection.sqs.SendMessage(QueueName='Narf-Queue', MessageBody='I like turtles')

# Send a batch of messages
MessageBatch = [
  {'Id': 'msg1', 'MessageBody': 'NARF 1'},
  {'Id': 'msg2', 'MessageBody': 'NARF 2'},
]
result = connection.sqs.SendMessageBatch(QueueName='Narf-Queue', SendMessageBatchRequestEntry=MessageBatch)

# Parse XML into an object
xml_obj = result.xml_object()
message_text = xml_obj.ReceiveMessageResult.Message.Body.text
request_id =  xml_obj.ResponseMetadata.RequestId.text
```

All calls to the API support the arguments **async=True|False** and **callback=a_callback_function**.  See [Asynchronous Requests](https://developers.google.com/appengine/docs/python/urlfetch/asynchronousrequests) for more info on how to handle asynchronous requests.

For individual parameters supported for each API see the links for each API above.  In general, we try to follow the same naming conventions used in the Amazon Docs for actions and input parameters.

## Installation

To install, simply add the gae_boto directory to the root of your App Engine app. You can do this several ways.

* Download and unzip https://github.com/pizzapanther/gae_boto/archive/master.zip and rename directory to gae_boto
* Checkout the code: `git clone git@github.com:pizzapanther/gae_boto.git`
* If you're using Git, checkout as a submodule: `git submodule add git@github.com:pizzapanther/gae_boto.git gae_boto`

If you plan to parse your result XML make sure LXML is added to your libraries section of your app.yaml.  Synchronous results will have a method called _xml_object_ added to them to parse the XML into a Python object.
