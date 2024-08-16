class ShipPlacement:
    def __init__(self, length, orientation, row, col):
        self.length = length
        self.orientation = orientation
        self.row = row
        self.col = col
        self.ship_rows = self._get_rows()
        self.ship_columns = self._get_columns()

    def covers(self, row, col):
        if self.orientation == "vertical":
            if self.col != col:
                return False
            return self.row <= row < self.row + self.length
        else:
            if self.row != row:
                return False
            return self.col <= col < self.col + self.length
        
    def _get_rows(self):
        rows = [self.row]
        while len(rows) < self.length:
            if self.orientation == "vertical":
                rows.append(rows[-1] + 1)
            else:
                rows.append(rows[-1])
        return rows
    
    def _get_columns(self):
        columns = [self.col]
        while len(columns) < self.length:
            if self.orientation == "vertical":
                columns.append(columns[-1])
            else:
                columns.append(columns[-1] + 1)
        return columns


    def __repr__(self):
        return f"ShipPlacement(length={self.length}, orientation={self.orientation}, row={self.row}, col={self.col})"
