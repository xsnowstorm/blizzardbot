"""Managers for commands, events and tasks"""

import discord
import os
from typing import Dict, List

class CommandManager:
    """Manager for commands"""
    commands: Dict = {}

    def __init__(self, bot: discord.Client) -> None:
        """Initialize the manager

        [Args]:
            directory (List): A list containing the path for the commands directory
            bot (discord.Client): The client
        """
        self.__bot = bot

    def load(self, directory: List) -> None:
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


    async def execute(self, command_name: str, message: discord.Message, arguments: List) -> None:
        if command_name in self.commands:
            command = self.commands[command_name](self.__bot, self)
            await command.execute(message, arguments)
        else:
            await message.reply(f"Error: Unknown command: `{command_name}`")
