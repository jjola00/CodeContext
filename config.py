from pydantic import BaseModel
import json
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class AppConfig(BaseModel):
    greeting: str
    repeat_greeting: bool
    default_number: int

class ConfigRoot(BaseModel):
    app: AppConfig

class Config:
    def __init__(self):
        self.config = self._load_config()

    def _load_config(self) -> ConfigRoot:
        config_path = 'config.json'

        try:
            with open(config_path, 'r') as config_file:
                data = json.load(config_file)
                return ConfigRoot(**data)
        except FileNotFoundError:
            logger.warning(f"Config file {config_path} not found! Using defaults.")
        except json.JSONDecodeError:
            logger.error(f"Config file {config_path} is not valid JSON! Using defaults.")

        return ConfigRoot(
            app=AppConfig(
                greeting="Hello World",
                repeat_greeting=False,
                default_number=1
            )
        )

    def get_app_config(self) -> AppConfig:
        """Get the application configuration"""
        return self.config.app
