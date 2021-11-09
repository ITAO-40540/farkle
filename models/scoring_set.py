class ScoringSet:
    def __init__(self, dice):
        self._dice = dice
        self._dice_as_integers = []

    def points(self):
        self.__dice_to_integers()
        value_counts = self.__value_counts(self._dice_as_integers)

        if self._dice_as_integers == [1, 2, 3, 4, 5, 6]:
            return 3000
        elif len(value_counts.keys()) == 3 and list(value_counts.values()) == [2, 2, 2]:
            return 1500
        else:
            return self.__extract_points(value_counts)

    def len(self):
        return len(self._dice)

    def __extract_points(self, value_counts):
        point_total = 0

        try:
            index_of_threes = list(value_counts.values()).index(3)
            value_with_threes = list(value_counts.keys())[index_of_threes]
            value_counts.pop(value_with_threes)
            point_total += self.__points_from_threes(value_with_threes)
        except:
            index_of_threes = None
        try:
            index_of_fours = list(value_counts.values()).index(4)
            value_with_fours = list(value_counts.keys())[index_of_fours]
            value_counts.pop(value_with_fours)
            point_total += self.__points_from_fours(value_with_fours)
        except:
            # raise
            index_of_fours = None

        point_total += self.__points_from_singles(value_counts)

        return point_total

    def __points_from_threes(self, value):
        if value == 1:
            return 1000
        else:
            return value * 100

    def __points_from_fours(self, value):
        total_points = self.__points_from_threes(value)
        total_points += self.__points_from_singles({value: 1})
        return total_points

    def __points_from_singles(self, value_counts):
        point_total = 0
        for die_val in value_counts.keys():
            die_count = value_counts[die_val]
            for v in range(die_count):
                if die_val == 1:
                    point_total += 100
                elif die_val == 5:
                    point_total += 50

        return point_total

    def __value_counts(self, dice_values):
        value_counts = {}
        for i in dice_values:
            if i in value_counts:
                value_counts[i] += 1
            else:
                value_counts[i] = 1
        return value_counts

    def __extract_points_from_threes(self, dice_values):
        if dice_values == [1, 1, 1]:
            return 1000
        elif dice_values == [5, 5, 5]:
            return 500
        elif dice_values == [4, 4, 4]:
            return 400
        elif dice_values == [3, 3, 3]:
            return 300
        elif dice_values == [2, 2, 2]:
            return 200
        else:
            return 0

    def __dice_to_integers(self):
        self._dice_as_integers = []
        for die in self._dice:
            self._dice_as_integers.append(int(die.current_value()))
        self._dice_as_integers.sort()
