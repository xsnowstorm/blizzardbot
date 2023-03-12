"""Basic configuration of the bot"""
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    """configuration class"""
    botname: str = "Blizzard"
    prefix: str = "?"
    token: str = getenv("BLIZZARD_TOKEN", "")
