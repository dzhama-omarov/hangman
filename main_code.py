import random
import time
import json
import os
from pprint import pprint


# Load json data from filepath
def load_json(filename) -> dict:
    with open(filename, "r", encoding="utf8") as file:
        return json.load(file)


text = load_json("resources/texts.json")
pictures = load_json("resources/pictures.json")
word_lists = load_json("resources/word_lists.json")


def print_from_imported_json(resource_type, key, language="en") -> None:
    try:
        imported_value = resource_type[language][key]
        print(imported_value)
    except KeyError:
        print("KeyError! Could not find key:", key, "Dictionary/Json below:")
        pprint(resource_type)


def clear_previous_line(length_of_line=100) -> None:
    print("\033[A" + ' '*length_of_line + "\033[A")


def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu() -> None:
    global language
    global number_of_lives
    while True:
        print_from_imported_json(text, "main_menu_txt", language)
        choice = input().lower().strip()
        if choice == "1":
            already_given_letters = []
            my_word, current_word = setup_game()
            while "_" in current_word and number_of_lives > 0:
                input_letter = guessing_letter(already_given_letters)
                already_given_letters.append(input_letter)
                current_word = letter_check(
                                            my_word,
                                            current_word,
                                            input_letter)
            end_game(my_word)
        elif choice == "2":
            rules_page()
        elif choice == "3":
            settings_menu()
        elif choice == "4":
            credits_page()
        elif choice == "5":
            clear_terminal()
        elif choice == "6":
            if language == "en":
                print("\nCya next time!")
            elif language == "ru":
                print("\nУвидимся в следующий раз!")
            elif language == "de":
                print("\nAuf Wiedersehen!")
            elif language == "fr":
                print("\nAu revoir!")
            exit(0)
        elif choice == "easter":
            easter_egg_page()
        else:
            print_from_imported_json(text, "known_input_err_txt", language)


def rules_page() -> None:
    global language
    while True:
        print_from_imported_json(text, "rules_txt", language)
        back = input().lower().strip()
        if back != "b":
            print_from_imported_json(text, "unknown_input_err_txt", language)
        else:
            break
    return


def easter_egg_page() -> None:
    global language
    while True:
        print_from_imported_json(text, "easter_egg_txt", language)
        back = input().lower().strip()
        if back != "b":
            print_from_imported_json(text, "unknown_input_err_txt", language)
        else:
            break
    return


def credits_page() -> None:
    global language
    while True:
        print_from_imported_json(text, "credits_txt", language)
        back = input().lower().strip()
        if back != "b":
            print_from_imported_json(text, "unknown_input_err_txt", language)
        else:
            break
    return


def settings_menu() -> None:
    global language
    while True:
        print_from_imported_json(text, "settings_txt", language)
        choice = input().lower().strip()
        if choice == "1":
            lives_settings()
        elif choice == "2":
            language_settings()
        elif choice == "b":
            break
        else:
            print_from_imported_json(text, "known_input_err_txt", language)
    return


def lives_settings() -> None:
    global language
    global number_of_lives
    while True:
        print_from_imported_json(text, "lives_settings_txt", language)
        choice = input().lower().strip()
        if choice not in ["b", "1", "2", "3", "4", "5"]:
            print_from_imported_json(text, "known_input_err_txt", language)
        elif choice == "b":
            break
        else:
            number_of_lives = int(choice)
            print_from_imported_json(text, "lives_changed_txt", language)


def language_settings() -> None:
    global language
    while True:
        print_from_imported_json(text, "language_settings_txt", language)
        choice = input().lower().strip()
        if choice not in ["b", "1", "2", "3", "4"]:
            print_from_imported_json(text, "known_input_err_txt", language)
        elif choice == "1":
            language = "en"
            print_from_imported_json(text, "language_changed_txt", language)
        elif choice == "2":
            language = "ru"
            print_from_imported_json(text, "language_changed_txt", language)
        elif choice == "3":
            language = "de"
            print_from_imported_json(text, "language_changed_txt", language)
        elif choice == "4":
            language = "fr"
            print_from_imported_json(text, "language_changed_txt", language)
        else:
            break


def setup_game() -> tuple[str, str]:
    global language
    global number_of_lives

    print_from_imported_json(text, "in_game_txt1", language)
    for _ in range(3):
        print(".")
        time.sleep(0.5)
        clear_previous_line()
        print("..")
        time.sleep(0.5)
        clear_previous_line()
        print("...")
        time.sleep(0.5)
        clear_previous_line()

    my_word = random.choice(word_lists[language]).lower()
    print_from_imported_json(text, "in_game_txt2", language)
    print_from_imported_json(pictures, f"p{5-number_of_lives}")

    current_word = "_" * len(my_word)
    print(" ".join(current_word))
    print_from_imported_json(text, "in_game_txt3", language)
    return my_word, current_word


def guessing_letter(already_given_letters) -> str:
    global language
    global number_of_lives

    while True:
        input_letter = input().lower().strip()
        if len(input_letter) != 1 or not input_letter.isalpha():
            print_from_imported_json(text, "in_game_input_err_txt", language)
        elif input_letter in already_given_letters:
            print_from_imported_json(text, "in_game_same_letter_txt", language)
        else:
            break
    return input_letter


def letter_check(my_word, current_word, input_letter) -> str:
    global language
    global number_of_lives

    if input_letter in my_word:
        print_from_imported_json(text, "in_game_txt5", language)
        current_word = "".join(
                                input_letter if my_word[i]
                                == input_letter else current_word[i]
                                for i in range(len(my_word))
                                )
        print_from_imported_json(pictures, f"p{5-number_of_lives}")
        print(" ".join(current_word))
        print_from_imported_json(text, "in_game_txt3", language)
        return current_word
    else:
        print_from_imported_json(text, "in_game_txt4", language)
        number_of_lives -= 1
        print_from_imported_json(pictures, f"p{5-number_of_lives}")
        print(" ".join(current_word))
        print_from_imported_json(text, "in_game_txt3", language)
        return current_word


def end_game(my_word) -> None:
    global number_of_lives
    while True:
        if number_of_lives == 0:
            print_from_imported_json(text, "in_game_txt7", language)
            print_from_imported_json(text, "in_game_txt8", language)
            print(my_word)
            print_from_imported_json(text, "in_game_txt9", language)
        else:
            print_from_imported_json(text, "in_game_txt6", language)
            print_from_imported_json(text, "in_game_txt8", language)
            print(my_word)
            print_from_imported_json(text, "in_game_txt9", language)
        choice = input().lower().strip()
        if choice not in ["b"]:
            print_from_imported_json(text, "known_input_err_txt", language)
        else:
            number_of_lives = 5
            break


language = "en"
number_of_lives = 5

if __name__ == '__main__':
    main_menu()
