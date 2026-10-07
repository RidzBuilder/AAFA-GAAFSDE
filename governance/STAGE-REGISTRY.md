# AAFA-FSDW Stage Registry

Normative operational parent: AAFA-FSDW v0.1 LOCKED.

| Stage | Name | Primary objective | Minimum evidence ceiling |
|---|---|---|---|
| S00 | Charter | establish scope, authority, governance | E1 |
| S01 | Requirements | establish testable requirements and claims | E1/E2 |
| S02 | Architecture | establish provider-neutral architecture | E1/E2 |
| S03 | Contracts | establish executable contracts/interfaces | E2 |
| S04 | UX/UI + Frontend | implement user-facing surface | E2/E3 |
| S05 | Backend + Data | implement services and persistence | E2/E3 |
| S06 | Agent Core + Capabilities | implement observable agent loop | E3/E4 |
| S07 | Runtime Integration | execute real runtime actions | E3/E4 |
| S08 | Security + Trust | enforce authority and safety boundaries | E3/E4 |
| S09 | Observability + Evaluation | reconstruct behavior and evaluate outcomes | E4 |
| S10 | AAFA Conformance | execute AT/AG tests reproducibly | E5 |
| S11 | Release + Governance | release only with evidence and controls | E5 |

## Universal stage contract

Every stage MUST define:

- id
- name
- objective
- inputs
- outputs
- required_skills
- allowed_providers
- entry_criteria
- activities
- exit_criteria
- evidence_required
- failure_conditions
- remediation
- downstream_dependencies
- rollback_or_reentry

## Transition rules

1. No Evidence, No PASS.
2. No Silent Bypass.
3. Controlled exceptions must be explicit and cannot create proof.
4. Claims MUST match evidence.
5. Dependency changes can trigger regression.
6. Agentic proof requires runtime behavioral evidence.
7. Agnostic proof requires replacement/swap evidence.
8. Requested, executed, and succeeded actions MUST remain distinguishable.
9. Recovery MUST be tested where applicable.
10. Human authority MUST remain explicit.
11. Evidence MUST be reproducible.
