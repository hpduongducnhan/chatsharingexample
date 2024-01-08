from uuid import uuid4
from typing import Dict
from ..rule import Rule
from ..base import BaseHandler


class WebsiteHandler(BaseHandler):
    def __init__(self) -> None:
        super().__init__()

    def handle(self, message: Dict, rule: Rule, **kwargs):
        # check action type in here, maybe get from kwargs
        action_type = kwargs.get('action_type', 'customer_send_message')
        if action_type == 'customer_send_message':
            return self.handle_action_customer_send_message(message, rule, **kwargs)
        elif action_type == 'salesman_send_message':
            return self.handle_action_salesman_send_message(message, rule, **kwargs)
        else:
            print('Unknown action type to handle')

    def create_room(self, room_name: str = str(uuid4())):
        print(f'Creating room {room_name}...')

    def notify_salesman(self, salesman_id: str = str(uuid4())):
        print(f'Notifying salesman {salesman_id}...')

    def notify_customer(self, customer_id: str = str(uuid4())):
        print(f'Notifying customer {customer_id}...')

    # each actions will be handled in here
    # nên tách ra thành nhiều class nhỏ hơn để quản lý
    def handle_action_customer_send_message(self, message: Dict, rule: Rule, **kwargs):
        print(f'Handling action customer send message... {message=}, {rule=}, {kwargs=}')
        self.create_room()
        self.notify_customer

    def handle_action_salesman_send_message(self, message: Dict, rule: Rule, **kwargs):
        print(f'Handling action salesman send message... {message=}, {rule=}, {kwargs=}')
        self.create_room()
        self.notify_salesman()
