import time


class Rule:
    def __init__(self) -> None:
        pass


class RuleLoader:
    def __init__(self) -> None:
        pass

    def load(self):
        print('Loading rules...')
        time.sleep(1)
        print('Rules loaded!')

    def reload(self):
        print('Reloading rules...')
        time.sleep(1)
        self.load()
        print('Rules reloaded!')

    def get_selected_rule(self) -> Rule:
        return Rule()
