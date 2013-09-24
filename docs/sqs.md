# SQS: Simple Queue Service

* **[Product Page](http://aws.amazon.com/sqs/)**
* **[API Documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Welcome.html)**

## Actions

* [CreateQueue](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryCreateQueue.html)
  * Required:
      * QueueName
  * Optional:
      * DelaySeconds
      * MaximumMessageSize
      * MessageRetentionPeriod
      * Policy
      * ReceiveMessageWaitTimeSeconds
      * VisibilityTimeout
* [DeleteMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryDeleteMessage.html)
  * Required:
      * QueueName
      * ReceiptHandle
* [DeleteQueue](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryDeleteQueue.html)
  * Required:
      * QueueName
* [ReceiveMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryReceiveMessage.html)
  * Required:
      * QueueName
  * Optional:
      * AttributeName
      * MaxNumberOfMessages
      * VisibilityTimeout
      * WaitTimeSeconds
* [SendMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySendMessage.html)
  * Required:
      * MessageBody
      * QueueName
  * Optional:
      * DelaySeconds
* [SendMessageBatch](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySendMessageBatch.html)
  * Required:
      * QueueName
      * SendMessageBatchRequestEntry: List of Id, MessageBody, optional: (DelaySeconds)

