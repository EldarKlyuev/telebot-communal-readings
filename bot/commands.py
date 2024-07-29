from aiogram.types import BotCommand


async def setup_bot_command(bot):
    """Все команды для бота"""

    bot_command = [
        BotCommand(command='/start', description='Старт'),
    ]

    await bot.set_my_commands(bot_command)