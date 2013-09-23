# SQS: Simple Queue Service

* **[Product Page](http://aws.amazon.com/sqs/)**
* **[API Documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Welcome.html)**

## Actions

* [CreateQueue](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryCreateQueue.html)
  * Required Parameters:
      * QueueName
  * Optional Parameters:
      * DelaySeconds
      * MaximumMessageSize
      * MessageRetentionPeriod
      * Policy
      * ReceiveMessageWaitTimeSeconds
      * VisibilityTimeout
* [SendMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySendMessage.html)
  * Required Parameters:
      * QueueName
      * MessageBody
  * Optional Parameters:
      * DelaySeconds
* [SendMessageBatch](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySendMessageBatch.html)
  * Required Parameters:
      * QueueName
      * SendMessageBatchRequestEntry: List of Id, MessageBody, DelaySeconds(optional)