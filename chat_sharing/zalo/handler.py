from typing import Dict
from ..rule import Rule
from ..base import BaseHandler


class ZaloHandler(BaseHandler):
    def __init__(self) -> None:
        super().__init__()

    def handle(self, message: Dict, rule: Rule, **kwargs):
        print(f'Handling message from website... {message=}, {rule=}, {kwargs=}')
