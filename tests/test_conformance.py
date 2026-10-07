from runtime.adapters import MockEnvironmentA, MockEnvironmentB, MemoryTrace, RuleModelA, RuleModelB
from runtime.engine import AgentRuntime

def run(model, env, run_id):
    return AgentRuntime(model, env, MemoryTrace()).run("complete two-step goal", run_id)

def event_names(result):
    return [e.event for e in result["events"]]

def test_at01_multi_action_goal():
    r = run(RuleModelA(), MockEnvironmentA(), "AT-01")
    assert r["status"] == "completed"
    assert r["state"]["step_one_done"] and r["state"]["step_two_done"]

def test_at03_iteration_depends_on_observation():
    r = run(RuleModelA(), MockEnvironmentA(), "AT-03")
    names = event_names(r)
    assert names.count("decision") >= 3
    assert "observation" in names and "state_update" in names

def test_at04_goal_completion():
    r = run(RuleModelA(), MockEnvironmentA(), "AT-04")
    assert r["status"] == "completed"
    assert event_names(r)[-1] == "termination"

def test_ag01_model_swap():
    a = run(RuleModelA(), MockEnvironmentA(), "AG-01-A")
    b = run(RuleModelB(), MockEnvironmentA(), "AG-01-B")
    assert a["status"] == b["status"] == "completed"

def test_ag02_environment_swap():
    a = run(RuleModelA(), MockEnvironmentA(), "AG-02-A")
    b = run(RuleModelA(), MockEnvironmentB(), "AG-02-B")
    assert a["status"] == b["status"] == "completed"
    assert b["state"]["step_two_done"]

if __name__ == "__main__":
    tests = [
        test_at01_multi_action_goal,
        test_at03_iteration_depends_on_observation,
        test_at04_goal_completion,
        test_ag01_model_swap,
        test_ag02_environment_swap,
    ]
    for t in tests:
        t()
        print("PASS", t.__name__)
