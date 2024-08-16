from lib.player import Player
class Players():
    def __init__(self) -> None:
        self.players = [Player(0), Player(1)]

    def check_if_hit_or_miss(self, player_number, row, col):
        player = next(player for player in self.players if player.number == player_number)
        opponent = next(player for player in self.players if player.number != player_number)
        if opponent.ship_at(row, col):
            player.hits.append((row, col))
            return True
        else:
            player.misses.append((row, col))
            return False
        
    def check_if_shot_sinks_opponents_ship(self, player_number):
        player = self.players[player_number]
        opponent = self.players[abs(player_number-1)]
        for ship in opponent.ships_remaining:
            counter = 0
            rows_cols = list(map(lambda x, y: (x, y), ship.ship_rows, ship.ship_columns))
            for hit in player.hits:
                if hit in rows_cols:
                    counter += 1
            if counter == ship.length:
                player.ships_sunk.append(ship)
                opponent.ships_remaining.remove(ship)
                return True
        return False



