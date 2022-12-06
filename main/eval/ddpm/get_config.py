# Helper script to sample from a conditional DDPM model
# Add project directory to sys.path
import os
import sys

p = os.path.join(os.path.abspath("."), "main")
sys.path.insert(1, p)

import hydra


@hydra.main(config_path=os.path.join(p, "configs"))
def get_config(config):
    print(config)
    return config
   

if __name__ == "__main__":
    get_config()