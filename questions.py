# Enable the generation of random numbers
import random
# Import maths module
import math
# Import module to allow number to be converted to words
from num2words import num2words
# Import method to return all permutations of a list
from itertools import permutations
# Import module to generate Roman numerals
from rom import rom_generate


def random_boolean():
    return random.randint(0, 1)


def question_text_objective_n1(direction, highest_value, multiple):
    if direction:
        return "What is the next number in the sequence?\n\n{}, {}, {}... ". \
            format(highest_value, highest_value - multiple, highest_value - 2 * multiple)
    else:
        return "What is the next number in the sequence?\n\n{}, {}, {}... ". \
            format(highest_value - 2 * multiple, highest_value - multiple, highest_value)


class BasicN1:
    def __init__(self, year_group, multiples):
        self.year_group = year_group
        self.multiples = multiples
        self.direction = random_boolean()
        self.multiple = self.multiple()
        self.highest_value = self.highest_value()
        self.correct_answer = self.correct_answer()
        self.question_text = self.question_text()

    def multiple(self):
        return self.multiples[random.randint(0, len(self.multiples) - 1)]

    def highest_value(self):
        multiplier = random.randint(3, 10)
        return self.multiple * multiplier

    def correct_answer(self):
        if self.direction:
            return self.highest_value - 3 * self.multiple
        else:
            return self.highest_value + self.multiple

    def question_text(self):
        return question_text_objective_n1(self.direction, self.highest_value, self.multiple)


class Objective1N1:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        basic = BasicN1(1, (2, 5, 10))
        self.direction = basic.direction
        self.multiple = basic.multiple
        self.highest_value = basic.highest_value
        self.correct_answer = basic.correct_answer
        self.question_text = basic.question_text


class Objective2N1:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        self.question_type = random_boolean()
        self.direction = random_boolean()
        self.multiples = (2, 3, 5)
        self.multiple = self.multiple()
        self.highest_value = self.highest_value()
        self.correct_answer = self.correct_answer()
        self.question_text = self.question_text()

    def multiple(self):
        if self.question_type:
            return self.multiples[random.randint(0, len(self.multiples) - 1)]
        else:
            return 10

    def highest_value(self):
        if self.question_type:
            return random.randrange(self.multiple * 3, self.multiple * 12, self.multiple)
        else:
            highest_value = random.randint(31, 99)
            while highest_value % 10 == 0:
                highest_value = random.randint(31, 99)
            return highest_value

    def correct_answer(self):
        if self.direction:
            return self.highest_value - 3 * self.multiple
        else:
            return self.highest_value + self.multiple

    def question_text(self):
        return question_text_objective_n1(self.direction, self.highest_value, self.multiple)


class Objective3N1:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        basic = BasicN1(3, (4, 8, 50, 100))
        self.correct_answer = basic.correct_answer
        self.question_text = basic.question_text


class Objective4N1:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        basic = BasicN1(4, (6, 7, 9, 25, 1000))
        self.correct_answer = basic.correct_answer
        self.question_text = basic.question_text


class Objective5N1:
    def __init__(self):
        self.multi_plot = False

        self.direction = random_boolean()
        self.power = random.randint(1, 5)
        self.multiple = self.multiple()
        self.highest_value = self.highest_value()
        self.correct_answer = self.correct_answer()
        self.question_text = self.question_text()

    def multiple(self):
        return 10 ** self.power

    def highest_value(self):
        highest_value = random.randint(200000, 800000)
        while highest_value % 10 == 0 or highest_value % 100 < 10\
                or highest_value % 1000 < 100 or highest_value % 10000 < 1000:
            highest_value = random.randint(200000, 800000)
        return highest_value

    def correct_answer(self):
        if self.direction:
            return self.highest_value - 3 * self.multiple
        else:
            return self.highest_value + self.multiple

    def question_text(self):
        return question_text_objective_n1(self.direction, self.highest_value, self.multiple)


class ReadNumbers:
    def __init__(self, lower_limit, upper_limit):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        # Chooses a random integer between lower limit and upper limit
        self.correct_answer = random.randint(lower_limit, self.upper_limit)
        # Allows user to enter their answer
        self.question_text = "Write {} in numerals. ".format(num2words(self.correct_answer))


class WriteNumbers:
    def __init__(self, lower_limit, upper_limit):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        # Chooses a random integer between lower limit and upper limit
        self.answer_in_numerals = random.randint(lower_limit, self.upper_limit)
        self.correct_answer = num2words(self.answer_in_numerals)
        # Allows user to enter their answer
        self.question_text = "Write {} in words. ".format(self.answer_in_numerals)


class Objective1N2a:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        # Creates a read numbers object with an upper limit of 100
        read_question = ReadNumbers(1, 100)
        self.correct_answer = read_question.correct_answer
        self.question_text = read_question.question_text


class MoreLessThan:
    def __init__(self, lower_limit, upper_limit, amount):
        self.amount = amount
        self.direction = random_boolean()
        self.direction_text = self.direction_text()
        self.original_number = random.randint(lower_limit, upper_limit)
        self.correct_answer = self.correct_answer()
        self.question_text = self.question_text()

    def direction_text(self):
        if self.direction:
            return "more"
        else:
            return "less"

    def correct_answer(self):
        if self.direction:
            return self.original_number + self.amount
        else:
            return self.original_number - self.amount

    def question_text(self):
        return "What is {} {} than {}? ".format(self.amount, self.direction_text, self.original_number)


class Objective1N2b:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        question = MoreLessThan(1, 100, 1)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class Objective1N2c:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        self.question_type = random_boolean()
        # Creates a read numbers object with a lower limit of 1 and a upper limit of 20
        if self.question_type:
            read_question = ReadNumbers(1, 20)
            self.correct_answer = read_question.correct_answer
            self.question_text = read_question.question_text
        # Creates a write numbers object with a lower limit of 1 and a upper limit of 20
        else:
            write_question = WriteNumbers(1, 20)
            self.correct_answer = write_question.correct_answer
            self.question_text = write_question.question_text


class Objective2N2a:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        self.question_type = random_boolean()
        # Creates a read numbers object with a lower limit of 20 and a upper limit of 100
        if self.question_type:
            read_question = ReadNumbers(20, 100)
            self.correct_answer = read_question.correct_answer
            self.question_text = read_question.question_text
        # Creates a write numbers object with a lower limit of 20 and a upper limit of 100
        else:
            write_question = WriteNumbers(20, 100)
            self.correct_answer = write_question.correct_answer
            self.question_text = write_question.question_text


class CompareNumbers:
    def __init__(self, number_of_digits):
        self.number_of_digits = number_of_digits
        self.digits = self.set_digits()
        self.trimmed_digits = self.trim_digits()
        self.first_number = self.create_first_number()
        self.second_number = self.create_second_number()
        self.correct_answer = self.correct_answer()
        self.question_text = self.question_text()

    def set_digits(self):
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        while b == a:
            b = random.randint(1, 9)
        c = random.randint(1, 9)
        while c == b:
            c = random.randint(1, 9)
        d = random.randint(1, 9)
        while d == c:
            d = random.randint(1, 9)
        e = random.randint(1, 9)
        while e == d:
            e = random.randint(1, 9)
        f = random.randint(1, 9)
        while f == e:
            f = random.randint(1, 9)
        g = random.randint(1, 9)
        while g == f:
            g = random.randint(1, 9)
        return [a, b, c, d, e, f, g]

    def trim_digits(self):
        return self.digits[:self.number_of_digits]

    def create_first_number(self):
        first_number = ""
        for digit in self.trimmed_digits:
            first_number += str(digit)
        return first_number

    def create_second_number(self):
        random_number = self.random_second_number()
        while random_number == self.first_number:
            random_number = self.random_second_number()
        return random_number

    def random_second_number(self):
        if self.number_of_digits in (2, 3):
            trailing_digits = self.trimmed_digits
            list_options = list(permutations(trailing_digits, len(self.trimmed_digits)))
            choose_option = random.randint(0, self.number_of_digits - 1)
            list(list_options[choose_option])
            full_digit_list = list(list_options[choose_option])
        else:
            trailing_digits = self.trimmed_digits[1:]
            list_options = list(permutations(trailing_digits, len(self.trimmed_digits) - 1))
            choose_option = random.randint(0, self.number_of_digits - 2)
            trailing_digits = list(list_options[choose_option])
            full_digit_list = self.trimmed_digits[:1] + trailing_digits
        second_number = ""
        for digit in full_digit_list:
            second_number += str(digit)
        return second_number

    def correct_answer(self):
        if self.first_number == self.second_number:
            correct_answer = "="
        elif self.first_number > self.second_number:
            correct_answer = ">"
        elif self.first_number < self.second_number:
            correct_answer = "<"
        else:
            raise ValueError
        return correct_answer

    def question_text(self):
        return "Use <, > or = to compare the numbers shown\n{} □ {} ".format(self.first_number, self.second_number)


class Objective2N2b:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        question = CompareNumbers(2)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class Objective3N2a:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        # Selects a question type at random
        self.question_type = random.randint(1, 3)
        # Creates a comparison object with an upper limit of 1000
        if self.question_type == 1:
            question = CompareNumbers(3)
            self.correct_answer = question.correct_answer
            self.question_text = question.question_text
        # Creates a read numbers object with a lower limit of 100 and a upper limit of 1000
        elif self.question_type == 2:
            read_question = ReadNumbers(100, 1000)
            self.correct_answer = read_question.correct_answer
            self.question_text = read_question.question_text
        # Creates a write numbers object with a lower limit of 100 and a upper limit of 1000
        else:
            write_question = WriteNumbers(100, 1000)
            self.correct_answer = write_question.correct_answer
            self.question_text = write_question.question_text


class Objective3N2b:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        # Selects a question type at random
        self.question_type = random_boolean()
        if self.question_type:
            question = MoreLessThan(80, 1000, 10)
        else:
            question = MoreLessThan(200, 10000, 100)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class Objective4N2a:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        question = CompareNumbers(6)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class Objective4N2b:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        question = MoreLessThan(500, 1000000, 1000)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class Objective5N2:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        # Selects a question type at random
        self.question_type = random.randint(1, 3)
        # Creates a comparison object with an upper limit of 1000000
        if self.question_type == 1:
            question = CompareNumbers(6)
            self.correct_answer = question.correct_answer
            self.question_text = question.question_text
        # Creates a read numbers object with a lower limit of 10,000 and a upper limit of 1,000,000
        elif self.question_type == 2:
            read_question = ReadNumbers(10000, 1000000)
            self.correct_answer = read_question.correct_answer
            self.question_text = read_question.question_text
        # Creates a write numbers object with a lower limit of 10,000 and a upper limit of 1,000,000
        else:
            write_question = WriteNumbers(10000, 1000000)
            self.correct_answer = write_question.correct_answer
            self.question_text = write_question.question_text


class Objective6N2:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        # Selects a question type at random
        self.question_type = random.randint(1, 3)
        # Creates a comparison object with an upper limit of 1000000
        if self.question_type == 1:
            question = CompareNumbers(7)
            self.correct_answer = question.correct_answer
            self.question_text = question.question_text
        # Creates a read numbers object with a lower limit of 100,000 and a upper limit of 10,000,000
        elif self.question_type == 2:
            read_question = ReadNumbers(100000, 10000000)
            self.correct_answer = read_question.correct_answer
            self.question_text = read_question.question_text
        # Creates a write numbers object with a lower limit of 100,000 and a upper limit of 10,000,000
        else:
            write_question = WriteNumbers(100000, 10000000)
            self.correct_answer = write_question.correct_answer
            self.question_text = write_question.question_text


class PlaceValue:
    def __init__(self, digits):
        self.digits = digits
        self.minimum_value = self.minimum_value()
        self.maximum_value = self.maximum_value()
        self.number = random.randint(self.minimum_value, self.maximum_value)
        self.column = random.randint(0, self.digits // 2)
        self.correct_answer = self.correct_answer()
        self.question_text = self.question_text()

    def minimum_value(self):
        return 10 ** (self.digits - 1)

    def maximum_value(self):
        return 10 ** self.digits

    def correct_answer(self):
        number_as_list = [int(x) for x in str(self.number)]
        return number_as_list[self.column] * 10 ** (len(number_as_list) - self.column - 1)

    def question_text(self):
        number_as_list = [int(x) for x in str(self.number)]
        number_as_list[self.column] = "({})".format(number_as_list[self.column])
        underlined_number = ""
        for digit in number_as_list:
            underlined_number += str(digit)
        return "Write the value in numbers of the digit in the brackets\n\n{}".format(underlined_number)


class Objective2N3:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        question = PlaceValue(2)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class Objective3N3:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        question = PlaceValue(3)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class Objective4N3a:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        question = PlaceValue(4)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class RomanNumerals:
    def __init__(self, minimum, maximum):
        self.number = random.randint(minimum, maximum)
        self.correct_answer = self.number
        self.question_text = self.question_text()

    def question_text(self):
        return "The number {} is written in Roman Numerals. Write it as a number.".format(rom_generate(self.number))


class Objective4N3b:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        question = RomanNumerals(1, 100)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class Objective5N3a:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        question = PlaceValue(6)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class Objective5N3b:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        question = RomanNumerals(101, 2100)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class Objective6N3:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        question = PlaceValue(7)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class Objective1N4:
    def __init__(self):
        self.multi_plot = True
        self.place_text = False
        self.total_images = 1

        self.total = self.generate_total()
        number = self.generate_number()
        question = AdditionOrSubtraction(self.total, number)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text

        self.correct_answer = question.correct_answer
        self.question_text = question.question_text

        self.image_1_path = "C:/Users/Michael/Pictures/Saved Pictures/number_line_to_10.jpg"
        self.image_1_width = 600
        self.image_1_height = 150
        self.image_1_frequency = 1
        self.image_1_x_coord = [960 - self.image_1_width // 2]
        self.image_1_y_coord = [300]

        self.question_label_y = 450

    def generate_total(self):
        return random.randint(3, 10)

    def generate_number(self):
        return random.randint(0, self.total)


class Objective2N4:
    def __init__(self):
        self.multi_plot = True
        self.place_text = False
        self.total_images = 2

        self.correct_answer = self.generate_answer()
        self.question_text = "What number is represented?"

        self.image_1_path = "C:/Users/Michael/Pictures/Saved Pictures/tens_block.png"
        self.image_1_width = 250
        self.image_1_height = 250
        self.image_1_frequency = self.set_image_1_frequency()
        self.image_1_x_coord = [800 - (40 * x) for x in range(9)]
        self.image_1_y_coord = [255 for x in range(9)]

        self.image_2_path = "C:/Users/Michael/Pictures/Saved Pictures/ones_block.png"
        self.image_2_width = 250
        self.image_2_height = 250
        self.image_2_frequency = self.set_image_2_frequency()
        self.image_2_x_coord = (875, 940, 900, 915, 840, 945, 860, 855, 960)
        self.image_2_y_coord = (265, 250, 220, 290, 235, 205, 310, 190, 295)

        self.question_label_y = 450

    def generate_answer(self):
        return random.randint(20, 99)

    def set_image_1_frequency(self):
        return self.correct_answer // 10

    def set_image_2_frequency(self):
        return self.correct_answer % 10


class Objective3N4:
    def __init__(self):
        self.multi_plot = True
        self.place_text = True
        self.total_images = 1
        self.total_text = 4

        self.question_text = "What number is missing?"
        self.correct_answer = self.generate_total()

        self.total = self.generate_total()
        self.hundreds = self.set_text_2()
        self.tens = self.set_text_3()
        self.ones = self.set_text_4()

        self.text_labels = 4

        all_digits = (self.total, self.hundreds, self.tens, self.ones)
        selection = self.choose_selection()

        self.correct_answer = all_digits[selection]

        if selection == 0:
            self.total = "?"
        elif selection == 1:
            self.hundreds = "?"
        elif selection == 2:
            self.tens = "?"
        else:
            self.ones = "?"

        self.image_1_path = "C:/Users/Michael/Pictures/Saved Pictures/part_whole_3_digits.png"
        self.image_1_width = 300
        self.image_1_height = 225
        self.image_1_frequency = 1
        self.image_1_x_coord = [810]
        self.image_1_y_coord = [280]

        self.text_1_text = str(self.total)
        self.text_1_width = 50
        self.text_1_height = 50
        self.text_1_x_coord = 935
        self.text_1_y_coord = 300

        self.text_2_text = str(self.hundreds)
        self.text_2_width = 50
        self.text_2_height = 50
        self.text_2_x_coord = 828
        self.text_2_y_coord = 435

        self.text_3_text = str(self.tens)
        self.text_3_width = 50
        self.text_3_height = 50
        self.text_3_x_coord = 935
        self.text_3_y_coord = 435

        self.text_4_text = str(self.ones)
        self.text_4_width = 50
        self.text_4_height = 50
        self.text_4_x_coord = 1041
        self.text_4_y_coord = 435

        self.question_label_y = 470

    def generate_total(self):
        return random.randint(111, 999)

    def set_text_2(self):
        return 100 * (self.total // 100)

    def set_text_3(self):
        return 10 * ((self.total - self.hundreds) // 10)

    def set_text_4(self):
        return self.total - self.hundreds - self.tens

    def set_text_5(self):
        return self.total - self.hundreds - self.tens

    def choose_selection(self):
        return random.randint(0, 3)


class Objective4N4a:
    def __init__(self):
        self.multi_plot = True
        self.place_text = True
        self.total_images = 1
        self.total_text = 5

        self.question_text = "What number is missing?"
        self.correct_answer = self.generate_total()

        self.total = self.generate_total()
        self.thousands = self.set_text_2()
        self.hundreds = self.set_text_3()
        self.tens = self.set_text_4()
        self.ones = self.set_text_5()

        self.text_labels = 4

        all_digits = (self.total, self.thousands, self.hundreds, self.tens, self.ones)
        selection = self.choose_selection()

        self.correct_answer = all_digits[selection]

        if selection == 0:
            self.total = "?"
        elif selection == 1:
            self.thousands = "?"
        elif selection == 2:
            self.hundreds = "?"
        elif selection == 3:
            self.tens = "?"
        else:
            self.ones = "?"

        self.image_1_path = "C:/Users/Michael/Pictures/Saved Pictures/part_whole_4_digits.png"
        self.image_1_width = 400
        self.image_1_height = 225
        self.image_1_frequency = 1
        self.image_1_x_coord = [760]
        self.image_1_y_coord = [280]

        self.text_1_text = str(self.total)
        self.text_1_width = 80
        self.text_1_height = 50
        self.text_1_x_coord = 919
        self.text_1_y_coord = 300

        self.text_2_text = str(self.thousands)
        self.text_2_width = 80
        self.text_2_height = 50
        self.text_2_x_coord = 763
        self.text_2_y_coord = 435

        self.text_3_text = str(self.hundreds)
        self.text_3_width = 80
        self.text_3_height = 50
        self.text_3_x_coord = 868
        self.text_3_y_coord = 435

        self.text_4_text = str(self.tens)
        self.text_4_width = 80
        self.text_4_height = 50
        self.text_4_x_coord = 973
        self.text_4_y_coord = 435

        self.text_5_text = str(self.ones)
        self.text_5_width = 80
        self.text_5_height = 50
        self.text_5_x_coord = 1078
        self.text_5_y_coord = 435

        self.question_label_y = 470

    def generate_total(self):
        return random.randint(1111, 9999)

    def set_text_2(self):
        return 1000 * (self.total // 1000)

    def set_text_3(self):
        return 100 * ((self.total - self.thousands) // 100)

    def set_text_4(self):
        return 10 * ((self.total - self.thousands - self.hundreds) // 10)

    def set_text_5(self):
        return self.total - self.thousands - self.hundreds - self.tens

    def choose_selection(self):
        return random.randint(0, 4)


class RoundNumbers:
    def __init__(self, rounding_list):
        self.rounding_options = rounding_list
        self.option_position = self.set_option_position()
        self.round_to = self.rounding_options[self.option_position]
        self.minimum = self.minimum()
        self.maximum = self.maximum()
        self.round_value = self.round_value(self.round_to)
        self.number = self.set_number()
        self.correct_answer = self.correct_answer()
        self.question_text = self.question_text()

    def set_option_position(self):
        return random.randint(0, len(self.rounding_options) - 1)

    def minimum(self):
        minimum = 10 * 10 ** (self.option_position + 1)
        if minimum == 10000000:
            return 1000000
        else:
            return minimum

    def maximum(self):
        maximum = 10 * 10 ** (self.option_position + (random.randint(2, 3)))
        if maximum > 10000000:
            return 10000000
        else:
            return maximum

    def round_value(self, round_to):
        return int(math.log10(round_to)) * -1

    def set_number(self):
        number = random.randint(self.minimum, self.maximum)
        while number % self.round_to == 0:
            number = random.randint(self.minimum, self.maximum)
        return number

    def correct_answer(self):
        return round(self.number, self.round_value)

    def question_text(self):
        return "Round {} to the nearest {}.".format(self.number, self.round_to)


class Objective4N4b:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        question = RoundNumbers((10, 100, 1000))
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class Objective5N4:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        question = RoundNumbers((10, 100, 1000, 10000, 100000))
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class Objective6N4:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        question = RoundNumbers((10, 100, 1000, 10000, 100000, 1000000))
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class NumberBonds:
    def __init__(self, minimum, maximum, multiple):
        self.multiple = multiple
        self.minimum = minimum / multiple
        self.maximum = maximum / multiple
        self.total = random.randint(self.minimum, self.maximum)
        self.first_number = self.generate_first_number()
        self.second_number = self.generate_second_number()
        self.add = random_boolean()
        self.correct_answer = self.correct_answer()
        self.question_text = self.question_text()

    def generate_first_number(self):
        return random.randint(self.minimum - 1, self.total - 1)

    def generate_second_number(self):
        return self.total - self.first_number

    def correct_answer(self):
        if self.add:
            return self.total * self.multiple
        else:
            return self.second_number * self.multiple

    def question_text(self):
        if self.add:
            return "What is {} + {}?".format(self.first_number * self.multiple, self.second_number * self.multiple)
        else:
            return "What is {} - {}?".format(self.total * self.multiple, self.first_number * self.multiple)


class Objective4N5:
    def __init__(self):
        self.multi_plot = True
        self.place_text = False
        self.total_images = 1

        self.image_1_path = "C:/Users/Michael/Pictures/Saved Pictures/number_line_-5_to_5.jpg"
        self.image_1_width = 600
        self.image_1_height = 150
        self.image_1_frequency = 1
        self.image_1_x_coord = [960 - self.image_1_width // 2]
        self.image_1_y_coord = [300]

        self.question_label_y = 450

        self.position = self.set_position()
        self.correct_answer = self.correct_answer()
        self.question_text = self.question_text()

    def set_position(self):
        return random.randint(0, 3)

    def correct_answer(self):
        letters = ("A", "B", "C", "D")
        return letters[self.position]

    def question_text(self):
        number = (-4, -3, -2, -1)
        return "Which letter shows where {} is?".format(number[self.position])


class Objective5N5:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        self.first_number = self.set_first_number()
        self.decrease = self.set_decrease()
        self.correct_answer = self.correct_answer()
        self.question_text = self.question_text()

    def set_first_number(self):
        return random.randint(13, 37)

    def set_decrease(self):
        mini = round(self.first_number / 3.5)
        maxi = round(self.first_number / 2)
        if maxi > 12:
            maxi = 12
        decrease_list = [x for x in range(mini, maxi + 1)]
        for number in decrease_list:
            if self.first_number % number == 0:
                decrease_list.remove(number)
        return random.choice(decrease_list)

    def correct_answer(self):
        return self.first_number - 4 * self.decrease

    def question_text(self):
        return "What is the next number in the sequence?\n\n{}, {}, {}, {}...".\
            format(self.first_number, self.first_number - self.decrease, self.first_number - 2 * self.decrease,
                   self.first_number - 3 * self.decrease)


class Objective6N5:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        self.direction = random_boolean()
        self.lowest_number = self.set_lowest_number()
        self.change = self.set_change()
        self.correct_answer = self.correct_answer()
        self.question_text = self.question_text()

    def set_lowest_number(self):
        return random.randint(-20, -5)

    def set_change(self):
        return random.randint(3, 9)

    def correct_answer(self):
        if self.direction:
            return self.lowest_number + self.change
        else:
            return self.lowest_number

    def question_text(self):
        if self.direction:
            direction = "rises"
            first_number = self.lowest_number
        else:
            direction = "falls"
            first_number = self.lowest_number + self.change
        second_number = self.change
        return "The temperature is {}°C. It {} by {} degrees.\n\nWhat is the temperature now?".format(first_number,
                                                                                                      direction,
                                                                                                      second_number)


class Objective1C1:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        question = NumberBonds(8, 20, 1)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class Objective2C1:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        self.type = random_boolean()
        if self.type:
            question = NumberBonds(11, 20, 1)
        else:
            question = NumberBonds(20, 100, 10)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text


class AdditionOrSubtraction:
    def __init__(self, total, number, switch=False):
        if number > total:
            number, total = total, number
        self.add = random_boolean()
        self.total = total
        self.number = number
        self.second_number = self.total - self.number
        if self.second_number > self.number or switch:
            self.number, self.second_number = self.second_number, self.number
        self.correct_answer = self.correct_answer()
        self.question_text = self.question_text()

    def correct_answer(self):
        if self.add:
            return self.total
        else:
            return self.number

    def question_text(self):
        if self.add:
            return "What is {} + {}?".format(self.number, self.second_number)
        else:
            return "What is {} - {}?".format(self.total, self.second_number)


class Objective3C1:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        total = self.generate_total()
        number = self.generate_number()
        question = AdditionOrSubtraction(total, number)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text

    def generate_total(self):
        total = random.randint(110, 999)
        while total % 10 == 0 or total % 100 < 10:
            total = random.randint(110, 999)
        return total

    def generate_number(self):
        columns = random.randint(1, 3)
        return random.randint(1, 9) * 10 ** (columns - 1)


class Objective5C1:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        total = self.generate_total()
        number = self.generate_number()
        while -500 < total - number < 500:
            number = self.generate_number()
        question = AdditionOrSubtraction(total, number)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text

    def generate_total(self):
        total = random.randint(1000, 9999)
        while total % 10 == 0 or total % 100 < 10:
            total = random.randint(1000, 9999)
        return total

    def generate_number(self):
        number = random.randint(1000, 9999)
        while number % 10 == 0 or number % 100 < 10:
            number = random.randint(1000, 9999)
        return number


class Objective1C2a:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        self.total = self.generate_total()
        number = self.generate_number()
        question = AdditionOrSubtraction(self.total, number)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text

    def generate_total(self):
        return random.randint(8, 20)

    def generate_number(self):
        return random.randint(0, self.total)


class Objective2C2a:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False


        self.type = random.randint(1, 3)
        if self.type == 3:
            number1 = random.randint(1, 9)
            number2 = random.randint(1, 9)
            number3 = random.randint(1, 9)
            self.correct_answer = number1 + number2 + number3
            self.question_text = "What is {} + {} + {}?".format(number1, number2, number3)
        else:
            self.total = self.generate_total()
            number = self.generate_number()
            question = AdditionOrSubtraction(self.total, number, True)
            self.correct_answer = question.correct_answer
            self.question_text = question.question_text

    def generate_total(self):
        number = random.randint(30, 99)
        while number % 10 == 0:
            number = random.randint(30, 99)
        return number

    def generate_number(self):
        number = random.randint(3, 9)
        if self.type == 1:
            return number
        else:
            while number * 10 > self.total or -10 < number * 10 - self.total < 10:
                number = random.randint(1, 9)
            return number * 10


class Objective3C2:
    def __init__(self):
        self.multi_plot = False

        self.total = self.generate_total()
        number = self.generate_number()
        question = AdditionOrSubtraction(self.total, number)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text

    def generate_total(self):
        number = random.randint(300, 999)
        while number % 10 == 0:
            number = random.randint(300, 999)
        return number

    def generate_number(self):
        number =  random.randint(50, self.total - 100)
        while number % 10 == 0:
            number = random.randint(50, self.total - 100)
        return number


class Objective4C2:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        self.total = self.generate_total()
        number = self.generate_number()
        question = AdditionOrSubtraction(self.total, number)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text

    def generate_total(self):
        number = random.randint(3000, 9999)
        while number % 10 == 0:
            number = random.randint(3000, 9999)
        return number

    def generate_number(self):
        number = random.randint(500, self.total - 1000)
        while number % 10 == 0:
            number = random.randint(500, self.total - 1000)
        return number


class Objective5C2:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        self.total = self.generate_total()
        number = self.generate_number()
        question = AdditionOrSubtraction(self.total, number)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text

    def generate_total(self):
        number = random.randint(80000, 999999)
        while number % 10 == 0:
            number = random.randint(80000, 999999)
        return number

    def generate_number(self):
        number = random.randint(50000, self.total - 30000)
        while number % 10 == 0:
            number = random.randint(50000, self.total - 30000)
        return number


class InverseAddSub:
    def __init__(self, number, total):
        self.number = number
        self.total = total
        if self.number > self.total:
            self.number, self.total = self.total, self.number
        self.add = random_boolean()
        self.correct_answer = self.number
        self.question_text = self.question_text()

    def question_text(self):
        if self.add:
            return "{} + ? = {}".format(self.total - self.number, self.total)
        else:
            return "{} - ? = {}".format(self.total, self.total - self.number)


class InverseMulDiv:
    def __init__(self, multiple1, multiple2):
        self.multiple1 = multiple1
        self.multiple2 = multiple2
        self.multiply = random_boolean()
        self.correct_answer = self.multiple2
        self.question_text = self.question_text()

    def question_text(self):
        if self.multiply:
            return "{} x ? = {}".format(self.multiple1, self.multiple1 * self.multiple2)
        else:
            return "{} ÷ ? = {}".format(self.multiple1 * self.multiple2, self.multiple1)


class Objective2C3:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        self.total = self.generate_total()
        number = self.generate_number()
        question = InverseAddSub(number, self.total)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text

    def generate_total(self):
        number = random.randint(40, 99)
        while number % 10 == 0:
            number = random.randint(40, 99)
        return number

    def generate_number(self):
        number = random.randint(20, self.total - 20)
        while number % 10 == 0:
            number = random.randint(20, self.total - 20)
        return number


class Objective3C3:
    def __init__(self):
        self.multi_plot = False
        self.place_text = False

        self.total = self.generate_total()
        number = self.generate_number()
        question = InverseAddSub(number, self.total)
        self.correct_answer = question.correct_answer
        self.question_text = question.question_text

    def generate_total(self):
        total = random.randint(110, 999)
        while total % 10 == 0 or total % 100 < 10:
            total = random.randint(110, 999)
        return total

    def generate_number(self):
        columns = random.randint(1, 3)
        return random.randint(1, 9) * 10 ** (columns - 1)

