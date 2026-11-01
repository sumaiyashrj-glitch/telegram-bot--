import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Application, CommandHandler,
                          CallbackQueryHandler, ContextTypes)

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    kb = InlineKeyboardMarkup([[
        InlineKeyboardButton("হ্যালো", callback_data="hi"),
        InlineKeyboardButton("সাহায্য", callback_data="help"),
    ]])
    await update.message.reply_text("একটি বাটন বেছে নিন:", reply_markup=kb)

async def button(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    text = "হ্যালো! আমি চালু আছি" if q.data == "hi" else "/start লিখুন"
    await q.edit_message_text(text)

app = Application.builder().token(os.environ["BOT_TOKEN"]).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.run_polling()
