from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Tu token de bot de Telegram
TOKEN = '7907782756:AAEK7W6dXyXaqWpIxgGvxxmXFViuf9tOfP8'

# Datos de los juegos: descripción y enlace
juegos = [
    {"nombre": "📚 UN VIAJE AL MUNDO DE LA LECTURA", "descripcion": "Explora el mundo de la lectura.", "link": "https://link_juego1.com"},
    {"nombre": "🎹 APRENDE TOCAR EL PIANO", "descripcion": "Aprende música de manera interactiva.", "link": "https://scratch.mit.edu/projects/1100288301"},
    {"nombre": "📐 LA ISLA DE LAS MATEMÁTICAS", "descripcion": "Diviértete resolviendo problemas matemáticos.", "link": "https://view.genially.com/671961fb7884b6d68940cf8e/interactive-content-operaciones-"},
    {"nombre": "🐾 CAZADOR DE HISTORIAS", "descripcion": "Es un juego que se realiza mediante Quiz de preguntas de cierto y falso sobre el tema del istmo de Panamá,", "link": "https://kahoot.it/solo/?quizId=32812359-1fed-4000-a05f-b54716fdf72e  "},
    {"nombre": "🧩 WORD MAYHEM", "descripcion": "Resuelve desafíos de palabras en ingles y aprende de manera divertida.", "link": "https://www.tynker.com/play/wm-try2/6742a19b0d8d4271f07f7de2-882162Xi,diqfJ9yu3MK5tOpLD2zUk"},
    {"nombre": "✍️ CONSTRUCTOR DE HISTORIAS", "descripcion": "Crea tus propias historias a partir de imágenes.", "link": "https://padlet.com/electroos2022/constructor-de-historia-mmcmrx1lb8aedrac"},
    {"nombre": "🔬 LA CARRERA DE LA CIENCIA", "descripcion": "Compite resolviendo preguntas científicas básicas.", "link": "https://es.educaplay.com/recursos-educativos/21485435-carrera_cientifica.html"},
]

# Función para manejar el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton(juego["nombre"], callback_data=f"juego_{index}")]
        for index, juego in enumerate(juegos)
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🎮 <b>SELECCIONA UN JUEGO PARA APRENDER!!!:</b> 🎓",
        reply_markup=reply_markup,
        parse_mode="HTML"
    )

# Función para manejar los botones
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    data = query.data

    # Manejar selección de juegos
    if data.startswith("juego_"):
        index = int(data.split("_")[1])
        juego = juegos[index]

        # Botón para regresar al menú principal
        keyboard = [[InlineKeyboardButton("🔙 Regresar al Menú", callback_data="menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Enviar detalles del juego
        await query.edit_message_text(
            f"<b>{juego['nombre']}</b>\n\n{juego['descripcion']}\n\n"
            f"<a href='{juego['link']}'>🔗 Haz clic aquí para jugar</a>",
            parse_mode="HTML",
            reply_markup=reply_markup
        )

    # Regresar al menú principal
    elif data == "menu":
        keyboard = [
            [InlineKeyboardButton(juego["nombre"], callback_data=f"juego_{index}")]
            for index, juego in enumerate(juegos)
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "🎮 <b>Selecciona un juego educativo para aprender:</b> 🎓",
            reply_markup=reply_markup,
            parse_mode="HTML"
        )

# Función principal para iniciar el bot
def main() -> None:
    # Crea la aplicación del bot
    application = Application.builder().token(TOKEN).build()

    # Agrega los manejadores de comandos y botones
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Ejecuta el bot
    application.run_polling()

if __name__ == "__main__":
    main()
