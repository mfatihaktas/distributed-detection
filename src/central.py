import simpy

from src import (
    detector,
    target,
)

from src.utils.debug import DEBUG, slog


class CommandCenter:
    def __init__(
        self,
        name: str,
        env: simpy.Environment,
        step_time: float,
        detector_list: list[detector.Detector],
        target: target.Target,
    ) -> None:
        self.name = name
        self.env = env
        self.step_time = step_time
        self.detector_list = detector_list
        self.target = target

        self._num_detects_list = []

    def __repr__(self):
        return f"CommandCenter(name= {self.name})"

    def run(self):
        slog(DEBUG, self.env, self, "started")

        step = 0
        while True:
            yield self.env.timeout(self.step_time)

            num_detects = 0
            for detector in self.detector_list:
                num_detects += int(detector.detects(self.target))

            slog(DEBUG, self.env, self, f"detect-step-{step}", num_detects=num_detects)
            self._num_detects_list.append(num_detects)
            step += 1
