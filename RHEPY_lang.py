# workaround as ansiwrap still imports the deprecated 'imp' module
try:
    from ansiwrap import wrap
except ModuleNotFoundError:
    import importlib.util
    import sys
    sys.modules['imp'] = importlib.import_module('importlib.util')
    from ansiwrap import wrap
from constants import ENGLISH, PORTUGUESE
from colorama import Fore
from results import result_type, result_wing


def print_post_greeting(language):
    """
    Prints the text after the initial greeting text, even though it's also
    a greeting
    """
    greetings = {
        ENGLISH: ("Welcome to " + Fore.CYAN + "RHEPY" + Fore.RESET +
                  ", the Riso-Hudson Enneagram Type Indicator (RHETI) in "
                  "Python!\n"
                  "Enter [1] to proceed with the instructions, or "
                  "[2] to go directly to the test"),
        PORTUGUESE:
        ("Bem-vindo ao " + Fore.CYAN + "RHEPY" + Fore.RESET +
         ", o Indicador de Tipo do Eneagrama de Riso-Hudson (RHETI) "
         "em Python!\n"
         "Digite [1] para seguir com as instruções ou "
         "[2] para ir direto ao teste"),
    }

    greeting = greetings.get(language)
    if greeting:
        print(greeting)
    else:
        raise ValueError("Invalid language")


def print_instructions(language):
    """
    Prints the instructions to the test
    """
    instructions = {
        ENGLISH: [
            ("This test has " + Fore.RED + "144 " + Fore.RESET +
             "paired statements, and you have to choose the statement "
             "in each pair that best describes you. Even if you feel "
             "that in some pairs neither statement describes you very well, "
             "or that both statements are almost equally true, you must "
             "try to choose the statement that describes you best."),
            ("The most accurate approach to the test is to take it from "
             "the point of view of the past, as you have been for most of "
             "your life. You must enter the letter corresponding to "
             "the statement you wish to choose. If you're not sure of what "
             "to choose, you can skip the current pair by entering [>]."),
            ("The profile you receive from RHEPY reflects the major "
             "psychological functions of "
             "your personality, the balance of which changes over time. Your "
             "basic personality type should remain the same, but other "
             "personality functions will change over time. You may also wish "
             "to take the test as you are now, after you've taken "
             "it before. The test takes about 40 minutes to "
             "complete."),
            ("After you've taken the test, it's recommended that you "
             "read about the Enneagram type you have been given. Personal "
             "recommendations are:"),
            (Fore.BLUE + "https://www.enneagraminstitute.com/ " + Fore.RESET +
             "(English)\n" + Fore.BLUE +
             "https://os16mistypes.wixsite.com/16mistypes " + Fore.RESET +
             "(Portuguese)\n"),
            (Fore.RED + "PLEASE NOTE! " + Fore.RESET + 'The accuracy '
             'of this test will be increased if you understand that '
             'we have four "selves": our past self, our present self, '
             'our ideal self, and our self as others see us. RHEPY only '
             'attempts to identify your past self. So '
             'it\'s important that you concentrate on answering '
             'only in your past self, and not mix up your past, present, '
             'ideal or social self.'),
        ],
        PORTUGUESE: [
            ("Esse teste possui " + Fore.RED + "144 " + Fore.RESET +
             "pares de frases, onde você tem que escolher a frase em "
             "cada par que lhe descreve melhor. Até se você sentir "
             "que em certos pares, nenhum te descreve muito bem, ou que "
             "ambas as frases são quase igualmente verdadeiras, você "
             "deve tentar escolher a frase que lhe descreve melhor. "),
            ("A abordagem mais precisa para o teste é fazê-lo "
             "pelo ponto de vista do passado, como você tem sido "
             "na maior parte de sua vida. Você deve digitar a letra "
             "correspondente à frase que você deseja selecionar. Se "
             "você estiver incerto do que escolher, você pode pular "
             "o par atual se digitar [>]."),
            ("O perfil que você receberá do RHEPY irá refletir as "
             "principais funções psicológicas da sua personalidade, "
             "da qual o equilibrio muda com o tempo. O seu tipo básico "
             "de personalidade deve continuar o mesmo, mas outras "
             "funções da personalidade mudam com o tempo. Você pode "
             "querer também fazer o teste pensando em como você é "
             "no presente, depois de já tê-lo feito. Esse teste leva "
             "aproximadamente 40 minutos para fazer."),
            ("Após ter feito o teste, é recomendado que você "
             "leia sobre o tipo do Eneagrama que você obteve como "
             "resultado. Recomendações pessoais são:"),
            (Fore.BLUE + "https://www.enneagraminstitute.com/ " + Fore.RESET +
             " (Inglês)\n" + Fore.BLUE +
             "https://os16mistypes.wixsite.com/16mistypes " + Fore.RESET +
             " (Português)\n"),
            (Fore.RED + "ATENÇÃO! " + Fore.RESET + 'A precisão desse '
             'teste será aumentada se você entender que possuímos '
             'quatro "eus": o nosso eu do passado, o nosso eu do '
             'presente, o nosso eu ideal, e o eu como os outros nos '
             'veem. O RHEPY está tentando discernir apenas o seu eu do '
             'passado. Portanto, é essencial que você mantenha o foco '
             'em responder apenas no seu eu do passado, e não misturar '
             'o seu eu do passado, presente, ideal, ou social.'),
        ],
    }

    instructions_output = instructions.get(language)
    if instructions_output:
        for paragraph in instructions_output:
            print("\n".join(wrap(paragraph, 80)))
            print("")
    else:
        raise ValueError("Invalid language")


def print_result_explanation(language):
    """
    Prints an explanation about how the results are calculated
    """
    explanation = {
        ENGLISH: [
            ("The results of RHEPY are first calculated by the "
             "highest scoring type in the test. Then, if two types "
             "are tied, the one with the highest scoring wings "
             "takes precedence. Finally, your total score is checked "
             "to see if it matches a set of conditions that correlate with "
             "a particular type, and if it does, that is "
             "your resulting type. So even if your "
             "resulting type is not the highest scoring type in "
             "the test, it's not a mistake!"),
        ],
        PORTUGUESE: [
            ("Os resultados do RHEPY são calculados, primeiro, "
             "pelo tipo com a maior pontuação no teste. Então, "
             "se dois tipos estiverem empatados, o tipo com as "
             "asas de maior pontuação toma prioridade. Por último, "
             "ele checa se sua pontuação geral corresponde a uma "
             "série de condições correlacionadas a um tipo "
             "específico, e se sim, este fica sendo o seu tipo "
             "resultante. Portanto, mesmo que o seu tipo "
             "resultante não seja o de maior pontuação no teste, "
             "isso não é um erro!"),
        ],
    }

    explanation_output = explanation.get(language)
    if explanation_output:
        for paragraph in explanation_output:
            print("\n".join(wrap(paragraph, 80)))
            print("")
    else:
        raise ValueError("Invalid language")


def print_result(language, types):
    """
    Prints the results to the test, with scores
    """
    result = {"type": result_type(types), "wing": result_wing(types)}

    results = {
        ENGLISH: {
            "wing":
            "Your type is likely: " + Fore.RED +
            f"Enneagram Type {result['type']}w{result['wing']}" + Fore.RESET,
            "type":
            "Your type is likely: " + Fore.RED +
            f"Enneagram Type {result['type']} " + Fore.RESET +
            "(wing couldn't be calculated)",
            "score_header":
            "Score:\n",
            "thanks":
            "Thanks for using RHEPY! :)",
            "type_labels": {
                "1": "Type 1",
                "2": "Type 2",
                "3": "Type 3",
                "4": "Type 4",
                "5": "Type 5",
                "6": "Type 6",
                "7": "Type 7",
                "8": "Type 8",
                "9": "Type 9",
            },
        },
        PORTUGUESE: {
            "wing":
            "Seu tipo é provavelmente: " + Fore.RED +
            f"Tipo {result['type']}w{result['wing']} do Eneagrama" +
            Fore.RESET,
            "type":
            "Seu tipo é provavelmente: " + Fore.RED +
            f"Tipo {result['type']} " + Fore.RESET +
            "(asa não pôde ser calculada)",
            "score_header":
            "Pontuação:\n",
            "thanks":
            "Obrigado por usar o RHEPY! :)",
            "type_labels": {
                "1": "Tipo 1",
                "2": "Tipo 2",
                "3": "Tipo 3",
                "4": "Tipo 4",
                "5": "Tipo 5",
                "6": "Tipo 6",
                "7": "Tipo 7",
                "8": "Tipo 8",
                "9": "Tipo 9",
            },
        },
    }

    result_output = results.get(language)
    if result_output:
        print("RESULTS:\n" if language == ENGLISH else "RESULTADOS:\n")

        if result["wing"] > 0:
            print(result_output["wing"])
        elif result["wing"] == 0:
            print(result_output["type"])

        print("\n" + result_output["score_header"])
        type_labels = result_output["type_labels"]

        print("\t".join([
            type_labels["1"] + ": " + str(types['d_1']),
            type_labels["2"] + ": " + str(types['f_2']),
            type_labels["3"] + ": " + str(types['c_3'])
        ]))
        print("\t".join([
            type_labels["4"] + ": " + str(types['e_4']),
            type_labels["5"] + ": " + str(types['h_5']),
            type_labels["6"] + ": " + str(types['b_6'])
        ]))
        print("\t".join([
            type_labels["7"] + ": " + str(types['i_7']),
            type_labels["8"] + ": " + str(types['g_8']),
            type_labels["9"] + ": " + str(types['a_9'])
        ]))

        print("\n" + result_output["thanks"])
    else:
        raise ValueError("Invalid language")
