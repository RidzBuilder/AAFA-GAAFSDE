# Evidence Registry

## Canonical evidence object

```yaml
evidence:
  id:
  claim_id:
  stage_id:
  level: E0|E1|E2|E3|E4|E5
  artifact:
  source:
  version:
  test:
  observed_at:
  verifier:
  reproducibility:
  integrity_reference:
  status:
```

## Levels

- E0 CLAIM
- E1 DESIGN
- E2 STATIC IMPLEMENTATION
- E3 RUNTIME EXECUTION
- E4 BEHAVIORAL TRACE
- E5 REPRODUCIBLE CONFORMANCE

## Promotion rule

Evidence MUST NOT be promoted automatically.

E5 is permitted only when the independently reproducible AAFA conformance harness passes all applicable mandatory tests.
