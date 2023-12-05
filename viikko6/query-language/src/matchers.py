from player import Player
from abc import abstractmethod


class Matcher:
    @abstractmethod
    def test(self, player: Player) -> bool:
        pass


class And(Matcher):
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn(Matcher):
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast(Matcher):
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class All(Matcher):
    def test(self, player: Player) -> bool:
        return True


class Not(Matcher):
    def __init__(self, matcher: Matcher) -> None:
        self.__matcher: Matcher = matcher

    def test(self, player: Player) -> bool:
        return not self.__matcher.test(player)


class HasFewerThan(Matcher):
    def __init__(self, value: int, attr) -> None:
        self.__value: int = value
        self.__attr: str = attr
        self.__matcher: Matcher = Not(HasAtLeast(self.__value, self.__attr))

    def test(self, player: Player) -> bool:
        return self.__matcher.test(player)
