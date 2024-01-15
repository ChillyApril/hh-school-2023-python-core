from __init__ import time_decorator, time_decorator_with_return
class Market:
    @time_decorator
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = wines
        if wines == None:
            self.wines = []
        self.beers = beers
        if beers == None:
            self.beers = []
        self.titles = set([wine.title for wine in self.wines]) | set([beer.title for beer in self.beers])
    @time_decorator_with_return
    def has_drink_with_title(self, title=None) -> bool:
        return (title in self.titles)
    @time_decorator_with_return
    def get_drinks_sorted_by_title(self) -> list:
        return list(sorted(self.wines + self.beers, key = (lambda x: x.title)))
    @time_decorator_with_return
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        return [drink for drink in (self.wines + self.beers) if from_date < drink.production_date < to_date]
