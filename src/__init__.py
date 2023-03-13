"""Command, Event and Task blueprints"""

from abc import ABC, abstractmethod
from typing import List
import discord

from .logger import Logger
from .manager import CommandManager

__all__ = ["Command"]

class Command(ABC):
    """Blueprint for a command"""
    name = ""
    description = ""
    usage = ""

    def __init__(self, bot: discord.Client, manager: CommandManager) -> None:
        """Initialize a command

        [Args]:
            bot (discord.Client): The client
            manager (blizzard.manager.CommandManager): The command manager

        [Raises]:
            ValueError: if 'name' field is empty
            ValueError: if 'description' field is empty
        """

        self.bot = bot
        self.manager = manager

        if not self.name:
            raise ValueError("Command name is required")

        if not self.description:
            raise ValueError("Command description is required")

    @abstractmethod
    async def execute(self, message: discord.Message, arguments: List):
        """Execute the command
        
        [Args]:
            message (discord.Message): the message that ran the command
            arguments (List): a list with the given arguments

        [Raises]:
            NotImplementedError: if this method is not implemented
        """
        raise NotImplementedError("Execute method is required")
