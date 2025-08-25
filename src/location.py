import dataclasses
import math


@dataclasses.dataclass
class Location:
    x_list: list[float]

    def dist(self, other: "Location") -> float:
        assert len(self.x_list) == len(other.x_list)

        return math.sqrt(
            sum(
                (x - x_) ** 2
                for x, x_ in zip(self.x_list, other.x_list)
            )
        )

    def update(self, dx_list: list[float]):
        assert len(self.x_list) == len(dx_list)

        for i, dx in enumerate(dx_list):
            self.x_list[i] += dx
