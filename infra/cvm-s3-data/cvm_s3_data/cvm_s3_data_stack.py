from aws_cdk import Stack
import aws_cdk as cdk
import aws_cdk.aws_iam as iam
import aws_cdk.aws_lambda as aws_lambda
import aws_cdk.aws_s3 as s3
from constructs import Construct

"""

"""
class CvmS3DataStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    # Resources
    deployDataFilesAwsCliLayer69Dc861b = aws_lambda.CfnLayerVersion(self, 'DeployDataFilesAwsCliLayer69DC861B',
          content = {
            's3Bucket': 'cdk-hnb659fds-assets-818214664804-us-east-2',
            's3Key': 'd3adb8f8245549682ed42bc738adfed018ab3d9442ade840a7f42553830499d4.zip',
          },
          description = '/opt/awscli/aws',
        )

    deployWorkAreaAwsCliLayerD3186d17 = aws_lambda.CfnLayerVersion(self, 'DeployWorkAreaAwsCliLayerD3186D17',
          content = {
            's3Bucket': 'cdk-hnb659fds-assets-818214664804-us-east-2',
            's3Key': 'd3adb8f8245549682ed42bc738adfed018ab3d9442ade840a7f42553830499d4.zip',
          },
          description = '/opt/awscli/aws',
        )

    logRetentionaae0aa3c5b4d4f87b02d85b201efdd8aServiceRole9741Ecfb = iam.CfnRole(self, 'LogRetentionaae0aa3c5b4d4f87b02d85b201efdd8aServiceRole9741ECFB',
          assume_role_policy_document = {
            'Statement': [
              {
                'Action': 'sts:AssumeRole',
                'Effect': 'Allow',
                'Principal': {
                  'Service': 'lambda.amazonaws.com',
                },
              },
            ],
            'Version': '2012-10-17',
          },
          managed_policy_arns = [
            ''.join([
              'arn:',
              self.partition,
              ':iam::aws:policy/service-role/AWSLambdaBasicExecutionRole',
            ]),
          ],
          tags = [
            {
              'key': 'crescent:application:name',
              'value': 'crescent-data-deployment',
            },
          ],
        )

    crescentCvmDataBucket7Bfb4df0 = s3.CfnBucket(self, 'crescentCvmDataBucket7BFB4DF0',
          bucket_name = 'cvm-s3-data-crescent-us-east-2-aer1lu3eichu',
          lifecycle_configuration = {
            'rules': [
              {
                'expirationInDays': 1,
                'prefix': 'work_area/',
                'status': 'Enabled',
              },
            ],
          },
          public_access_block_configuration = {
            'blockPublicAcls': True,
            'blockPublicPolicy': True,
            'ignorePublicAcls': True,
            'restrictPublicBuckets': True,
          },
          tags = [
            {
              'key': 'crescent:application:name',
              'value': 'crescent-data-deployment',
            },
          ],
        )
    crescentCvmDataBucket7Bfb4df0.cfn_options.deletion_policy = cdk.CfnDeletionPolicy.RETAIN

    logRetentionaae0aa3c5b4d4f87b02d85b201efdd8aServiceRoleDefaultPolicyAdda7deb = iam.CfnPolicy(self, 'LogRetentionaae0aa3c5b4d4f87b02d85b201efdd8aServiceRoleDefaultPolicyADDA7DEB',
          policy_document = {
            'Statement': [
              {
                'Action': [
                  'logs:DeleteRetentionPolicy',
                  'logs:PutRetentionPolicy',
                ],
                'Effect': 'Allow',
                'Resource': '*',
              },
            ],
            'Version': '2012-10-17',
          },
          policy_name = 'LogRetentionaae0aa3c5b4d4f87b02d85b201efdd8aServiceRoleDefaultPolicyADDA7DEB',
          roles = [
            logRetentionaae0aa3c5b4d4f87b02d85b201efdd8aServiceRole9741Ecfb.ref,
          ],
        )

    logRetentionaae0aa3c5b4d4f87b02d85b201efdd8aFd4bfc8a = aws_lambda.CfnFunction(self, 'LogRetentionaae0aa3c5b4d4f87b02d85b201efdd8aFD4BFC8A',
          handler = 'index.handler',
          runtime = 'nodejs20.x',
          timeout = 900,
          code = {
            's3Bucket': 'cdk-hnb659fds-assets-818214664804-us-east-2',
            's3Key': '2819175352ad1ce0dae768e83fc328fb70fb5f10b4a8ff0ccbcb791f02b0716d.zip',
          },
          role = logRetentionaae0aa3c5b4d4f87b02d85b201efdd8aServiceRole9741Ecfb.attr_arn,
          tags = [
            {
              'key': 'crescent:application:name',
              'value': 'crescent-data-deployment',
            },
          ],
        )
    logRetentionaae0aa3c5b4d4f87b02d85b201efdd8aFd4bfc8a.add_dependency(logRetentionaae0aa3c5b4d4f87b02d85b201efdd8aServiceRoleDefaultPolicyAdda7deb)
    logRetentionaae0aa3c5b4d4f87b02d85b201efdd8aFd4bfc8a.add_dependency(logRetentionaae0aa3c5b4d4f87b02d85b201efdd8aServiceRole9741Ecfb)

    # Outputs
    """
      S3 bucket name for the us-east-2 region in 818214664804
    """
    self.bucket_name_output = crescentCvmDataBucket7Bfb4df0.ref
    cdk.CfnOutput(self, 'CfnOutputBucketNameOutput', 
      key = 'BucketNameOutput',
      description = 'S3 bucket name for the us-east-2 region in 818214664804',
      value = str(self.bucket_name_output),
    )



