from runtime.adapters import MockEnvironmentA, MockEnvironmentB, MemoryTrace, RuleModelA, RuleModelB
from runtime.alternate import AlternateRuntime, ListTrace
from runtime.engine import AgentRuntime
from runtime.safety import AuthorityBoundary, GovernedEnvironment

def test_at02_environment_changes_observable_result():
    a = AgentRuntime(RuleModelA(), MockEnvironmentA(), MemoryTrace()).run("g", "AT-02-A")
    b = AgentRuntime(RuleModelA(), MockEnvironmentB(), MemoryTrace()).run("g", "AT-02-B")
    assert a["state"]["step_one_result"] != b["state"]["step_one_result"]

def test_at05_human_boundary_blocks_consequential_action():
    env = GovernedEnvironment(MockEnvironmentA(), AuthorityBoundary(approved=False))
    result = env.execute("consequential_action", __import__("runtime.contracts", fromlist=["State"]).State())
    assert result.success is False
    assert result.result["reason"] == "human_approval_required"

def test_ag03_adapter_swap():
    a = AgentRuntime(RuleModelA(), MockEnvironmentA(), MemoryTrace()).run("g", "AG-03-A")
    b = AgentRuntime(RuleModelA(), MockEnvironmentB(), MemoryTrace()).run("g", "AG-03-B")
    assert a["status"] == b["status"] == "completed"

def test_ag04_runtime_swap():
    a = AgentRuntime(RuleModelA(), MockEnvironmentA(), MemoryTrace()).run("g", "AG-04-A")
    b = AlternateRuntime(RuleModelA(), MockEnvironmentA(), ListTrace()).run("g", "AG-04-B")
    assert a["status"] == b["status"] == "completed"

def test_ag05_storage_swap():
    a = AgentRuntime(RuleModelA(), MockEnvironmentA(), MemoryTrace()).run("g", "AG-05-A")
    b = AgentRuntime(RuleModelA(), MockEnvironmentA(), ListTrace()).run("g", "AG-05-B")
    assert len(a["events"]) == len(b["events"])
