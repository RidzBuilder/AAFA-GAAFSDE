from .contracts import EnvironmentAdapter, ModelAdapter, State, StorageAdapter, TraceEvent

class AgentRuntime:
    def __init__(self, model: ModelAdapter, environment: EnvironmentAdapter, storage: StorageAdapter, max_steps: int = 8):
        self.model = model
        self.environment = environment
        self.storage = storage
        self.max_steps = max_steps

    def run(self, goal: str, run_id: str):
        state = State()
        observations = []
        self.storage.append(TraceEvent(run_id, "goal", {"goal": goal}))

        for step in range(self.max_steps):
            decision = self.model.decide(goal, state, observations)
            self.storage.append(TraceEvent(run_id, "decision", {
                "step": step, "capability": decision.capability_id, "reason": decision.reason
            }))

            if decision.capability_id == "terminate":
                self.storage.append(TraceEvent(run_id, "termination", {"reason": "goal_state_reached"}))
                return {"status": "completed", "state": state.values, "events": self.storage.events()}

            self.storage.append(TraceEvent(run_id, "action_requested", {"capability": decision.capability_id}))
            observation = self.environment.execute(decision.capability_id, state)
            self.storage.append(TraceEvent(run_id, "observation", {
                "action_id": observation.action_id, "result": observation.result, "success": observation.success
            }))
            if not observation.success:
                self.storage.append(TraceEvent(run_id, "termination", {"reason": "action_failed"}))
                return {"status": "failed", "state": state.values, "events": self.storage.events()}

            observations.append(observation)
            state.values[f"{observation.action_id}_done"] = True
            state.values[f"{observation.action_id}_result"] = observation.result
            self.storage.append(TraceEvent(run_id, "state_update", {"state": dict(state.values)}))

        self.storage.append(TraceEvent(run_id, "termination", {"reason": "max_steps_exceeded"}))
        return {"status": "failed", "state": state.values, "events": self.storage.events()}
