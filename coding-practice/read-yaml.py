# Config Parser CLI

import yaml

with open('config.yml','r') as f:
    config = yaml.safe_load(f)

print(config)