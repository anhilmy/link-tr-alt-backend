import sys
import yaml

try:
    with open(".local.yml", "r") as file:
        config = yaml.safe_load(file)
except Exception as errs:
    print(str(errs))
    sys.exit("error when opening config file")


class Config:
    SQLALCHEMY_DATABASE_URI = config.get("dsn")
    SQLALCHEMY_TRACK_MODIFICATIONS = (
        config["db_track_modification"]
        if config.get("db_track_modification") != None
        else False
    )
