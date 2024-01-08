from typing import Dict, Any
from .zalo import ZaloHandler
from .website import WebsiteHandler
from .base import BaseHandler
from .rule import RuleLoader


class ChatSharing:
    def __init__(self):
        # chỗ này xài factory hoặc inject các kiểu vào nhé, lười nên fix cứng trong này luôn
        self.rule_loader: RuleLoader = RuleLoader()
        self.zalo_handler: ZaloHandler = ZaloHandler
        self.website_handler: WebsiteHandler = WebsiteHandler

    def set_rule_loader(self, rule_loader: RuleLoader):
        self.rule_loader = rule_loader

    def execute(self, message: Dict, handler: BaseHandler, **kwargs):
        self.rule_loader.load()
        handler.handle_message(message, self.rule_loader.get_selected_rule(), **kwargs)

    def handle_website_message_from_webhook(self, message: Dict = {'message': 'Hello'}):
        handler = self.website_handler()
        return self.execute(message, handler=handler)

    def handle_website_message_from_salesman(self, message: Dict = {'message': 'Hello'}):
        handler = self.website_handler()
        return self.execute(message, handler=handler, action_type='salesman_send_message')
