from telegram.ext import Application, CommandHandler, MessageHandler, filters
from commands import start, help_command, echo

async def main():
    # Замените 'YOUR_TOKEN' на токен вашего бота
    application = Application.builder().token("YOUR_TOKEN").build()

    # Регистрация команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запуск бота
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())