"""Baseline Customer Support Ticket Routing Service (Pre-AI)."""


def check_health() -> dict[str, str]:
    return {"status": "healthy", "service": "customer-support-router"}


def route_ticket(category: str, priority: str) -> str:
    if priority.lower() == "urgent":
        return "tier-2-escalation-queue"
    if category.lower() in ("billing", "refund"):
        return "finance-support-queue"
    return "general-support-queue"


if __name__ == "__main__":
    print(check_health())
    print(route_ticket("billing", "normal"))