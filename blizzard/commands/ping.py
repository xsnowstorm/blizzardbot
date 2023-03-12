from blizzard import Command

class Cmd(Command):
    name = "ping"
    description = "Ping command"

    async def execute(self, message, arguments):
        await message.reply("Pong!")
