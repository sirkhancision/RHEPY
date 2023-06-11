#!/usr/bin/env python3

import sys
from constants import ENGLISH, EXPLANATION, INSTRUCTIONS, PORTUGUESE, TEST
from colorama import Fore
from RHEPY_lang import (print_instructions, print_post_greeting, print_result,
                        print_result_explanation)
from statements import print_statements


def print_greeting():
    """
    Prints the first line of text, with or without the enneagram symbol
    ASCII art
    """
    display_symbol = "--no-symbol" not in sys.argv

    if display_symbol:
        with open("enneagram_symbol.txt", "r") as enneagram_symbol:
            print(Fore.CYAN + enneagram_symbol.read() + Fore.RESET)

    print("RHEPY v1.5\n"
          "RHEPY is made by " + Fore.GREEN + "sirkhancision" + Fore.RESET +
          "\n"
          "All rights are reserved to the respective owners of RHETI\n")


def language_choice():
    """
    Select the language of the text displayed
    """
    print("Select the language of the test:\n"
          "(select a different option to exit)\n" + Fore.RED +
          "[1] English\n" + Fore.GREEN + "[2] Portuguese" + Fore.RESET)

    language = input()
    if language != ENGLISH and language != PORTUGUESE:
        print("Exiting...")
        sys.exit(0)

    return language


def test_choice(language):
    """
    Prints translated prompt for selecting if the user wants to read the
    instructions, go directly to the test, or read how the results of the
    test are calculated
    """
    choices = {
        ENGLISH: (Fore.RED + "[1] " + Fore.GREEN + "Instructions\n" +
                  Fore.RED + "[2] " + Fore.GREEN + "The RHEPY test\n" +
                  Fore.RED + "[3] " + Fore.GREEN + "Explain how the results "
                  "are calculated" + Fore.RESET),
        PORTUGUESE: (Fore.RED + "[1] " + Fore.GREEN + "Instruções\n" +
                     Fore.RED + "[2] " + Fore.GREEN + "O teste RHEPY\n" +
                     Fore.RED + "[3] " + Fore.GREEN + "Explicar como os "
                     "resultados são calculados" + Fore.RESET)
    }

    choices_output = choices.get(language)
    if choices_output:
        print(choices_output)

        choice = input()
        return choice
    else:
        raise ValueError("Invalid language choice")


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

    try:
        print_post_greeting(language)

        while True:
            choice = test_choice(language)

            if choice == INSTRUCTIONS:
                print_instructions(language)
            elif choice == EXPLANATION:
                print_result_explanation(language)
            elif choice == TEST:
                break

        print_statements(language, enneagram_types)

        print_result(language, enneagram_types)
    except ValueError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nEnded by user, exiting...")
        sys.exit(0)
