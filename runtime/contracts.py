from dataclasses import dataclass, field
from typing import Any, Protocol

@dataclass
class State:
    values: dict[str, Any] = field(default_factory=dict)

@dataclass
class Observation:
    action_id: str
    result: Any
    success: bool

@dataclass
class Decision:
    capability_id: str
    reason: str

@dataclass
class TraceEvent:
    run_id: str
    event: str
    payload: dict[str, Any]

class ModelAdapter(Protocol):
    name: str
    def decide(self, goal: str, state: State, observations: list[Observation]) -> Decision: ...

class EnvironmentAdapter(Protocol):
    name: str
    def execute(self, capability_id: str, state: State) -> Observation: ...

class StorageAdapter(Protocol):
    name: str
    def append(self, event: TraceEvent) -> None: ...
    def events(self) -> list[TraceEvent]: ...
