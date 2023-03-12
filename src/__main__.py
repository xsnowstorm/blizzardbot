"""Starts the bot"""
import discord

from .config import Config
from .manager import CommandManager
from .logger import Logger


def main() -> None:
    """Main function"""
    bot = discord.Client(intents=discord.Intents.all())
    manager = CommandManager(bot)

    @bot.event
    async def on_ready() -> None:
        """on_ready event"""
        Logger.log(f"{Config.botname} has started")
        Logger.newline()
        Logger.log(f"Logged in as {bot.user.name}#{bot.user.discriminator}")
        Logger.log("Prefix:", Config.prefix)

        manager.load(["src", "commands"])

    @bot.event
    async def on_message(message: discord.Message) -> None:
        """Handle messages"""
        if message.author.bot or not message.content.startswith(Config.prefix):
            return
        parts = message.content[len(Config.prefix):].split(" ")
        command, args = [parts[0], parts[1:]]
        Logger.log(f"{message.author} used command {command} with arguments {args}")
        await manager.execute(command, message, args)

    bot.run(Config.token)

if __name__ == "__main__":
    main()
