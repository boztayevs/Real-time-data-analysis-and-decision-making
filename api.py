from fastapi import FastAPI
from main import validate_event

app = FastAPI()

def occupancy_category(passengers):
    if 0 <= passengers <= 10:
        return "LOW"
    if 11 <= passengers <= 20:
        return "MEDIUM"
    if 21 <= passengers <= 30:
        return "HIGH"
    return "OVER CAPACITY"

@app.post("/events")
def receive_event(event: dict):
    result = validate_event(event)
    if not result["accepted"]:
        return {
            "accepted": False,
            "errors": result["errors"],
            "occupancy_category": None
        }
    
    clean_event = result["event"]
    return {
        "accepted": True,
        "errors": [],
        "occupancy_category": occupancy_category(clean_event["passengers"]),
        "event": clean_event
    }