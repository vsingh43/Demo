# validate_playbook.py

import yaml
import sys


def validate_playbook(file_path):
    try:
        with open(file_path, "r") as file:
            yaml.safe_load(file)
        print(f"{file_path} is a valid YAML file.")
    except yaml.YAMLError as exc:
        print(f"Error in {file_path}: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    # Validate the sample playbook by default
    validate_playbook("playbooks/sample-playbook.yml")
