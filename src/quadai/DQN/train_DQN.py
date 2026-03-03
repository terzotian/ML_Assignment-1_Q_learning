"""
Train a DQN agent using sb3 on the droneEnv environment
"""

import os

from stable_baselines3 import DQN
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.callbacks import CheckpointCallback
import wandb
from wandb.integration.sb3 import WandbCallback

from env_DQN import droneEnv

run = wandb.init(
    # Set the wandb entity where your project will be logged (generally your team name).
    entity="1718441196-lingnan-university",
    # Set the wandb project where this run will be logged.
    project="CDS524Assignment1",
    # Track hyperparameters and run metadata.
    config={
        "algorithm": "DQN",
        "policy_type": "MlpPolicy",
        "total_timesteps": 5000000,
        "env_name": "Quadcopter-2D",
        "framework": "stable-baselines3",
        "learning_rate": 5e-5,
        "buffer_size": 1000000,
        "learning_starts": 50000,
        "batch_size": 32,
        "gamma": 0.99,
        "target_update_interval": 10000,
        "exploration_fraction": 0.2,
        "exploration_final_eps": 0.01,
    },
    sync_tensorboard=True,
    monitor_gym=True,
    save_code=True,
)

# Create log dir
log_dir = os.path.join(os.path.dirname(__file__), "tmp")
os.makedirs(log_dir, exist_ok=True)

# Create models dir
models_dir = os.path.join(os.path.dirname(__file__), "models")
os.makedirs(models_dir, exist_ok=True)

# Create and wrap the environment
env = droneEnv(False, False)
env = Monitor(env, log_dir)

# Create DQN agent
model = DQN(
    "MlpPolicy",
    env,
    verbose=1,
    tensorboard_log=log_dir,
    device="auto",
    learning_rate=5e-5,
    exploration_fraction=0.2,
    exploration_final_eps=0.01,
)

# Create checkpoint callback
checkpoint_callback = CheckpointCallback(
    save_freq=100000, save_path=models_dir, name_prefix="rl_model_v0"
)

# Train the agent
model.learn(
    total_timesteps=5000000,
    callback=[
        checkpoint_callback,
        WandbCallback(
            gradient_save_freq=100000,
            model_save_path=os.path.join(models_dir, run.id),
            model_save_freq=100000,
            verbose=2,
        ),
    ],
)
