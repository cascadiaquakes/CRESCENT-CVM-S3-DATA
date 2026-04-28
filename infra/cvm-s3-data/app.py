#!/usr/bin/env python3
import aws_cdk as cdk

from cvm_s3_data.cvm_s3_data_stack import CvmS3DataStack


from lib.deployment_environment_config import DeploymentEnvironmentConfig
AWS_ACCOUNT_ID = '818214664804'
AWS_REGION = 'us-east-2'

# Define configuration based on the deployment environment.
# NOTE: The `deployment-environment` MUST be provided at runtime via CDK context.
# Example: `cdk synth --context deployment-environment=dev`
deployment_environments_configs: dict[str, DeploymentEnvironmentConfig] = {
    "dev": DeploymentEnvironmentConfig(
        bucket_name="cvm-s3-data-latest-dev-us-east-2-aer1lu3eichu"
    ),
    "prod": DeploymentEnvironmentConfig(
        bucket_name="cvm-s3-data-crescent-us-east-2-aer1lu3eichu"
    ),
}

#PROD_BUCKET_NAME = "cvm-s3-data-crescent-us-east-2-aer1lu3eichu"
#DEV_BUCKET_NAME = "cvm-s3-data-latest-dev-us-east-2-aer1lu3eichu"

app = cdk.App()

deployment_environment = app.node.try_get_context("deployment-environment")
if not deployment_environment:
    raise SystemExit(
        "Error: deployment-environment context variable not set. "
        "Use '--context deployment-environment=<dev|prod>' to set it."
    )

if deployment_environment not in {"dev", "prod"}:
    raise SystemExit(
        "Error: deployment-environment context must be one of 'dev' or 'prod'."
    )

env_config = deployment_environments_configs.get(deployment_environment)

if not env_config:
    raise SystemExit(
        f"Error: No configuration found for deployment environment '{deployment_environment}'."
    )

# CDK uses the stack name as the prefix for nearly all resources created.
# Create a prefix for non-Prod Stacks to avoid naming conflicts between environments.
resource_prefix=f"{deployment_environment}-" if deployment_environment != "prod" else ""


CvmS3DataStack(
    app,
    f"{resource_prefix}cvm-s3-data",
    env=cdk.Environment(account=AWS_ACCOUNT_ID, region=AWS_REGION),
    config=env_config,
)

app.synth()
