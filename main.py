%%writefile main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/v1/healthz")
def health():
    return {"status": "healthy"}


@app.get("/v1/metadata")
def metadata():
    return {
        "name": "Vera Engine",
        "version": "1.0",
        "deterministic": True
    }


@app.post("/v1/context")
def context(data: dict):
    return {"accepted": True}


@app.post("/v1/tick")
def tick(data: dict):

    merchant = data.get("merchant", {})
    trigger = data.get("trigger", {})

    kind = trigger.get("kind", "")
    payload = trigger.get("payload", {})

    views = merchant.get("performance", {}).get("views", 0)

    # research_digest
    if kind == "research_digest":

        return {
            "message": f"Your listing received {views} views recently. New search trends are emerging in your category. Would you like a campaign draft based on these trends?",
            "cta": "Draft Campaign",
            "send_as": "Vera",
            "suppression_key": trigger.get("suppression_key"),
            "rationale": "Curiosity + Reciprocity"
        }

    # regulation_change
    elif kind == "regulation_change":

        deadline = payload.get("deadline_iso", "upcoming deadline")

        return {
            "message": f"A compliance update requires action before {deadline}. Would you like a readiness checklist?",
            "cta": "View Checklist",
            "send_as": "Vera",
            "suppression_key": trigger.get("suppression_key"),
            "rationale": "Urgency + Authority"
        }

    # perf_spike
    elif kind == "perf_spike":

        growth = payload.get("delta_pct", 0)

        return {
            "message": f"Performance increased by {growth*100:.0f}% recently. Should we capitalize on this momentum with a promotion?",
            "cta": "Capture Demand",
            "send_as": "Vera",
            "suppression_key": trigger.get("suppression_key"),
            "rationale": "Curiosity + Opportunity"
        }
    # perf_dip elif kind == "perf_dip": drop = abs(payload.get("delta_pct", 0)) return { "message": f"Calls and engagement dropped by {drop*100:.0f}% recently. Would you like me to refresh your listing and promote your best offer?", "cta": "Recover Leads", "send_as": "Vera", "suppression_key": trigger.get("suppression_key"), "rationale": "Loss Aversion" } # festival_upcoming elif kind == "festival_upcoming": festival = payload.get("festival", "Festival") days = payload.get("days_until", "") return { "message": f"{festival} is coming in {days} days. Businesses often see increased demand before major festivals. Should I prepare a campaign?", "cta": "Launch Campaign", "send_as": "Vera", "suppression_key": trigger.get("suppression_key"), "rationale": "Urgency + Seasonal Demand" } # recall_due elif kind == "recall_due": service = payload.get("service_due", "scheduled service") return { "message": f"A customer is due for {service}. Would you like me to send a reminder with available slots?", "cta": "Send Reminder", "send_as": "Vera", "suppression_key": trigger.get("suppression_key"), "rationale": "Relationship + Specificity" }

    # default
    return {
        "message": "I found a growth opportunity for your business.",
        "cta": "Review",
        "send_as": "Vera",
        "suppression_key": "default",
        "rationale": "Default response"
    }


@app.post("/v1/reply")
def reply(data: dict):
    return {
        "message": "Reply received",
        "cta": None
    }
