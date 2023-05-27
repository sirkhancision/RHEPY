#!/usr/bin/env python3

import constants as consts
from ansiwrap import *
from colorama import Fore, init
from results import result_type, result_wing

# initialize colorama
init()


def print_post_greeting(language):
    """
    Prints the text after the initial greeting text, even though it's also a greeting
    """
    match language:
        case consts.ENGLISH:
            print(
                "Welcome to "
                + Fore.CYAN
                + "RHEPY"
                + Fore.RESET
                + ", the Riso-Hudson Enneagram Type Indicator (RHETI) in Python!\n"
                "Enter [1] to proceed with the instructions, or [2] to go directly to the test",
            )
        case consts.PORTUGUESE:
            print(
                "Bem-vindo ao "
                + Fore.CYAN
                + "RHEPY"
                + Fore.RESET
                + ", o Indicador de Tipo do Eneagrama de Riso-Hudson (RHETI) em Python!\n"
                "Digite [1] para seguir com as instruções ou [2] para ir direto ao teste",
            )


def print_instructions(language):
    """
    Prints the instructions to the test
    """
    match language:
        case consts.ENGLISH:
            print(
                "\n".join(
                    wrap(
                        "This test has "
                        + Fore.RED
                        + "144 "
                        + Fore.RESET
                        + "paired statements, where you have to choose the statement in each pair that describes you best. Even if you feel that in certain pairs, neither describes you very well, or that both statements are almost equally true, you must try to choose the statement that describes you best.",
                        80,
                    )
                )
            )
            print("")

            print(
                "\n".join(
                    wrap(
                        "The most accurate approach to the test is to take it from the point of view of the past, as you have been most of your life. You must enter the letter that corresponds to the statement you want to select. If you're unsure of what to choose, you can skip the current pair by entering [>].",
                        80,
                    )
                )
            )
            print("")

            print(
                "\n".join(
                    wrap(
                        "The profile you get from RHEPY will reflect your personality's principal psychological functions, the balance of which changes over time. Your basic personality type should remain the same, but other personality functions shift over time. You might also want to take the test as you are in the present, after you've taken it before. This test takes approximately 40 minutes to complete.",
                        80,
                    )
                )
            )

            print(
                "\n".join(
                    wrap(
                        "After you've taken the test, it's recommended that you read about the Enneagram type you got as a result. Personal recommendations are:",
                        80,
                    )
                )
            )
            print("")

            print(
                Fore.BLUE
                + "https://www.enneagraminstitute.com/ "
                + Fore.RESET
                + "(English)\n"
                + Fore.BLUE
                + "https://os16mistypes.wixsite.com/16mistypes "
                + Fore.RESET
                + "(Portuguese)\n",
            )

            print(
                "\n".join(
                    wrap(
                        Fore.RED
                        + "PLEASE NOTE! "
                        + Fore.RESET
                        + 'The accuracy of this test will be increased if you understand that we have four "selves": our past self, our present self, our ideal self, and our self as others see us. RHEPY is attempting to discern only your past self. Therefore, it\'s essential that you keep your focus on answering in your past self only, and not mix your past, present, ideal, or social self.',
                        80,
                    )
                )
            )
            print("")
        case consts.PORTUGUESE:
            print(
                "\n".join(
                    wrap(
                        "Esse teste possui "
                        + Fore.RED
                        + "144 "
                        + Fore.RESET
                        + "pares de frases, onde você tem que escolher a frase em cada par que lhe descreve melhor. Até se você sentir que em certos pares, nenhum te descreve muito bem, ou que ambas as frases são quase igualmente verdadeiras, você deve tentar escolher a frase que lhe descreve melhor.",
                        80,
                    )
                )
            )
            print("")

            print(
                "\n".join(
                    wrap(
                        "A abordagem mais precisa para o teste é fazê-lo pelo ponto de vista do passado, como você tem sido na maior parte de sua vida. Você deve digitar a letra correspondente à frase que você deseja selecionar. Se você estiver incerto do que escolher, você pode pular o par atual se digitar [>].",
                        80,
                    )
                )
            )
            print("")

            print(
                "\n".join(
                    wrap(
                        "O perfil que você receberá do RHEPY irá refletir as principais funções psicológicas da sua personalidade, da qual o equilibrio muda com o tempo. O seu tipo básico de personalidade deve continuar o mesmo, mas outras funções da personalidade mudam com o tempo. Você pode querer também fazer o teste pensando em como vocẽ é no presente, depois de já tê-lo feito. Esse teste leva aproximadamente 40 minutos para fazer.",
                        80,
                    )
                )
            )
            print("")

            print(
                "\n".join(
                    wrap(
                        "Após ter feito o teste, é recomendado que você leia sobre o tipo do Eneagrama que você obteve como resultado. Recomendações pessoais são:",
                        80,
                    )
                )
            )
            print("")

            print(
                Fore.BLUE
                + "https://www.enneagraminstitute.com/ "
                + Fore.RESET
                + " (Inglês)\n"
                + Fore.BLUE
                + "https://os16mistypes.wixsite.com/16mistypes "
                + Fore.RESET
                + " (Português)\n",
            )

            print(
                "\n".join(
                    wrap(
                        Fore.RED
                        + "ATENÇÃO! "
                        + Fore.RESET
                        + 'A precisão desse teste será aumentada se você entender que possuímos quatro "eus": o nosso eu do passado, o nosso eu do presente, o nosso eu ideal, e o eu como os outros nos veem. O RHEPY está tentando discernir apenas o seu eu do passado. Portanto, é essencial que você mantenha o foco em responder apenas no seu eu do passado, e não misturar o seu eu do passado, presente, ideal, ou social.',
                        80,
                    )
                )
            )
            print("")


def print_result(language, types):
    """
    Prints the results to the test, with scores
    """
    result = {"type": result_type(types), "wing": result_wing(types)}

    match language:
        case consts.ENGLISH:
            print("RESULTS:\n")

            if result["wing"] > 0:
                print(
                    "Your type is likely: "
                    + Fore.RED
                    + f"Enneagram Type {result['type']}w{result['wing']}"
                    + Fore.RESET
                )
            elif result["type"] == 0 and result["wing"] == 0:
                print(
                    "Your type is likely: "
                    + Fore.RED
                    + "a sneaky bastard"
                    + Fore.RESET
                    + "\n"
                )
            elif result["wing"] == 0:
                print(
                    "Your type is likely: "
                    + Fore.RED
                    + f"Enneagram Type {result['type']} "
                    + Fore.RESET
                    + "(wing couldn't be calculated)\n"
                )

            print(
                "Score:\n"
                f"Type 1: {types['d_1']}\tType 2: {types['f_2']}\tType 3: {types['c_3']}\n"
                f"Type 4: {types['e_4']}\tType 5: {types['h_5']}\tType 6: {types['b_6']}\n"
                f"Type 7: {types['i_7']}\tType 8: {types['g_8']}\tType 9: {types['a_9']}\n"
            )

            print("Thanks for using RHEPY! :)")

        case consts.PORTUGUESE:
            print("RESULTADOS:\n")

            if result["wing"] > 0:
                print(
                    "Seu tipo é provavelmente: "
                    + Fore.RED
                    + f"Tipo {result['type']}w{result['wing']} do Eneagrama"
                    + Fore.RESET
                )
            elif result["type"] == 0 and result["wing"] == 0:
                print(
                    "Seu tipo é provavelmente: "
                    + Fore.RED
                    + "um malandro sorrateiro"
                    + Fore.RESET
                    + "\n"
                )
            elif result["wing"] == 0:
                print(
                    "Seu tipo é provavelmente: "
                    + Fore.RED
                    + f"Tipo {result['type']} do Eneagrama "
                    + Fore.RESET
                    + "(asa não pôde ser calculada)\n"
                )

            print(
                "Pontuação:\n"
                f"Tipo 1: {types['d_1']}\tTipo 2: {types['f_2']}\tTipo 3: {types['c_3']}\n"
                f"Tipo 4: {types['e_4']}\tTipo 5: {types['h_5']}\tTipo 6: {types['b_6']}\n"
                f"Tipo 7: {types['i_7']}\tTipo 8: {types['g_8']}\tTipo 9: {types['a_9']}\n"
            )

            print("Obrigado por usar o RHEPY! :)")
