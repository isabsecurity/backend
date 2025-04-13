import logging
import sys
import asyncio
from django.core.management.base import BaseCommand
from tg_bot.handlers import *
from tg_bot.dispatcher import   dp


# Set the default settings module for your Django project
async def main() -> None:
    await set_bot_commands()
    await dp.start_polling(bot)



class Command(BaseCommand):

    def handle(self, *args, **options):
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())