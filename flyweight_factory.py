from models import VehicleIcon

class VehicleIconFactory:
    _icons = {}

    @classmethod
    def get_icon(cls, type: str, color: str, icon: str) -> VehicleIcon:
        key = (type, color, icon)
        if key not in cls._icons:
            cls._icons[key] = VehicleIcon(type=type, color=color, icon=icon)
        return cls._icons[key]
