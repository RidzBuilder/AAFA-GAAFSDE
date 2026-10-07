from .contracts import Decision, EnvironmentAdapter, ModelAdapter, Observation, State, StorageAdapter, TraceEvent

class RuleModelA:
    name = "rule-model-a"
    def decide(self, goal, state, observations):
        if not state.values.get("step1_done"):
            return Decision("step_one", "step one is required")
        if not state.values.get("step2_done"):
            return Decision("step_two", "step two depends on observed step one")
        return Decision("terminate", "goal state reached")

class RuleModelB:
    name = "rule-model-b"
    def decide(self, goal, state, observations):
        # Same canonical contract, intentionally different implementation.
        return RuleModelA().decide(goal, state, observations)

class MockEnvironmentA:
    name = "mock-env-a"
    def execute(self, capability_id, state):
        if capability_id == "step_one":
            return Observation("step_one", {"value": 1}, True)
        if capability_id == "step_two":
            return Observation("step_two", {"value": 2}, True)
        return Observation(capability_id, None, False)

class MockEnvironmentB:
    name = "mock-env-b"
    def execute(self, capability_id, state):
        if capability_id == "step_one":
            return Observation("step_one", {"value": "one"}, True)
        if capability_id == "step_two":
            return Observation("step_two", {"value": "two"}, True)
        return Observation(capability_id, None, False)

class MemoryTrace:
    name = "memory"
    def __init__(self):
        self._events = []
    def append(self, event):
        self._events.append(event)
    def events(self):
        return list(self._events)
