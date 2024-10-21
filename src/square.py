import numpy as np


row_notation = "12345678"
column_notation = "abcdefgh"


class Square:
    def __init__(self, row_number: int, column_number: int) -> None:
        if row_number > 8 or row_number < 1 or column_number > 8 or column_number < 1:
            raise Exception("Not a valid piece")
        self.row_number = row_number
        self.column_number = column_number
        if (row_number + column_number) % 2 == 0:
            self.square_color = "BLACK"
        else:
            self.square_color = "WHITE"
        self.notation = (
            row_notation[row_number - 1] + column_notation[column_number - 1]
        )
