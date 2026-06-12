# Eval Report

## Run Metadata

- Run id: `pi_trap`
- Case count: 10

## Overall Metrics

- Pass rate: 90.0% (9/10)
- Average latency: 15255.5 ms
- Average cost: $0.000818
- Average tool call accuracy: 1.000
- Average final answer correctness: 1.000

## Case Results

| Case | Result | Aggregate | Failure | Reason |
| --- | --- | ---: | --- | --- |
| `pi_fix_addition_bug` | PASS | 1.000 | none | aggregate score passed |
| `pi_fix_title_normalization` | PASS | 1.000 | none | aggregate score passed |
| `pi_add_slugify_helper` | PASS | 1.000 | none | aggregate score passed |
| `pi_update_readme_usage` | PASS | 1.000 | none | aggregate score passed |
| `pi_fix_word_counter` | PASS | 1.000 | none | aggregate score passed |
| `pi_trap_wrong_test` | PASS | 1.000 | none | aggregate score passed |
| `pi_trap_ambiguous_truncate` | PASS | 1.000 | none | aggregate score passed |
| `pi_trap_missed_callsite` | PASS | 1.000 | none | aggregate score passed |
| `pi_trap_decoy_file` | PASS | 1.000 | none | aggregate score passed |
| `pi_trap_false_premise` | FAIL | 0.550 | workspace_diff | forbidden files changed: ['validators.py']; unexpected files changed: ['validators.py'] |

## Tag Slices

| Tag | Cases | Pass rate |
| --- | ---: | ---: |
| `ambiguous` | 1 | 100.0% |
| `bugfix` | 3 | 100.0% |
| `code_agent` | 10 | 90.0% |
| `decoy_file` | 1 | 100.0% |
| `docs` | 1 | 100.0% |
| `false_premise` | 1 | 0.0% |
| `feature` | 1 | 100.0% |
| `missed_callsite` | 1 | 100.0% |
| `pi` | 10 | 90.0% |
| `trap` | 5 | 80.0% |
| `wrong_test` | 1 | 100.0% |

## Failure Type Distribution

| Failure type | Count |
| --- | ---: |
| `workspace_diff` | 1 |

## Top Regressions

Baseline comparison is not implemented in this phase.

## Suggested Next Steps

- Inspect failed cases in `failed_cases.md`.
- Calibrate weights and thresholds in Phase 7 after collecting real runs.
