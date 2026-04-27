import aws_cdk as core
import aws_cdk.assertions as assertions

from cvm_s3_data.cvm_s3_data_stack import CvmS3DataStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cvm_s3_data/cvm_s3_data_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CvmS3DataStack(app, "cvm-s3-data")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
