from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from models.residuosList import residuosList
from models.residuo import Residuo
from routes.routes import Routes
class Controllers:
    
    @staticmethod
    async def start (update:Update, context: ContextTypes.DEFAULT_TYPE):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Registrar Residuo ♻️", callback_data=Routes.FORM)],
            [InlineKeyboardButton(text="Listar residuos 📋", callback_data=Routes.LIST)],
            [InlineKeyboardButton(text="Visitar Smart Cities 🇨🇴", url="https://digitaltwin.smartcitycolombia.org/")]
        ])
        await update.effective_message.reply_text(f"Hola! estas hablando con bot de Smart Cities Colombia 🤖🇨🇴\n"
                                        f"Por favor recuerda que los mensajes de este bot son automatizados por lo que no hay una persona atendiendo este chat\n\n"
                                        f"*Que deseas hacer?* 💡\n",
                                        parse_mode="markdown", reply_markup=keyboard)
        
            
    @staticmethod
    async def create_residuo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        file_id = context.user_data.get("form_photo")
        latitude = context.user_data.get("latitude")
        longitude = context.user_data.get("longitude")
        residuo = Residuo(file_id, latitude, longitude)
        residuosList.append(residuo)
        caption = f"Nuevo registro de residuo completado! ♻️\nLatitud: {residuo.latitude}\nLongitud: {residuo.longitude}\nFecha: {residuo.date}\nHora: {residuo.time}"
        await update.message.reply_photo(photo=residuo.file_id, caption=caption)
        
    @staticmethod
    async def list_residuos (update: Update, context: ContextTypes.DEFAULT_TYPE):
        if len(residuosList) > 0:
            for residuo in residuosList:
                caption = f"Información del registro ♻️\nLatitud: {residuo.latitude}\nLongitud: {residuo.longitude}\nFecha: {residuo.date}\nHora: {residuo.time}"
                await update.effective_message.reply_photo(photo=residuo.file_id, caption=caption)
            await Controllers.start(update, context)
        else:
            await update.effective_message.reply_text("Actualmente no hay registros de residuos, crea uno para usar este comando")
            await Controllers.start(update, context)