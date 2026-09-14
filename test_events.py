from main import validate_event

def test_valid_event_boundary():
    event = {"timestamp": "09:00", "route": "AITU", "bus": "B03", "passengers": 30, "speed_kmh": 120, "status": "ON_ROUTE"}
    assert validate_event(event)["accepted"] is True

def test_invalid_speed():
    event = {"timestamp": "09:00", "route": "AITU", "bus": "B03", "passengers": 15, "speed_kmh": -5, "status": "ON_ROUTE"}
    assert validate_event(event)["accepted"] is False

def test_invalid_status():
    event = {"timestamp": "09:00", "route": "AITU", "bus": "B03", "passengers": 15, "speed_kmh": 40, "status": "PARKED"}
    assert validate_event(event)["accepted"] is False