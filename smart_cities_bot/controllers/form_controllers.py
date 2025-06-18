from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, CallbackContext
from models.residuosList import residuosList
from models.residuo import Residuo
from controllers.controllers import Controllers
ASK_PHOTO, ASK_LOCATION = range(2)
class Form_controllers:
    
    @staticmethod
    async def start_form_button(update:Update, context:ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        await update.effective_message.reply_text(f"Haz iniciado el formulario para registrar un residuo ♻️\n\n"
                                        f"---------------\n"
                                        f"*Comandos* 💡\n"
                                        f"/cancel: Si en cualquier momento deseas cancelar el formulario❌\n"
                                        f"---------------\n\n"
                                        f"Para iniciar por favor envia una foto del residuo 📸\n"
                                        f"(Puedes tomarla o seleccionarla de tu galeria)", 
                                        parse_mode='markdown')
        return ASK_PHOTO
        
    
        
    @staticmethod
    async def ask_message(update:Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f"Haz iniciado el formulario para registrar un residuo ♻️\n\n"
                                        f"---------------\n"
                                        f"*Comandos* 💡\n"
                                        f"/cancel: Si en cualquier momento deseas cancelar el formulario❌\n"
                                        f"---------------\n\n"
                                        f"Para iniciar por favor envia una foto del residuo 📸\n"
                                        f"(Puedes tomarla o seleccionarla de tu galeria)", 
                                        parse_mode='markdown')
        
        return ASK_PHOTO

    @staticmethod
    async def ask_photo(update:Update, context: ContextTypes.DEFAULT_TYPE):
        print("mask photo activo")
        message = update.effective_message
        if message.photo:
            context.user_data["form_photo"] = message.photo[1].file_id
            await update.message.reply_text(f"Foto detectada correctamente 📸 ✅\n"
                                            f"Ahora por favor envia la localización del residuo 📍")
            return ASK_LOCATION
        
        else:
            await update.message.reply_text(f"No se detecto una foto 📸👀, vuele a intentarlo\n"
                                            f"---------------\n"
                                            f"*Comandos* 💡\n"
                                            f"/cancel: Si en cualquier momento deseas cancelar el formulario❌\n"
                                            f"---------------\n\n",
                                            parse_mode='markdown')
            return ASK_PHOTO

    @staticmethod
    async def ask_location(update:Update, context: ContextTypes.DEFAULT_TYPE):
        message = update.message
        if message.location:
            context.user_data["latitude"] = update.message.location.latitude
            context.user_data["longitude"] = update.message.location.longitude
            await update.message.reply_text("Localización detectada 🗺️")
            await Form_controllers.create_residuo(update, context)
            return ConversationHandler.END
        else:
            await update.message.reply_text(f"No se detecto una localización 📍👀, vuele a intentarlo\n"
                                            f"---------------\n"
                                            f"*Comandos* 💡\n"
                                            f"/cancel: Si en cualquier momento deseas cancelar el formulario❌\n"
                                            f"---------------\n\n",
                                            parse_mode='markdown')
            return ASK_LOCATION
    
    @staticmethod
    async def cancel_form(update:Update, context: ContextTypes.DEFAULT_TYPE):
         await update.message.reply_text("Se ha cancelado el formulario ❌, puedes volver a iniciar usando el comando: /form")
         await Controllers.start(update, context)
         return ConversationHandler.END
     
    @staticmethod
    async def create_residuo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        file_id = context.user_data.get("form_photo")
        latitude = context.user_data.get("latitude")
        longitude = context.user_data.get("longitude")
        residuo = Residuo(file_id, latitude, longitude)
        residuosList.append(residuo)
        caption = f"Nuevo registro de residuo completado! ♻️\nLatitud: {residuo.latitude}\nLongitud: {residuo.longitude}\nFecha: {residuo.date}\nHora: {residuo.time}"
        await update.message.reply_photo(photo=residuo.file_id, caption=caption)
        await Controllers.start(update, context)
    
        