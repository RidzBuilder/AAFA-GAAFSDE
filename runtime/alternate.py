from .contracts import TraceEvent

class AlternateRuntime:
    """Second runtime implementation using the same model/environment/storage contracts."""

    def __init__(self, model, environment, storage, max_steps=8):
        self.model, self.environment, self.storage, self.max_steps = model, environment, storage, max_steps

    def run(self, goal, run_id):
        from .contracts import State
        state, observations = State(), []
        self.storage.append(TraceEvent(run_id, "goal", {"goal": goal}))
        for step in range(self.max_steps):
            d = self.model.decide(goal, state, observations)
            self.storage.append(TraceEvent(run_id, "decision", {"step": step, "capability": d.capability_id}))
            if d.capability_id == "terminate":
                self.storage.append(TraceEvent(run_id, "termination", {"reason": "goal_state_reached"}))
                return {"status": "completed", "state": state.values, "events": self.storage.events()}
            self.storage.append(TraceEvent(run_id, "action_requested", {"capability": d.capability_id}))
            o = self.environment.execute(d.capability_id, state)
            self.storage.append(TraceEvent(run_id, "observation", {"action_id": o.action_id, "result": o.result, "success": o.success}))
            if not o.success:
                self.storage.append(TraceEvent(run_id, "termination", {"reason": "action_failed"}))
                return {"status": "failed", "state": state.values, "events": self.storage.events()}
            observations.append(o)
            state.values[f"{o.action_id}_done"] = True
            state.values[f"{o.action_id}_result"] = o.result
            self.storage.append(TraceEvent(run_id, "state_update", {"state": dict(state.values)}))
        return {"status": "failed", "state": state.values, "events": self.storage.events()}

class ListTrace:
    name = "list-trace"
    def __init__(self):
        self._events = []
    def append(self, event):
        self._events.append(event)
    def events(self):
        return list(self._events)
