#!/usr/bin/env python3.11

import sys
import constants
import RHEPY_lang
from colorama import Fore, init
from statements import print_statements

# initialize colorama
init()


def print_greeting():
    display_symbol = True

    for arg in sys.argv:
        if arg == "--no-symbol":
            display_symbol = False

    if display_symbol:
        enneagram_symbol = open("enneagram_symbol.txt", "r")
        print(Fore.CYAN + enneagram_symbol.read() + Fore.RESET)
        enneagram_symbol.close()

    print(
        "RHEPY v1.0\n"
        "RHEPY is made by " + Fore.GREEN + "sirkhancision" + Fore.RESET + "\n"
        "All rights are reserved to the respective owners of RHETI\n"
    )


def language_choice():
    print(
        "Select the language of the test:\n"
        "(select a different option to exit)\n"
        + Fore.RED
        + "[1] English\n"
        + Fore.GREEN
        + "[2] Portuguese"
        + Fore.RESET
    )

    language = input()
    if language != constants.ENGLISH and language != constants.PORTUGUESE:
        print("Exiting...")
        sys.exit(0)

    return language


def instructions_or_test_choice(language):
    match language:
        case constants.ENGLISH:
            print(
                Fore.RED
                + "[1] "
                + Fore.GREEN
                + "Instructions\n"
                + Fore.RED
                + "[2] "
                + Fore.GREEN
                + "The RHEPY test"
                + Fore.RESET
            )
            choice = input()
        case constants.PORTUGUESE:
            print(
                Fore.RED
                + "[1] "
                + Fore.GREEN
                + "Instruções\n"
                + Fore.RED
                + "[2] "
                + Fore.GREEN
                + "O teste RHEPY"
                + Fore.RESET
            )
            choice = input()
        case _:
            print("Invalid language choice")
            sys.exit(1)
    return choice


try:

    def main():
        # the nine Enneagram types and the resulting type from the test
        enneagram_types = {
            "d_1": 0,
            "f_2": 0,
            "c_3": 0,
            "e_4": 0,
            "h_5": 0,
            "b_6": 0,
            "i_7": 0,
            "g_8": 0,
            "a_9": 0,
            "result": 0,
        }

        print_greeting()
        language = language_choice()
        RHEPY_lang.print_post_greeting(language)

        while True:
            choice = instructions_or_test_choice(language)
            if choice == constants.INSTRUCTIONS:
                RHEPY_lang.print_instructions(language)
            elif choice == constants.TEST:
                break

        print_statements(language, enneagram_types)
        RHEPY_lang.print_result(language, enneagram_types)

    if __name__ == "__main__":
        main()

except KeyboardInterrupt:
    print("\nEnded by user, exiting...")
    sys.exit(0)
