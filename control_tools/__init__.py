import logging.config
import pathlib
import json


__version__ = "0.0.1"

config_file = pathlib.Path(__file__).parents[0].joinpath("logging.json")
with open(config_file, "r", encoding="utf-8") as f:
    logging_config = json.load(f)

logging.config.dictConfig(logging_config)
