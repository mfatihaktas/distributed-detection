import abc
import random
import simpy

from src import (
    location as location_module,
    target as target_module,
)

from src.utils.debug import DEBUG, slog


class Detector:
    def __init__(
        self,
        name: str,
        env: simpy.Environment,
        location: location_module.Location,
    ) -> None:
        self.name = name
        self.env = env
        self.location = location


    @abc.abstractmethod
    def prob_detect(self, dist: float) -> float:
        pass

    def detects(self, target: target_module.Target) -> bool:
        dist = self.location.dist(target.location)
        p = self.prob_detect(dist)
        assert 0 <= p <= 1

        r = random.random()
        return r <= p


class Detector_wProbDetectDecayingLinearly:
    def __init__(
        self,
        name: str,
        env: simpy.Environment,
        max_range: int,
        decay_start_range: int,
    ) -> None:
        self.name = name
        self.env = env
        self.max_range = max_range
        self.decay_start_range = decay_start_range

    def __repr__(self):
        return (
            "Detector_wProbDetectDecayingLinearly("
            f"name= {self.name}, "
            f"max_range= {self.max_range}, "
            f"decay_start_range= {self.decay_start_range}"
            ")"
        )

    def prob_detect(self, dist: float) -> float:
        if dist < self.decay_start_range:
            return 1
        elif dist > self.max_range:
            return 0

        return 1 - (dist - self.decay_start_range) / (self.max_range - self.decay_start_range)
