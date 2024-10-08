from aiogram.types import BotCommand


async def setup_bot_command(bot):
    """Все команды для бота"""

    bot_command = [
        BotCommand(command='/start', description='Старт'),
        BotCommand(command='/test', description='Тест работы'),
        BotCommand(command='/getmyid', description='Получить свой ChatID'),
        BotCommand(command='/cancel', description='Отменить текущие действия'),
    ]

    await bot.set_my_commands(bot_command)