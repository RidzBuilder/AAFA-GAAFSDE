from tests.test_conformance import (
    test_at01_multi_action_goal, test_at03_iteration_depends_on_observation,
    test_at04_goal_completion, test_ag01_model_swap, test_ag02_environment_swap
)
from tests.test_full_conformance import (
    test_at02_environment_changes_observable_result, test_at05_human_boundary_blocks_consequential_action,
    test_ag03_adapter_swap, test_ag04_runtime_swap, test_ag05_storage_swap
)

TESTS = [
 ("AT-01", test_at01_multi_action_goal),
 ("AT-02", test_at02_environment_changes_observable_result),
 ("AT-03", test_at03_iteration_depends_on_observation),
 ("AT-04", test_at04_goal_completion),
 ("AT-05", test_at05_human_boundary_blocks_consequential_action),
 ("AG-01", test_ag01_model_swap),
 ("AG-02", test_ag02_environment_swap),
 ("AG-03", test_ag03_adapter_swap),
 ("AG-04", test_ag04_runtime_swap),
 ("AG-05", test_ag05_storage_swap),
]
for test_id, fn in TESTS:
    fn()
    print(f"PASS {test_id}")
print("ALL REFERENCE AT/AG TESTS PASS")
