"""Managers for commands, events and tasks"""

from typing import Dict, List
import os
import discord

__all__ = ["CommandManager"]

class CommandManager:
    """Manager for commands"""
    commands: Dict = {}

    def __init__(self, bot: discord.Client) -> None:
        """Initialize the manager

        [Args]:
            bot (discord.Client): The client
        """
        self.__bot = bot

    def load(self, directory: List) -> None:
        """Load commands in a directory
        
        [Args]:
            directory (List): A list containing the path for the commands directory
        """
        files = [
            i
            for i in os.listdir(os.path.join(*directory))
            if not i.startswith("__") and i.endswith(".py")
        ]
        for filename in files:
            module_name = filename[:-3]
            cmd = __import__(
                f"{'.'.join(directory)}.{module_name}", globals(), locals(), ["Cmd"], 0
            ).Cmd
            self.commands[cmd.name] = cmd


    async def execute(self, name: str, message: discord.Message, arguments: List) -> None:
        """Execute a command
        
        [Args]:
            name (str): Name of the command
            message (discord.Message): Message where the command was executed
            arguments (List): Arguments for the command
        """
        if name in self.commands:
            command = self.commands[name](self.__bot, self)
            await command.execute(message, arguments)
        else:
            await message.reply(f"Error: Unknown command: `{name}`")
