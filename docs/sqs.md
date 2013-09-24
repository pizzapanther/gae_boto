# SQS: Simple Queue Service

* **[Product Page](http://aws.amazon.com/sqs/)**
* **[API Documentation](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Welcome.html)**

## Actions

* [AddPermission](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryAddPermission.html)
  * Required:
      * AWSAccountId
      * ActionName
      * Label
      * QueueName
* [ChangeMessageVisibility](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryChangeMessageVisibility.html)
  * Required:
      * QueueName
      * ReceiptHandle
      * VisibilityTimeout
* [ChangeMessageVisibilityBatch](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryChangeMessageVisibilityBatch.html)
  * Required:
      * ChangeMessageVisibilityBatchRequestEntry: List of Id, ReceiptHandle, VisibilityTimeout
      * QueueName
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
* [DeleteMessageBatch](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryDeleteMessageBatch.html)
  * Required:
      * DeleteMessageBatchRequestEntry: List of Id, ReceiptHandle
      * QueueName
* [DeleteQueue](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryDeleteQueue.html)
  * Required:
      * QueueName
* [GetQueueAttributes](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryGetQueueAttributes.html)
  * Required:
      * AttributeName
      * QueueName
* [GetQueueUrl](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryGetQueueUrl.html)
  * Required:
      * QueueName
  * Optional:
      * QueueOwnerAWSAccountId
* [ListQueues](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryListQueues.html)
  * Optional:
      * QueueNamePrefix
* [ReceiveMessage](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryReceiveMessage.html)
  * Required:
      * QueueName
  * Optional:
      * AttributeName
      * MaxNumberOfMessages
      * VisibilityTimeout
      * WaitTimeSeconds
* [RemovePermission](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QueryRemovePermission.html)
  * Required:
      * Label
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
* [SetQueueAttributes](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Query_QuerySetQueueAttributes.html)
  * Required:
      * Attribute.Name
      * Attribute.Value

