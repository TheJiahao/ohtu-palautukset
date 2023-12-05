from matchers import *


class QueryBuilder:
    def __init__(self, matcher: Matcher = All()) -> None:
        self.__matcher: Matcher = matcher

    def playsIn(self, team: str) -> "QueryBuilder":
        return QueryBuilder(And(self.__matcher, PlaysIn(team)))

    def hasAtLeast(self, value: int, attr: str) -> "QueryBuilder":
        return QueryBuilder(And(self.__matcher, HasAtLeast(value, attr)))

    def hasFewerThan(self, value: int, attr: str) -> "QueryBuilder":
        return QueryBuilder(And(self.__matcher, HasFewerThan(value, attr)))

    def oneOf(self, *matchers:Matcher):
        return QueryBuilder(Or(*matchers))

    def build(self) -> Matcher:
        return self.__matcher
