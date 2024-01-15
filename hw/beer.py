from __init__ import time_decorator
class Beer:
    @time_decorator
    def __init__(self, title=None, production_date=None) -> None:
        self.title = title
        self.production_date = production_date
