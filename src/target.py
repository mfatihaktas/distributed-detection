from src import (
    location as location_module,
)


class Target:
    def __init__(
        self,
        start_location: location_module.Location,
        dx_per_sec_list: list[float],
    ) -> None:
        self.location = start_location
        self.dx_per_sec_list = dx_per_sec_list

    def move(self, duration: float):
        self.location.update(
            dx_list=[
                dx_per_sec * duration
                for dx_per_sec in self.dx_per_sec_list
            ]
        )
