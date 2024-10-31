from pydantic import BaseModel

class VehicleState(BaseModel):
    latitude: float
    longitude: float
    direction: float
    speed: float

class VehicleIcon(BaseModel):
    type: str
    color: str
    icon: str

    def render(self, state: VehicleState):
        return {
            "type": self.type,
            "color": self.color,
            "icon": self.icon,
            "latitude": state.latitude,
            "longitude": state.longitude,
            "direction": state.direction,
            "speed": state.speed
        }
