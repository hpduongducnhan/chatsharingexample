class BaseHandler:
    def __init__(self) -> None:
        pass

    def handle(self):
        raise NotImplementedError

    def handle_message(self, *args, **kwargs):
        try:
            return self.handle(*args, **kwargs)
        except Exception as e:
            print(e)
            return None
