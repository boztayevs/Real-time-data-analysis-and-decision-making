from datetime import datetime
import matplotlib.pyplot as plt

# Custom Dataset
events_data = [
    {"timestamp": "09:00", "route": "AITU-Campus-Residence", "bus": "B03", "passengers": 12, "speed_kmh": 40, "status": "ON_ROUTE"},
    {"timestamp": "09:01", "route": "AITU-Campus-Residence", "bus": "B04", "passengers": 15, "speed_kmh": 35, "status": "ON_ROUTE"},
    {"timestamp": "09:02", "route": "AITU-Campus-Residence", "bus": "B03", "passengers": 14, "speed_kmh": 42, "status": "ON_ROUTE"},
    {"timestamp": "09:03", "route": "AITU-Campus-Residence", "bus": "B04", "passengers": 18, "speed_kmh": 38, "status": "ON_ROUTE"},
    {"timestamp": "09:04", "route": "AITU-Campus-Residence", "bus": "B03", "passengers": 22, "speed_kmh": 0, "status": "STOPPED"},
    {"timestamp": "09:05", "route": "AITU-Campus-Residence", "bus": "B04", "passengers": 25, "speed_kmh": 30, "status": "ON_ROUTE"},
    {"timestamp": "09:06", "route": "AITU-Campus-Residence", "bus": "B03", "passengers": 24, "speed_kmh": 45, "status": "ON_ROUTE"},
    {"timestamp": "09:07", "route": "AITU-Campus-Residence", "bus": "B04", "passengers": 32, "speed_kmh": 25, "status": "ON_ROUTE"},
    {"timestamp": "09:08", "route": "AITU-Campus-Residence", "bus": "B03", "passengers": 26, "speed_kmh": 40, "status": "ON_ROUTE"},
    {"timestamp": "09:09", "route": "AITU-Campus-Residence", "bus": "B04", "passengers": 35, "speed_kmh": 20, "status": "ON_ROUTE"},
]

ALLOWED_STATUS = {"ON_ROUTE", "STOPPED"}

def validate_event(event):
    errors = []
    try:
        parsed_time = datetime.strptime(event["timestamp"], "%H:%M").time()
    except (KeyError, TypeError, ValueError):
        errors.append("Invalid timestamp")

    passengers = event.get("passengers")
    if not isinstance(passengers, int) or isinstance(passengers, bool) or passengers < 0:
        errors.append("Passengers must be a non-negative integer")

    speed = event.get("speed_kmh")
    if not isinstance(speed, (int, float)) or not 0 <= speed <= 120:
        errors.append("Speed_kmh must be between 0 and 120")

    status = event.get("status")
    if status not in ALLOWED_STATUS:
        errors.append("Status must be ON_ROUTE or STOPPED")

    if errors:
        return {"accepted": False, "errors": errors}
    return {"accepted": True, "event": event, "errors": []}

def event_stream(events):
    for event in events:
        result = validate_event(event)
        if result["accepted"]:
            yield result["event"]

def analyze_stream(stream):
    valid_events = list(stream)
    passengers = [e["passengers"] for e in valid_events]
    
    avg_passengers = sum(passengers) / len(passengers)
    max_passengers = max(passengers)
    stopped_count = sum(1 for e in valid_events if e["status"] == "STOPPED")
    busiest = max(valid_events, key=lambda x: x["passengers"])
    
    print(f"Average passenger count: {avg_passengers}")
    print(f"Maximum passenger count: {max_passengers}")
    print(f"Number of STOPPED events: {stopped_count}")
    print(f"Busiest minute and bus: {busiest['timestamp']} / {busiest['bus']}")

    # Plot generation to visually evaluate code output
    plt.figure(figsize=(8, 4))
    plt.plot([e["timestamp"] for e in valid_events], passengers, marker='o', color='green')
    plt.title('Passenger Load Over Time')
    plt.xlabel('Time')
    plt.ylabel('Passengers')
    plt.grid(True)
    plt.savefig('passenger_load_plot.png')
    print("Plot saved as passenger_load_plot.png. Include this in the Moodle upload.")

if __name__ == "__main__":
    stream = event_stream(events_data)
    analyze_stream(stream)