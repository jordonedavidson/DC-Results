import random


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
        5: 3, 4: 4, 3: 5, 2: 7, 1: 9, 0: 11,
        -1: 13, -2: 15, -3: 18, -4: 21, -5: 24, -6: 28,
        -7: 32, -8: 36,  -9: 40
    }

    RESULT_TABLE = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 5, 4, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [10, 8, 6, 4, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [12, 10, 9, 7, 6, 4, 3, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [15, 12, 11, 9, 8, 7, 5, 3, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [18, 14, 13, 11, 10, 9, 8, 6, 4, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [21, 18, 17, 16, 14, 12, 10, 8, 6, 4, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [24, 21, 20, 19, 17, 15, 13, 11, 9, 7, 5, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [27, 24, 23, 22, 20, 18, 16, 14, 12, 10, 8, 6, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [30, 27, 26, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [35, 30, 29, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [40, 35, 34, 33, 31, 29, 27, 25, 23, 21, 19, 17,
            14, 12, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [45, 40, 38, 36, 34, 32, 30, 38, 36, 24, 22, 20, 18,
            16, 13, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [50, 45, 43, 41, 40, 38, 36, 34, 31, 28, 26, 24,
            22, 20, 17, 14, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [55, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30,
            27, 24, 21, 18, 15, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [60, 55, 53, 51, 49, 47, 45, 43, 41, 39, 36, 33,
            30, 27, 24, 21, 18, 15, 13, 0, 0, 0, 0, 0, 0, 0, 0],
        [65, 60, 58, 56, 54, 52, 50, 48, 46, 44, 41, 38, 35,
            32, 29, 26, 23, 20, 18, 13, 0, 0, 0, 0, 0, 0, 0],
        [70, 65, 63, 61, 59, 57, 55, 53, 51, 49, 46, 43, 40,
            37, 34, 31, 28, 25, 23, 18, 14, 0, 0, 0, 0, 0, 0],
        [75, 70, 68, 66, 64, 62, 60, 58, 56, 54, 51, 48, 45,
            42, 39, 36, 33, 30, 28, 23, 19, 15, 0, 0, 0, 0, 0],
        [80, 75, 73, 71, 69, 67, 65, 63, 61, 59, 56, 53, 50,
            47, 44, 41, 38, 35, 33, 28, 24, 20, 16, 0, 0, 0, 0],
        [85, 80, 78, 76, 74, 72, 70, 68, 66, 64, 61, 58, 55, 52,
            49, 46, 43, 40, 38, 33, 29, 25, 21, 17, 0, 0, 0],
        [90, 85, 83, 81, 79, 77, 75, 73, 71, 69, 66, 63, 60, 57,
            54, 51, 48, 45, 43, 38, 34, 30, 26, 22, 18, 0, 0],
        [95, 90, 88, 86, 84, 82, 80, 78, 76, 74, 71, 68, 65, 62,
            59, 56, 53, 50, 48, 43, 39, 35, 31, 27, 23, 19, 0],
        [100, 95, 93, 91, 89, 87, 85, 83, 81, 79, 76, 73, 70, 67,
            64, 61, 58, 55, 53, 48, 44, 40, 36, 32, 28, 24, 20]
    ]

    column_zero_cases = [
        {1: 6},
        {2: 5, 1: 9},
        {3: 4, 2: 7, 1: 9},
    ]

    def get_to_hit(self, acting: int, opposing: int):
        to_hit = 11
        acting_column = self._get_column(acting)
        opposing_column = self._get_column(opposing)

        if opposing_column == 0:
            match acting_column:
                case 1:
                    to_hit = 6
                case 2:
                    to_hit = 5
                case 3:
                    to_hit = 4
                case 4:
                    to_hit = 4
                case _:
                    to_hit = 3

        else:
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
        # print(f"To Hit: {to_hit}, Rolled: {rolled}")
        success = rolled >= to_hit
        column_shifts = self._get_column_shifts(rolled, to_hit)
        # print(f"Success: {success}, Column Shifts: {column_shifts}")
        return {
            "success": success,
            "column_shifts": column_shifts
        }

    def roll_dice(self, current_total: int = 0):
        die_1 = random.randint(1, 10)
        die_2 = random.randint(1, 10)
        current_total = current_total + die_1 + die_2

        if (die_1 == 1 and die_2 == 1):
            current_total = 2

        return {
            "die_1": die_1,
            "die_2": die_2,
            "current_total": current_total
        }

    def get_result(self, effect_value: int, resistance_value: int, column_shifts: int):
        effect_column = self._get_column(effect_value)
        resistance_column = self._get_column(resistance_value) - column_shifts
        raps = 0

        if resistance_column == 0:
            raps = effect_value
        elif resistance_column < 0:
            raps = effect_value + abs(resistance_column)
        else:
            raps = self.RESULT_TABLE[effect_column][resistance_column]

        return raps

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
        if rolled <= to_hit:
            return 0

        # There are 3 cases that need to be handled for the 0th Opposing Value column
        # for:
        #   AV [1,2], VALUES["1"] = 6
        #   AV [3,4], VALUES["2"] = 5, VALUES["1"] = 9
        #   AV [5,6], VALUES["3"] = 9, VALUES["2"] = 7, VALUES["1"] = 4
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
        return abs((temp_column_key+1) - column_key)
