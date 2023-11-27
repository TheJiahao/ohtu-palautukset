from player import Player


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = [Player(player1_name, 0), Player(player2_name, 0)]
        self.scores = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def won_point(self, player_name):
        for player in self.players:
            if player.name == player_name:
                player.points += 1

    def get_score(self):
        result = ""

        player1 = self.players[0]
        player2 = self.players[1]

        if player1.points == player2.points:
            result = self.__handle_even(player1.points)

        elif player1.points >= 4 or player2.points >= 4:
            if player1.points > player2.points:
                result = self.__handle_advantage(player1, player2)
            else:
                result = self.__handle_advantage(player2, player1)
        else:
            result = f"{self.scores[player1.points]}-{self.scores[player2.points]}"

        return result

    def __handle_even(self, points):
        if points >= 3:
            return "Deuce"

        return f"{self.scores[points]}-All"

    def __handle_advantage(
        self, player_with_advantage: Player, player_without_advantage: Player
    ) -> str:
        difference = player_with_advantage.points - player_without_advantage.points

        if difference == 1:
            return f"Advantage {player_with_advantage.name}"

        return f"Win for {player_with_advantage.name}"
