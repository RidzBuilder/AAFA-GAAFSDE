class AuthorityBoundary:
    """Explicit human-approval boundary for consequential capabilities."""

    def __init__(self, approved=False):
        self.approved = approved

    def authorize(self, capability_id: str) -> bool:
        if capability_id == "consequential_action":
            return self.approved
        return True

class GovernedEnvironment:
    name = "governed-env"

    def __init__(self, base_env, authority: AuthorityBoundary):
        self.base_env = base_env
        self.authority = authority

    def execute(self, capability_id, state):
        from .contracts import Observation
        if not self.authority.authorize(capability_id):
            return Observation(capability_id, {"blocked": True, "reason": "human_approval_required"}, False)
        return self.base_env.execute(capability_id, state)
