from pathlib import Path

import aws_cdk as cdk
from aws_cdk import CfnOutput, Duration, RemovalPolicy, Size, Tags
import aws_cdk.aws_logs as logs
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_s3_deployment as s3deploy
from constructs import Construct
from lib.deployment_environment_config import DeploymentEnvironmentConfig



class CvmS3DataStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, *, config: DeploymentEnvironmentConfig, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        Tags.of(self).add("crescent:application:name", "CVM-S3-DATA")

        project_root = Path(__file__).resolve().parents[3]
        data_dir = project_root / "data"
        work_area_dir = project_root / "work_area"

        bucket = s3.Bucket(
            self,
            "CvmDataBucket",
            bucket_name=config.bucket_name,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.RETAIN,
            auto_delete_objects=False,
            lifecycle_rules=[
                s3.LifecycleRule(
                    enabled=True,
                    expiration=Duration.days(1),
                    prefix="work_area/",
                )
            ],
        )

        s3deploy.BucketDeployment(
            self,
            "DeployDataFiles",
            sources=[s3deploy.Source.asset(str(data_dir))],
            destination_bucket=bucket,
            destination_key_prefix="data/",
            extract=True,
            retain_on_delete=False,
            memory_limit=2048,
            ephemeral_storage_size=Size.gibibytes(2),
            log_retention=logs.RetentionDays.FIVE_DAYS,
        )

        s3deploy.BucketDeployment(
            self,
            "DeployWorkArea",
            sources=[s3deploy.Source.asset(str(work_area_dir))],
            destination_bucket=bucket,
            destination_key_prefix="work_area/",
            extract=True,
            retain_on_delete=False,
            memory_limit=512,
            ephemeral_storage_size=Size.gibibytes(2),
        )

        CfnOutput(
            self,
            "BucketNameOutput",
            value=bucket.bucket_name,
            description=f"S3 bucket name for the {self.region} region in {self.account}",
        )
