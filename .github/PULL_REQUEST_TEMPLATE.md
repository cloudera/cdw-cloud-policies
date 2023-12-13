(Add description here)

---
# Pull Request checklist:

### Description:
- [ ] Description of the change is added
- [ ] Jira ID is added to the title

**Changes to any files in generated folder(not to be touched)**
- [ ] No
- [ ] Yes

**Is the DWX JIRA PR using a new AWS SDK API which needs new permission(s), not included in either of the files under
https://github.com/cloudera/cdw-cloud-policies/tree/main/aws-iam-policies/docs then create a PR to include the new action**

- [ ] Include in [Reduced mode cross account Policy](./aws-iam-policies/reduced-permissions-mode.json)
- [ ] Include in [Restricted cross account Policy](./aws-iam-policies/docs)

**Is the dwx-cf-template.yaml being modified, that is specifically any new resources are added or if new permissions/actions are needed.**

- [ ] Include in [Restricted cross account Policy](./aws-iam-policies/docs)

**Are new permissions added in the policies section of "NodeInstanceRole" section of dwx-cf-template.yaml**

- [ ] Include in [Managed Policy Inline Node Role Policy](./aws-iam-policies/managedArn-node-inline-policy.json)

**Is this a bug fix for an old release, with missing permission, example [DWX-15473](https://jira.cloudera.com/browse/DWX-15473)**

- [ ] Create a TSB about the missing permission


**Backward compatibility**

- [ ] No breaking changes for upgrades
- [ ] Yes, then create a TSB, 

### Testing:
  - [ ] Manual tests (**add details**)
  - [ ] Control Plane integrated
  - [ ] mow-priv
