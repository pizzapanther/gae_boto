# GAE Boto

Even though Google has a lot of great services sometimes it is still necessary to use Amazon Web Services.  The official Amazon library for Python, Boto, does not work on Google App Engine.  GAE Boto attempts to implement the AWS API's in manner that will work in the Google App Engine environment.  Specifically, GAE Boto implements Amazon APIs with the AppEngine URL Fetch API.

Right now GAE Boto supports the following APIs:

* [SQS](http://aws.amazon.com/sqs/)

If you don't see the API you need, please contribute or ask nicely in the Issue Tracker :-)
