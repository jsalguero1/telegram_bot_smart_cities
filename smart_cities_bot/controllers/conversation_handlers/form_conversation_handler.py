from telegram.ext import CommandHandler, MessageHandler,ConversationHandler, filters, CallbackQueryHandler
from controllers.form_controllers import Form_controllers

ASK_PHOTO, ASK_LOCATION = range(2)

conversation_handler = ConversationHandler(
        entry_points=[CommandHandler("form",Form_controllers.ask_message)],
        states={
            ASK_PHOTO: [MessageHandler(filters.ALL & ~filters.COMMAND, Form_controllers.ask_photo)],
            ASK_LOCATION: [MessageHandler(filters.ALL & ~filters.COMMAND, Form_controllers.ask_location)]
        },
        fallbacks=[
            MessageHandler(filters.COMMAND, Form_controllers.cancel_form)
        ]
    )