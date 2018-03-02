from .main import Notification
import telepot

class TelegramNotification(Notification):

    def __init__(self):
        super(Notification, self).__init__()
        self.bot = telepot.Bot('535630901:AAE9rJEtkg3PLMKBbtcvdIA-CQFdxEb_g-M')
        self.chat_id = "517543770"

    def notify(self, string):
        print("****"+string+"****")
        self.bot.sendMessage(self.chat_id, "NOT: "+string)
