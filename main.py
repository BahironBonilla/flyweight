from fastapi import FastAPI
from flyweight_factory import VehicleIconFactory
from models import VehicleState
from data import test_data

app = FastAPI()

@app.post("/vehicles/")
async def get_vehicle_icon(type: str, color: str, icon: str, state: VehicleState):
    vehicle_icon = VehicleIconFactory.get_icon(type, color, icon)
    return vehicle_icon.render(state)

@app.get("/test-vehicles/")
async def get_test_vehicles():
    response = []
    for data in test_data:
        icon = VehicleIconFactory.get_icon(data["type"], data["color"], data["icon"])
        rendered_icon = icon.render(data["state"])
        response.append(rendered_icon)
    return response
