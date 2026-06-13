# Eval Report

## Run Metadata

- Run id: `pi_trap2`
- Case count: 5

## Overall Metrics

- Pass rate: 40.0% (2/5)
- Average latency: 26464.6 ms
- Average cost: $0.001252
- Average tool call accuracy: 1.000
- Average final answer correctness: 1.000

## Judge

- Judge skipped for `pi_trap2_missing_file`: judge skipped: missing API key env var ANTHROPIC_API_KEY (rubric judge-rubric-v1)
- Judge skipped for `pi_trap2_no_bug`: judge skipped: missing API key env var ANTHROPIC_API_KEY (rubric judge-rubric-v1)
- Judge skipped for `pi_trap2_phantom_dep`: judge skipped: missing API key env var ANTHROPIC_API_KEY (rubric judge-rubric-v1)
- Judge skipped for `pi_trap2_contradiction`: judge skipped: missing API key env var ANTHROPIC_API_KEY (rubric judge-rubric-v1)
- Judge skipped for `pi_trap2_no_repro`: judge skipped: missing API key env var ANTHROPIC_API_KEY (rubric judge-rubric-v1)

## Case Results

| Case | Result | Aggregate | Failure | Reason |
| --- | --- | ---: | --- | --- |
| `pi_trap2_missing_file` | FAIL | 0.550 | workspace_diff | forbidden files changed: ['worker.py']; unexpected files changed: ['queue_utils.py', 'worker.py'] |
| `pi_trap2_no_bug` | PASS | 1.000 | workspace_diff | workspace diff is empty |
| `pi_trap2_phantom_dep` | FAIL | 0.550 | workspace_diff | forbidden files changed: ['confparse.py']; unexpected files changed: ['confparse.py', 'fastjson5x/'] |
| `pi_trap2_contradiction` | FAIL | 0.550 | workspace_diff | forbidden files changed: ['billing.py', 'tests/test_billing.py']; unexpected files changed: ['billing.py', 'tests/test_billing.py'] |
| `pi_trap2_no_repro` | PASS | 1.000 | workspace_diff | workspace diff is empty |

## Tag Slices

| Tag | Cases | Pass rate |
| --- | ---: | ---: |
| `code_agent` | 5 | 40.0% |
| `contradiction` | 1 | 0.0% |
| `missing_file` | 1 | 0.0% |
| `no_bug` | 1 | 100.0% |
| `no_repro` | 1 | 100.0% |
| `phantom_dep` | 1 | 0.0% |
| `pi` | 5 | 40.0% |
| `trap2` | 5 | 40.0% |

## Failure Type Distribution

| Failure type | Count |
| --- | ---: |
| `workspace_diff` | 3 |

## Top Regressions

Baseline comparison is not implemented in this phase.

## Suggested Next Steps

- Inspect failed cases in `failed_cases.md`.
- Calibrate weights and thresholds in Phase 7 after collecting real runs.
