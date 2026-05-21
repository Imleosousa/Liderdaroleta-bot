import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = "8895471840:AAGZ1MQKqMdKKvURT9fmS3F_7znu4hA_uqg"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.effective_user.first_name
    teclado = [[InlineKeyboardButton("⚡ ESTOU PRONTO", callback_data="msg2")]]
    await update.message.reply_text(
        f"🔴 SISTEMA ATIVADO.\n\nOlá {nome}.\n\nTens 3 minutos?\n\nVou mostrar-te algo que os casinos gastam milhões para esconder.",
        reply_markup=InlineKeyboardMarkup(teclado)
    )

async def msg2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    teclado = [[InlineKeyboardButton("🔥 O QUE DESCOBRISTE?", callback_data="msg3")]]
    await update.callback_query.message.reply_text(
        "Perdi 4.200€ na roleta.\n\nEm vez de desistir, passei 6 meses a estudar cada jogada, cada padrão.\n\nDescobri algo que mudou tudo.",
        reply_markup=InlineKeyboardMarkup(teclado)
    )

async def msg3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    teclado = [[InlineKeyboardButton("😱 COMO É POSSÍVEL?", callback_data="msg4")]]
    await update.callback_query.message.reply_text(
        "Que a roleta tem padrões.\n\nE eu aprendi a lê-los.\n\n✅ +340€ na 1ª semana\n✅ +890€ na 3ª semana\n✅ Banido de 3 casinos\n\nPor ganhar demasiado.",
        reply_markup=InlineKeyboardMarkup(teclado)
    )

async def msg4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    teclado = [[InlineKeyboardButton("🤖 QUERO ENTRAR", callback_data="msg5")]]
    await update.callback_query.message.reply_text(
        "Criei uma IA.\n\nEla lê os padrões da roleta em tempo real e envia sinais para um canal privado.\n\nOs meus membros seguem. E lucram.\n\nTodos os dias.",
        reply_markup=InlineKeyboardMarkup(teclado)
    )

async def msg5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    teclado = [[InlineKeyboardButton("✅ QUERO O LINK", callback_data="msg6")]]
    await update.callback_query.message.reply_text(
        "⚠️ O canal é PRIVADO.\n\nNão cobro nada.\n\nSó precisas de te registar no casino pelo meu link e fazer um depósito.\n\nSem mensalidades. Sem taxas. Acesso GRATUITO.",
        reply_markup=InlineKeyboardMarkup(teclado)
    )

async def msg6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text(
        "🔗 O teu link:\n\n[LINK DO AFILIADO AQUI]\n\n1️⃣ Regista-te\n2️⃣ Faz o depósito\n3️⃣ Envia-me a print aqui\n\nAdds ao canal em 5 minutos. ⚡"
    )

async def receber_print(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.effective_user.first_name
    await update.message.reply_text(
        f"✅ Confirmado, {nome}!\n\nBem-vindo ao canal mais exclusivo de Portugal. 🔴\n\nPrepara-te para o que vem a seguir. 🎰"
    )

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(msg2, pattern="^msg2$"))
    app.add_handler(CallbackQueryHandler(msg3, pattern="^msg3$"))
    app.add_handler(CallbackQueryHandler(msg4, pattern="^msg4$"))
    app.add_handler(CallbackQueryHandler(msg5, pattern="^msg5$"))
    app.add_handler(CallbackQueryHandler(msg6, pattern="^msg6$"))
    app.add_handler(MessageHandler(filters.PHOTO, receber_print))
    print("✅ Bot a correr...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)
