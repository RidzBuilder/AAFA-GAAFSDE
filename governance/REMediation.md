# Remediation Registry

Canonical lifecycle:

OPEN → TRIAGED → ACTIONED → EVIDENCE SUBMITTED → VERIFIED → CLOSED

A remediation is not closed because code changed.

## Required remediation object

```yaml
remediation:
  id:
  source_stage:
  criterion_id:
  finding:
  severity:
  impact:
  root_cause:
  corrective_action:
  owner:
  priority:
  required_evidence:
  reentry_stage:
  due_condition:
  status:
  verification:
```

All BLOCKER/CRITICAL/MAJOR findings MUST have an explicit corrective action and re-entry stage.
