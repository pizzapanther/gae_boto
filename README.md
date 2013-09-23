# GAE Boto

Even though Google has a lot of great services sometimes it is still necessary to use Amazon Web Services.  The official Amazon library for Python, Boto, does not work on Google App Engine.  GAE Boto attempts to implement the AWS API's in manner that will work in the Google App Engine environment.  Specifically, GAE Boto implements Amazon APIs with the AppEngine URL Fetch API.

Right now GAE Boto supports the following APIs:

* [SQS](docs/sqs.md)

If you don't see the API you need, please contribute or ask nicely in the Issue Tracker :-)

**Example Usage:**

```
from gae_boto import AmazonConnection

connection = AmazonConnection('AWS_ID', 'AWS_KEY', 'ACCOUNT_NUMBER')
# Note: Account number is not always required for all API's

result = connection.sqs.CreateQueue(QueueName='Narf-Queue', DelaySeconds=50)

# Or run call asynchronously
rpc = connection.sqs.CreateQueue(async=True, QueueName='Narf-Queue', DelaySeconds=50)
result = rpc.get_result()

```

All calls to the API support the arguments **async=True|False** and **callback=a_callback_function**.  See [Asynchronous Requests](https://developers.google.com/appengine/docs/python/urlfetch/asynchronousrequests) for more info on how to handle asynchronous requests.

For individual parameters supported for each API see the links for each API above.  In general, we try to follow the same naming conventions used in the Amazon Docs for actions and input parameters.
