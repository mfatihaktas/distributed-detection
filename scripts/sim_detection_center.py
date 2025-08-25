import simpy

from src import (
    center as center_module,
    detector as detector_module,
    location as location_module,
    target as target_module,
)


env = simpy.Environment()

detector_list = [
    detector_module.Detector_wProbDetectDecayingLinearly(
        name="detector-0",
        env=env,
        location=location_module.Location(x_list=[0]),
        max_range=100,
        decay_start_range=50,
    )
]

target = target_module.Target(
    start_location=location_module.Location(x_list=[100]),
    dx_per_sec_list=[-1],
)

center = center_module.DetectionCenter(
    name="center",
    env=env,
    step_time=1,
    detector_list=detector_list,  # type: ignore
    target=target,
    num_steps=10,
)

env.run()
