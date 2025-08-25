import simpy

from src import (
    detector,
    target as target_module,
)

from src.utils.debug import DEBUG, slog


class DetectionCenter:
    def __init__(
        self,
        name: str,
        env: simpy.Environment,
        step_time: float,
        detector_list: list[detector.Detector],
        target: target_module.Target,
        num_steps: int,
    ) -> None:
        self.name = name
        self.env = env
        self.step_time = step_time
        self.detector_list = detector_list
        self.target = target
        self.num_steps = num_steps

        self._num_detects_list = []

        self.run_proc = env.process(self.run())

    def __repr__(self):
        return f"Center(name= {self.name})"

    def run(self):
        slog(DEBUG, self.env, self, "started")

        for step in range(self.num_steps):
            yield self.env.timeout(self.step_time)

            num_detects = 0
            for detector in self.detector_list:
                num_detects += int(detector.detects(self.target))

            slog(DEBUG, self.env, self, f"Detection at step-{step}", num_detects=num_detects)
            self._num_detects_list.append(num_detects)

            self.target.move(duration=self.step_time)

        slog(DEBUG, self.env, self, "done")
