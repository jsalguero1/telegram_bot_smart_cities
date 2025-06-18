from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from controllers.controllers import Controllers
from controllers.form_controllers import Form_controllers
from controllers.conversation_handlers import form_conversation_handler
ASK_PHOTO, ASK_LOCATION = range(2)

# Token del bot
TOKEN = "7775429448:AAGU1cRTOkar0OqH_BndnsG6hq1z6pijkv0"

# Creacion de app
app = ApplicationBuilder().token(TOKEN).build()

# Handlers
app.add_handler(CommandHandler("start", Controllers.start))
app.add_handler(CommandHandler("list", Controllers.list_residuos))
#app.add_handler(CallbackQueryHandler(Form_controllers.form_button))
app.add_handler(form_conversation_handler.conversation_handler)

#polling
app.run_polling() 