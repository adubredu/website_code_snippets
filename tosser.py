#!/usr/bin/env python3
"""
Shows how to toss a capsule to a container.
"""
from mujoco_py import load_model_from_path, MjSim, MjViewer
import os

#Load the model and environment from its xml file
model = load_model_from_path("../xmls/tosser.xml")
sim = MjSim(model)

#the time for each episode of the simulation
sim_horizon = 1000

#initialize the simulation visualization
viewer = MjViewer(sim)

#get initial state of simulation
sim_state = sim.get_state()

#repeat indefinitely
while True:
    #set simulation to initial state
    sim.set_state(sim_state)

    #for the entire simulation horizon
    for i in range(sim_horizon):

        #trigger the lever within the 0 to 150 time period
        if i < 150:
            sim.data.ctrl[:] = 0.0
        else:
            sim.data.ctrl[:] = -1.0
        #move one time step forward in simulation
        sim.step()
        viewer.render()

    if os.getenv('TESTING') is not None:
        break
