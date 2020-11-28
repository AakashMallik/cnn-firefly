#!/usr/bin/env python3

from pathlib import Path
from inquirer import Checkbox, List, prompt
from inquirer.themes import GreenPassion
from src.utils.path import CONFIG_ROOT
from src.main import Pipeline


config_list = [config_files for config_files in CONFIG_ROOT.iterdir()
               if config_files.is_file()]

if len(config_list) < 1:
    print(f"No config files found in [{CONFIG_ROOT}]")
else:
    questions = [
        Checkbox(
            'configs',
            message="Select configs to run",
            choices=[config.name for config in config_list],
        ),
        List('confirmation',
             message='Continue?',
             choices=['yes', 'no'],
             default='no'
             )
    ]
    answers = prompt(questions, theme=GreenPassion())

    if answers["confirmation"] == "yes" or len(answers["configs"]) > 0:
        for config in answers["configs"]:
            Pipeline.execute(
                CONFIG_ROOT / config,
                {
                    "DEV_MODE": False
                }
            )
    else:
        print("Pipeline terminated")
