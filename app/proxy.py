import os
from loguru import logger
from whatsapp_chatbot_python import GreenAPIBot, Notification


class Proxy:
    def __init__(self):
        self.id_instance = os.getenv("ID_INSTANCE")
        self.api_token_instance = os.getenv("TOKEN")
        self.bot = GreenAPIBot(id_instance=self.id_instance, api_token_instance=self.api_token_instance)
        
    def send_notification(self, chat_id: str, message: str):
        try:
            self.bot.api.sending.sendMessage(chatId=chat_id, message=message)
            logger.info(f"Notification sent to {chat_id}")
        except Exception as e:
            logger.error(f"Failed to send notification to {chat_id}: {e}")