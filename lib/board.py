class Board():
    def format_board(self, player):
        rows = []
        rows_nums = "0123456789"
        for row, i in zip(range(1, player.rows + 1),rows_nums):
            row_cells = []
            for col in range(1, player.cols + 1):
                if player.ship_at(row, col):
                    row_cells.append(" S")
                else:
                    row_cells.append(" ·")
            rows.append(i + " │" + "".join(row_cells) + " │")
        rows.insert(0, "    0 1 2 3 4 5 6 7 8 9  ")
        rows.insert(1,  "  ┌─────────────────────┐")
        rows.append("  └─────────────────────┘")
        return "\n".join(rows)
    
    def format_enemy_board(self, player):
        rows = []
        rows_nums = "0123456789"
        for row, i in zip(range(1, player.rows + 1),rows_nums):
            row_cells = []
            for col in range(1, player.cols + 1):
                if (row, col) in player.hits:
                    if player.sunk_ship_at(row, col):
                        row_cells.append(" #")
                    else:
                        row_cells.append(" X")
                elif (row, col) in player.misses:
                    row_cells.append(" O")
                else:
                    row_cells.append(" ·")
            rows.append(i + " │" + "".join(row_cells) + " │")
        rows.insert(0, "    0 1 2 3 4 5 6 7 8 9  ")
        rows.insert(1,  "  ┌─────────────────────┐")
        rows.append("  └─────────────────────┘")
        return "\n".join(rows)
