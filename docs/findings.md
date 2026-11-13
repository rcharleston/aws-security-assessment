# Findings and residual risk

The source fixture represents a fictional SaaS environment. The original experiment assessed five themes; the table separates the historical change from what can responsibly be concluded.

| Area | Condition in the fixture | Historical action | Evidence interpretation / remaining work |
|---|---|---|---|
| S3 frontend | All four Block Public Access protections disabled | Enabled bucket-level protections | Disabled protections are a risk condition; effective public access also depends on policies and ACLs. Verify bucket policy, ACLs, and account-level settings. |
| S3 uploads | No explicit encryption resource in Terraform | Observed a passing encryption control | Missing IaC configuration did **not** prove plaintext storage. AWS applied default SSE-S3. Explicitly declare the intended encryption policy for reviewability. |
| Network | TCP/22 allowed from `0.0.0.0/0` | Removed the unused SSH rule | Verify the rule is absent in a resource-specific rescan. A security group by itself does not prove a live host was reachable. |
| Deployment identity | Direct AdministratorAccess attachment and long-lived keys | Moved the policy attachment to a group; registered MFA | Group attachment changes administration structure, not the breadth of admin permissions. Replace static deployment keys with a scoped role/federation and retire old keys. |
| Developer identities | Direct PowerUserAccess attachments and missing MFA | Group-based attachments and MFA registration | Confirm MFA enforcement, effective privileges, session conditions, and access-key handling separately. Registration alone is not enforcement. |

## Why the totals are not the whole story

The historical comparison improved from 71/167 to 76/167 passing rows. A rolling root-usage check can turn green with elapsed time, independently of a configuration change. Security Hub findings can also arrive asynchronously. Treat aggregate improvement as context; close a finding only when the relevant resource and control have been rechecked.

The publication includes the original after-scan aggregate. It does not include a complete resource-by-resource before/after export, so the aggregate alone cannot prove that every changed result was caused by remediation.

## Follow-up work

- Review account-level S3 public-access protections and the IAM password-policy baseline.
- Reduce the deploy identity's effective permissions; a group holding AdministratorAccess still grants AdministratorAccess.
- Use short-lived deployment credentials and confirm old keys are removed.
- Capture configuration snapshots and matching result IDs for future before/after comparisons.
- Keep documented exceptions, owners, and validation dates with the risk register.

## Technical references

- [AWS S3 default-encryption FAQ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-encryption-faq.html)
- [AWS MFA-protected API access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html)
- [AWS IAM access-key guidance](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)

Control themes here are explanatory, not a formal assessment against every SOC 2 or CIS requirement.
