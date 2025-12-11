

import os
import sys



# --- КОНФІГУРАЦІЯ ---
BLOCK_W = 14  # Ширина одного блоку (включно з рамкою)
ROWS = 3
COLS = 5
DB_FILE = "users.json"

# Кольори (ANSI)
RED = "\033[91m"
RESET = "\033[0m"


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_block_lines(r, c, text):
    """
    Генерує 3 рядки (верх, центр, низ) для конкретного блоку (r, c).
    Визначає, чи потрібна рамка, залежно від позиції.
    """
    # 1. Визначаємо символи для цього блоку
    char_top = " "  # За замовчуванням пусто
    char_bot = " "
    char_left = " "
    char_right = " "

    # Логіка ВЕРХНЬОЇ межі (тільки якщо це r=0)
    if r == 0:
        char_top = "═"
        # Кутики для верхнього ряду
        corner_tl = "╔" if c == 0 else "═"
        corner_tr = "╗" if c == COLS - 1 else "═"
    else:
        # Всередині сітки верху немає (пустота)
        corner_tl = "║" if c == 0 else " "
        corner_tr = "║" if c == COLS - 1 else " "

    # Логіка НИЖНЬОЇ межі (тільки якщо це r=2, останній ряд)
    if r == ROWS - 1:
        char_bot = "═"
        # Кутики для нижнього ряду
        corner_bl = "╚" if c == 0 else "═"
        corner_br = "╝" if c == COLS - 1 else "═"
    else:
        corner_bl = "║" if c == 0 else " "
        corner_br = "║" if c == COLS - 1 else " "

    # Логіка БОКОВИХ меж (тільки для c=0 та c=4)
    if c == 0: char_left = "║"
    if c == COLS - 1: char_right = "║"

    # 2. Формуємо рядки блоку (Top, Mid, Bot)

    # --- TOP LINE ---
    if r == 0:
        # Якщо це самий верх - малюємо лінію
        # Лівий кут + (W-2) ліній + Правий кут
        # Але тут хитрість: блок 14 символів.
        if c == 0:
            line_top = corner_tl + char_top * (BLOCK_W - 1)
        elif c == COLS - 1:
            line_top = char_top * (BLOCK_W - 1) + corner_tr
        else:
            line_top = char_top * BLOCK_W
    else:
        # Якщо не верх - це просто бокові стінки або пустота
        if c == 0:
            line_top = char_left + " " * (BLOCK_W - 1)
        elif c == COLS - 1:
            line_top = " " * (BLOCK_W - 1) + char_right
        else:
            line_top = " " * BLOCK_W

    # --- MID LINE (З ТЕКСТОМ) ---
    # Обчислюємо доступну ширину для тексту
    # Якщо зліва рамка - мінус 1 символ. Якщо справа - мінус 1 символ.
    pad_l = 1 if c == 0 else 0
    pad_r = 1 if c == COLS - 1 else 0
    text_space = BLOCK_W - pad_l - pad_r

    # Центруємо текст
    centered_text = text[:text_space].center(text_space)

    # Склеюємо: Ліва межа + Текст + Права межа
    line_mid = (char_left if c == 0 else "") + centered_text + (char_right if c == COLS - 1 else "")
    # Добиваємо пробілами, якщо раптом текст короткий (хоча center це робить)
    # Важливо: якщо це середній блок, там немає меж, тому просто center(14)

    # --- BOT LINE ---
    if r == ROWS - 1:
        # Якщо самий низ
        if c == 0:
            line_bot = corner_bl + char_bot * (BLOCK_W - 1)
        elif c == COLS - 1:
            line_bot = char_bot * (BLOCK_W - 1) + corner_br
        else:
            line_bot = char_bot * BLOCK_W
    else:
        # Якщо не низ
        if c == 0:
            line_bot = char_left + " " * (BLOCK_W - 1)
        elif c == COLS - 1:
            line_bot = " " * (BLOCK_W - 1) + char_right
        else:
            line_bot = " " * BLOCK_W

    return [line_top, line_mid, line_bot]


def render_grid(blocks_data, prompt_text=">>> "):
    clear()

    # Проходимо по рядах
    for r in range(ROWS):
        # Буфери для склеювання рядків
        row_str_top = ""
        row_str_mid = ""
        row_str_bot = ""

        # Проходимо по колонках
        for c in range(COLS):
            text = blocks_data.get((r, c), "")

            # Отримуємо 3 лінії для цього конкретного блоку
            block_parts = get_block_lines(r, c, text)

            # Склеюємо їх в довгі рядки
            row_str_top += block_parts[0]
            row_str_mid += block_parts[1]
            row_str_bot += block_parts[2]

        # Друкуємо готові лінії ряду
        print(row_str_top)
        print(row_str_mid)
        print(row_str_bot)

    print("\n" + prompt_text, end="")
    return input()


def show_popup_result(is_correct, correct_ans=None, comment=""):
    clear()
    width = 60
    title = " RESULT "
    padding = (width - len(title) - 2) // 2

    print("╔" + "═" * padding + title + "═" * padding + "╗")
    print("║" + "═" * width + "║")
    print("║" + " " * width + "║")

    if is_correct:
        print(f"║ {'✅ ПРАВИЛЬНО!':<{width}}║")
    else:
        print(f"║ {RED}✖{RESET} {'НЕПРАВИЛЬНО!':<{width - 2}}║")
        print(f"║ {f'Правильно: {correct_ans}':<{width}}║")

    print("║" + " " * width + "║")
    print(f"║ {comment:<{width}}║")
    print("║" + " " * width + "║")
    print("╚" + "═" * width + "╝")
    input("\nНатисни Enter...")


# --- ЛОГІКА ПРОГРАМИ ---

def screen_start():
    while True:
        grid = {}
        # Логотип (Верхній ряд)
        grid[(0, 1)] = "TOXIC"
        grid[(0, 2)] = "QUIZ"
        grid[(0, 3)] = "v1.0"

        # Кнопки (Середній ряд)
        grid[(1, 1)] = "[1] GET IN"
        grid[(1, 3)] = "[q] QUIT"

        choice = render_grid(grid)
        if choice == '1':
            screen_auth()
        elif choice.lower() == 'q':
            sys.exit()


def screen_auth():
    global USERS_DB, CURRENT_USER
    while True:
        grid = {}
        grid[(0, 2)] = "AUTH"
        grid[(1, 1)] = "[1] LOGIN"
        grid[(1, 3)] = "[2] REGISTER"
        grid[(2, 2)] = "[b] BACK"

        choice = render_grid(grid)

        if choice == '1':
            grid[(1, 1)] = ">> TYPE <<"
            login = render_grid(grid, "Nick >>> ")
            if login in USERS_DB:
                CURRENT_USER = login
                screen_dashboard()
            else:
                show_popup_result(False, "User not found", "Ти не існуєш.")
        elif choice == '2':
            new_login = render_grid(grid, "New Nick >>> ")
            if new_login and new_login not in USERS_DB:
                USERS_DB[new_login] = {"xp": 0}
                CURRENT_USER = new_login
                screen_dashboard()
        elif choice.lower() == 'b':
            return


def screen_dashboard():
    global CURRENT_USER
    while True:
        xp = USERS_DB[CURRENT_USER]['xp']
        grid = {}

        # ЛІВА ЧАСТИНА (ІНФО)
        grid[(0, 0)] = "USER:"
        grid[(0, 1)] = CURRENT_USER[:10]

        grid[(1, 0)] = "XP:"
        grid[(1, 1)] = str(xp)

        grid[(2, 0)] = "RANK:"
        grid[(2, 1)] = "NOOB" if xp < 50 else "BOSS"

        # ПРАВА ЧАСТИНА (МЕНЮ)
        grid[(0, 3)] = "[1] MATH"
        grid[(1, 3)] = "[2] CS"
        grid[(2, 4)] = "[b] OUT"




