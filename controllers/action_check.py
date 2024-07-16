class ActionCheck():
    """
    Handles the calculation of the to hit and column shifts for an attack
    """

    VALUES = [
        [0, 0], [1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 15],
        [16, 18], [19, 21], [22, 24], [25, 27], [28, 30], [31, 35], [36, 40],
        [41, 45], [46, 50], [51, 55], [56, 60], [61, 65], [66, 70], [71, 75],
        [76, 80], [81, 85], [86, 90], [91, 95], [96, 100]
    ]

    # TO_HIT dictionary maps column differences to number to hit
    # Column differences Greater Than 5 are always 3
    # Column differences Less Than -9 are 40 + (column difference - 9)*5
    TO_HIT = {
        5: 3,
        4: 4,
        3: 5,
        2: 7,
        1: 9,
        0: 11,
        -1: 13,
        -2: 15,
        -3: 18,
        -4: 21,
        -5: 24,
        -6: 28,
        -7: 32,
        -8: 36,
        -9: 40
    }

    def get_to_hit(self, acting: int, opposing: int):
        to_hit = 11
        acting_column = self._get_column(acting)
        opposing_column = self._get_column(opposing)

        to_hit_index = acting_column - opposing_column
        # print(f"To hit index is: {to_hit_index}")
        if to_hit_index > 5:
            to_hit = self.TO_HIT[5]
        elif to_hit_index < -9:
            to_hit = self.TO_HIT[-9] + (to_hit_index - 9) * 5
        else:
            to_hit = self.TO_HIT[to_hit_index]

        return to_hit

    def attack_result(self, to_hit: int, rolled: int):
        """
        Determines if an attack succeeds and, if so, how many column shifts result
        """
        success = rolled >= to_hit
        column_shifts = self._get_column_shifts(rolled, to_hit)

        return {
            "success": success,
            "column_shifts": column_shifts
        }

    def _get_column(self, value: int):
        if value == 0:
            return 0

        column = 0
        for values in self.VALUES:
            # print(
            #     f"checking {value} against: {values}: range({values[0]}, {values[1] +1})")
            # print(f"Index of {values} is: {VALUES.index(values)}")
            if value in range(values[0], values[1] + 1):
                column = self.VALUES.index(values)

        # print(f"for value: {value}, Column number is: {column}")
        return column

    def _get_column_shifts(self, rolled: int, to_hit: int):
        if rolled < to_hit:
            return 0

        # First get the key from the dictionary for the to_hit value
        column_key = list(self.TO_HIT.keys())[
            list(self.TO_HIT.values()).index(to_hit)]
        temp_column_key = column_key
        # print(f"Column key is: {column_key}")
        check_value = self.TO_HIT[temp_column_key]
        while check_value <= rolled:
            temp_column_key -= 1
            check_value = self.TO_HIT[temp_column_key]

        # print(f"Column key is: {temp_column_key}")
        return abs(temp_column_key - column_key)
