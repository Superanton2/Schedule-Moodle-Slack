from helper_functions import RED, RESET

import os


class Visual:

    def __init__(self):
        self.window = None
        self.window_width = None
        self.window_height = None
        self.block_width = None
        self.block_height = None


    def create_window(self, window_width: int, window_height: int, block_width: int, block_height: int) -> int:
        self.window_width = window_width - 1
        self.window_height = window_height - 1
        self.block_width = block_width
        self.block_height = block_height

        self.window = []

        counter = 0

        # Створюємо сітку [x][y]
        for x in range(window_width):
            colum = []
            for y in range(window_height + 1):

                new_block = [" " * block_width for _ in range(block_height)]
                colum.append(new_block)
                counter += 1
            self.window.append(colum)

        return counter

    def _check_write_to_coordinate(self, x_cord: int, y_cord: int, content) -> bool:
        # загальна перевірка
        if self.window is None:
            print(f"{RED}First create window{RESET}")
            return False

        if x_cord > self.window_width:
            print(f"{RED}X-coordinate is too large. Max possible value is {self.window_width}{RESET}")
            return False

        if y_cord > self.window_height:
            print(f"{RED}Y-coordinate is too large. Max possible value is {self.window_height}{RESET}")
            return False

        # перевірка тексту
        if type(content) == str:
            if len(content) > (self.block_height * self.block_width):
                print(f"{RED}Your content is too large. Max possible len is {self.block_height * self.block_width}{RESET}")
                return False

        if type(content) == list:

            if len(content) > self.block_height:
                print(f"{RED}To mush lines. Max possible number of line is {self.block_height}{RESET}")
                return False


            characters = 0
            for line in content:
                if len(line) > self.block_width:
                    print(f"{RED}Your content in line {content.index(line)} is too long."
                          f"Max possible number of line is {self.block_width}{RESET}")
                    return False

                characters += len(line)


            if characters > (self.block_height * self.block_width):
                print(f"{RED}Your content is too long. Max possible len is {self.block_height * self.block_width}{RESET}")
                return False



        return True

    def write_str_to_coordinate(self, x_cord: int, y_cord: int, content: str):
        # перевірка
        if not self._check_write_to_coordinate(x_cord, y_cord, content):
            return False


        # запис по кординатам
        content_words = content.split(" ")
        current_block_line = 0
        for index in range(len(content_words)):


            word = content_words[index - (self.block_height - 1)]
            print((self.block_height - 1) - index)
            print(word)

            if index == (len(content_words) - 1):
                sep = " " * (self.block_width - len(word))
            else:
                sep = " "


            if len(word) < self.block_width:
                self.window[x_cord][y_cord][index - (self.block_height - 1)] = word + sep

            else:
                self.window[x_cord][y_cord][index - (self.block_height - 1)] = word + sep



            if len(self.window[x_cord][y_cord][index - (self.block_height - 1)]) > self.block_width:

                if current_block_line < (self.block_height - 1):
                    current_block_line += 1
                else:
                    break

        print(content_words)

        self.window[x_cord][y_cord][0] = content + " "*(self.block_width - len(content))

        return True

    def write_lst_to_coordinate(self, x_cord: int, y_cord: int, content: list[str]):

        # перевірка
        if not self._check_write_to_coordinate(x_cord, y_cord, content):
            return None

        # запис по кординатам
        for index in range(len(content)):

            sep = " " * (self.block_width - len(content[index]))

            self.window[x_cord][y_cord][index - (self.block_height - 1)] = content[index] + sep


        return True

    def print_window(self, vertical_sep= "", horizontal_sep= ""):
        # self.clear_window()

        for y in range(self.window_height):
            # [(self.window_height - 1) - y]

            for line in range(self.block_height):

                for x in range(self.window_width + 1):

                    print(self.window[x][(self.window_height - 1) - y][(self.block_height - 1) - line], end= vertical_sep)

                if (self.block_height - 1) - line == 0:
                    print()
                    # horizontal_line = (horizontal_sep * (self.block_width + 1)) * (self.window_width + 1)
                    # print(horizontal_line, end= "")
                    horizontal_line = ((horizontal_sep * self.block_width) + "·") * (self.window_width + 1)
                    print(horizontal_line, end= "")

                print()
            # [(self.block_height - 1) - line]

        return self.window

    def print_horizontal_lines(self):
        pass

    # def clear_window(self):
    #     os.system('cls' if os.name == 'nt' else 'clear')


vis = Visual()
vis.create_window(3, 3, 10, 3)
print()
# vis.write_str_to_coordinate(0, 0,   "to in")

# vis.write_lst_to_coordinate(1, 1, ["444irasntieans4", "Я"])
# vis.write_lst_to_coordinate(1, 1, ["1", "Я тут", ""])

print()

vis.print_window(vertical_sep= "│", horizontal_sep= "─")
print()

vis.print_window(vertical_sep= "┃", horizontal_sep= "━")





"""
━
┃
┏┳┓
┣╋┫

┗┻┛
"""


#
# # метод виводу розкладу на тиждень
# # переключення між тижнями
#
# # from tqdm import tqdm
# # import time
# #
# # # range(100) — це загальна кількість кроків
# # for i in tqdm(range(100), desc="Обробка файлів", ascii=False):
# #     time.sleep(0.1) # Імітація роботи
#
#
#
# import time
#
# print("Запуск таймера...")
#
# for i in range(10, 0, -1):
#     # \r повертає на початок. end="" забороняє новий рядок.
#     # Пробіли в кінці потрібні, щоб затерти залишки довшого тексту
#     print(f"\rЗалишилось часу: {i} секунд   ", end="")
#     time.sleep(1)
#
# print("\rГотово!                   ")
