from statistics import Statistics

from matchers import And, HasAtLeast, PlaysIn
from player_reader import PlayerReader


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(HasAtLeast(5, "goals"), HasAtLeast(20, "assists"), PlaysIn("PHI"))

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
