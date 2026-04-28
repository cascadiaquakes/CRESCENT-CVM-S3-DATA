# CRESCENT CVM S3 Data (infra/new)

This CDK app deploys the CVM S3 data bucket and uploads the data and work area prefixes.
It is a Python CDK app that uses only standard AWS CDK libraries.

## Context

The `deployment-environment` context value controls whether the app deploys the dev or prod bucket.

Example:

- dev: `cdk synth --context deployment-environment=dev`
- prod: `cdk synth --context deployment-environment=prod`

## Hard-coded AWS Account/Region

The app is configured to deploy to:

- Account: `818214664804`
- Region: `us-east-2`

## Bucket Names

- dev: `cvm-s3-data-latest-dev-us-east-2-aer1lu3eichu`
- prod: `cvm-s3-data-crescent-us-east-2-aer1lu3eichu`

## Tags

Only the following tag is applied:

- `crescent:application:name` = `CVM-S3-DATA`
