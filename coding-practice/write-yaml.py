import yaml

config_dict = {
    "job": {
        "name": "train_model",
        "resources": {
            "cpu": 4,
            "memory": 16
        },
        "env": {
            "model": "bert",
            "epochs": 10
        }
    }
}

# Write to a file
with open("written-config.yml", "w") as f:
    yaml.dump(config_dict, f, default_flow_style=False)
