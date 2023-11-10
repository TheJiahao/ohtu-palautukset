from player_reader import PlayerReader


class PlayerStats:
    def __init__(self, reader) -> None:
        self._reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self._reader.get_players()

        return sorted(
            filter(lambda player: player.nationality == nationality, players),
            key=lambda player: player.points,
            reverse=True,
        )
