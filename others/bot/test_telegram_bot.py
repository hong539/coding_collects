import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# 設定Token
TOKEN = "your_bot_token"

# 定義處理/start指令的函式
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm a bot.")

# 定義處理文字訊息的函式
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# 建立bot物件，使用Upater作為參數，並且設定Token
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)

# 加入處理/start指令的Handler
start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)

# 加入處理文字訊息的Handler
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
updater.dispatcher.add_handler(echo_handler)

# 開始接收和處理訊息
updater.start_polling()