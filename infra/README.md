## Workflow

The github workflow in `main.yml` assumes a [trunk-based development workflow](https://trunkbaseddevelopment.com/) where developers either push directly to the `main` branch or create PRs from short-lived feature branches that are merged into `main` (typically after code review).

Note that the github action for cloning the repo requires `lfs: true` to enable [large file support](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage) because some of the files imported into this repo are larger than GitHub's maximum file size.

Pushing to `main` or merging a PR to `main` will trigger a deploy of the Dev resources automatically.

The 'Deploy to Prod Environment' job is gated by a GitHub Environment `Production`. The GitHub repository settings for the Environment include the list of **Required reviewers** who are able to trigger the prod deployment job.

The CDK App uses a `--context` variable to set the deployment environment.  Dev and Prod resources are created in the same AWS account.  Dev resources will be created with a `dev-` prefix.

### How to Deploy to Prod

The workflow will pause for approval after a successful Dev deployment and before 'Deploy to Prod Environmnet' can run.

After a Reviewer approves the pending deployment, the 'Deploy to Prod Environment' job will run which deploys to production the infrastructure and the version of software that was previously built in this workflow run.
