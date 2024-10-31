from models import VehicleState

test_data = [
    {"type": "car", "color": "blue", "icon": "🚗", "state": VehicleState(latitude=34.05, longitude=-118.25, direction=90, speed=65)},
    {"type": "car", "color": "red", "icon": "🚗", "state": VehicleState(latitude=40.71, longitude=-74.00, direction=180, speed=55)},
    {"type": "truck", "color": "green", "icon": "🚚", "state": VehicleState(latitude=34.05, longitude=-118.25, direction=45, speed=50)},
    {"type": "motorcycle", "color": "black", "icon": "🏍️", "state": VehicleState(latitude=51.50, longitude=-0.12, direction=270, speed=70)},
    {"type": "car", "color": "yellow", "icon": "🚗", "state": VehicleState(latitude=48.85, longitude=2.35, direction=90, speed=60)},
    {"type": "truck", "color": "blue", "icon": "🚚", "state": VehicleState(latitude=35.68, longitude=139.76, direction=135, speed=45)},
    {"type": "motorcycle", "color": "red", "icon": "🏍️", "state": VehicleState(latitude=-33.87, longitude=151.20, direction=0, speed=80)},
    {"type": "car", "color": "blue", "icon": "🚗", "state": VehicleState(latitude=37.77, longitude=-122.41, direction=270, speed=62)},
    {"type": "truck", "color": "green", "icon": "🚚", "state": VehicleState(latitude=55.75, longitude=37.61, direction=90, speed=55)},
    {"type": "motorcycle", "color": "black", "icon": "🏍️", "state": VehicleState(latitude=52.52, longitude=13.41, direction=180, speed=75)}
]
