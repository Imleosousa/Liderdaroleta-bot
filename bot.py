import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TOKEN = "8895471840:AAGZ1MQKqMdKKvURT9fmS3F_7znu4hA_uqg"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.effective_user.first_name
    teclado = [[InlineKeyboardButton("⚡ ESTOU PRONTO", callback_data="msg2")]]
    await update.message.reply_text(
        f"🔴 SISTEMA ATIVADO.\n\n"
        f"Olá {nome}.\n\n"
        f"Tens 3 minutos?\n\n"
        f"Vou mostrar-te algo que os\n"
        f"casinos gastam milhões\n"
        f"para esconder.",
        reply_markup=InlineKeyboardMarkup(teclado)
    )

async def msg2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    teclado = [[InlineKeyboardButton("🔥 O QUE DESCOBRISTE?", callback_data="msg3")]]
    await update.callback_query.message.reply_text(
        "Perdi 4.200€ na roleta.\n\n"
        "Em vez de desistir,\n"
        "passei 6 meses a estudar\n"
        "cada jogada, cada padrão.\n\n"
        "Descobri algo que mudou tudo.",
        reply_markup=InlineKeyboardMarkup(teclado)
    )

async def msg3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    teclado = [[InlineKeyboardButton("😱 COMO É POSSÍVEL?", callback_data="msg4")]]
    await update.callback_query.message.reply_text(
        "Que a roleta tem padrões.\n\n"
        "E eu aprendi a lê-los.\n\n"
        "✅ +340€ na 1ª semana\n"
        "✅ +890€ na 3ª semana\n"
        "✅ Banido de 3 casinos\n\n"
        "Por ganhar demasiado.",
        reply_markup=InlineKeyboardMarkup(teclado)
    )

async def msg4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    teclado = [[InlineKeyboardButton("🤖 QUERO ENTRAR", callback_data="msg5")]]
    await update.callback_query.message.reply_text(
        "Criei uma IA.\n\n"
        "Ela lê os padrões da roleta\n"
        "em tempo real e envia sinais\n"
        "para um canal privado.\n\n"
        "Os meus membros seguem.\n"
        "E lucram.\n\n"
        "Todos os dias.",
        reply_markup=InlineKeyboardMarkup(teclado)
    )

async def msg5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    teclado = [[InlineKeyboardButton("✅ QUERO O LINK", callback_data="msg6")]]
    await update.callback_query.message.reply_text(
        "⚠️ O canal é PRIVADO.\n\n"
        "Não cobro nada.\n\n"
        "Só precisas de te registar\n"
        "no casino pelo meu link\n"
        "e fazer um depósito.\n\n"
        "Isso é tudo.\n\n"
        "Sem mensalidades.\n"
        "Sem taxas.\n"
        "Acesso GRATUITO.",
        reply_markup=InlineKeyboardMarkup(teclado)
    )

async def msg6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text(
        "🔗 O teu link:\n\n"
        "[LINK DO AFILIADO AQUI]\n\n"
        "1️⃣ Regista-te\n"
        "2️⃣ Faz o depósito\n"
        "3️⃣ Envia-me a print aqui\n\n"
        "Adds ao canal em 5 minutos. ⚡"
    )

async def receber_print(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.effective_user.first_name
    await update.message.reply_text(
        f"✅ Confirmado, {nome}!\n\n"
        "Bem-vindo ao canal mais\n"
        "exclusivo de Portugal. 🔴\n\n"
        "Prepara-te para o que\n"
        "vem a seguir. 🎰"
    )

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(msg2, pattern="^msg2$"))
    app.add_handler(CallbackQueryHandler(msg3, pattern="^msg3$"))
    app.add_handler(CallbackQueryHandler(msg4, pattern="^msg4$"))
    app.add_handler(CallbackQueryHandler(msg5, pattern="^msg5$"))
    app.add_handler(CallbackQueryHandler(msg6, pattern="^msg6$"))
    app.add_handler(MessageHandler(filters.PHOTO, receber_print))
    print("✅ Bot a correr...")
    await app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    asyncio.run(main())
