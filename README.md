# cdw-cloud-policies

# AWS IAM Policies

### Restricted policy:

Since AWS has a character limit on the policies, the cross-account policy is split into 2.

- [Restricted Policy cross account file 1](./aws-iam-policies/generated/restricted-policy-1.json5).
- [Restricted Policy cross account file 2](./aws-iam-policies/generated/restricted-policy-2.json5).

To understand why CDW needs each permission see,

- [Restricted Policy file 1 with comments](./aws-iam-policies/docs/restricted-policy-doc-1.json5).
- [Restricted Policy file 2 with comments](./aws-iam-policies/docs/restricted-policy-doc-2.json5).


### Reduced permissions mode Policy:

- [Reduced mode cross account Policy](./aws-iam-policies/reduced-permissions-mode.json)


### Restricted Policy with Managed Policy ARN:

- [Restricted Policy cross account with Managed Policy ARN file 1](./aws-iam-policies/generated/restricted-policy-managedARN-1.json5).
- [Restricted Policy cross account with Managed Policy ARN file 2](./aws-iam-policies/generated/restricted-policy-managedARN-2.json5).

### Inline Node Role Policy:

- [Managed Policy Inline Node Role Policy](./aws-iam-policies/managedArn-node-inline-policy.json)


### Releases:

- Current release docs can be found at, https://github.com/cloudera/cdw-cloud-policies/blob/latest-release
- Older release docs can be found by their branch name
- Ongoing release commits will be made on **main** branch

### Development:

- Policies under generated folder are generated & committed via the github workflow. There should be no manual changes to them.
- Any changes to restricted policy,should be done in [docs](./aws-iam-policies/docs) folder
- The restricted policy w/o comments and restricted policy for managed policy ARN will be auto generated.

#### Guidelines:

Understand how conditions work, https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html. 

- If the action is a **create** resource with Request Tag passed, and
  - If the resource is created via running CloudFormation template, add the action in  Sid **CFRequestTag**
  - Else Add the action in Sid - **RequestTag**
- If the action is on an already existing resource which has a Resource Tag, and
  - If the action is called in the CloudFormation template, Then add the action in Sid - **CFResourceTag**
  - Else Add the action in Sid - **ResourceTag**
- If the action is called from our DWX Server go code via AWS SDK API
  - Add it in Sid gocode* as applicable



#### Create a new release and tagging:

##### Create a new release when CDW branch is cut for QE to test

```bash
$ git checkout -b R39 origin/main // Cut a new branch say R39
$ git push origin HEAD // push the branch to remote
```

##### Once in Prod update the tags

Since the docs need to use static links for referencing the policies, we need to always maintain the tag "latest-release" pointing to the current 
release. Steps to take care for once a new release branch is cut. Once the release is out, update the tags

```bash
$ git tag -d latest-release // Remove the old tag
$ git push origin :refs/tags/latest-release // push the deleted tag to remote
$ git tag latest-release // tag new release with latest-release
$ git push --tags // push the tag to remote
$ git push origin HEAD // push the branch to remote
```
