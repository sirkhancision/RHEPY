#!/usr/bin/env python3

import constants as consts
from ansiwrap import *

question_number = 1


def statement(
    statement_1, statement_2, option_1, option_2, statement_1_type, statement_2_type
):
    """
    The template for all statements of the test

    It formats the statements given, reads user input based on the options provided, and increases the score accordingly

    Returns a tuple
    """
    global question_number
    statement_1_wrapped = wrap(f"{question_number}. {statement_1} [{option_1}]", 80)
    statement_2_wrapped = wrap(f"{statement_2} [{option_2}]", 80)

    print("")
    print("\n".join(statement_1_wrapped))
    print("\n".join(statement_2_wrapped))
    question_number += 1

    while True:
        answer = input().upper()

        if answer == option_1:
            statement_1_type += 1
            return statement_1_type, statement_2_type
        elif answer == option_2:
            statement_2_type += 1
            return statement_1_type, statement_2_type
        elif answer == ">":
            return statement_1_type, statement_2_type
        else:
            continue


def print_statements(language, types):
    """
    Prints all test statements, based on the language chosen, and uses the statements template declared in the function statement()
    """
    match language:
        case consts.ENGLISH:
            # Statement Pair 1
            types["e_4"], types["b_6"] = statement(
                "I've been romantic and imaginative.",
                "I've been pragmatic and down-to-earth.",
                "E",
                "B",
                types["e_4"],
                types["b_6"],
            )

            # Statement Pair 2
            types["g_8"], types["a_9"] = statement(
                "I have tended to take on confrontations.",
                "I have tended to avoid confrontations.",
                "G",
                "A",
                types["g_8"],
                types["a_9"],
            )

            # Statement Pair 3
            types["c_3"], types["d_1"] = statement(
                "I have typically been diplomatic, charming and ambitious.",
                "I have typically been direct, formal and idealistic.",
                "C",
                "D",
                types["c_3"],
                types["d_1"],
            )

            # Statement Pair 4
            types["h_5"], types["i_7"] = statement(
                "I have tended to be focused and intense.",
                "I have tended to be spontaneous and fun-loving.",
                "H",
                "I",
                types["h_5"],
                types["i_7"],
            )

            # Statement Pair 5
            types["f_2"], types["e_4"] = statement(
                "I have been a hospitable person and have enjoyed welcoming new "
                "friends into my life.",
                "I have been a private person and have not mixed much with others.",
                "F",
                "E",
                types["f_2"],
                types["e_4"],
            )

            # Statement Pair 6
            types["b_6"], types["a_9"] = statement(
                "It's been difficult for me to relax and stop worrying about "
                "potential problems.",
                "It's been difficult for me to get myself worked up about "
                "potential problems.",
                "B",
                "A",
                types["b_6"],
                types["a_9"],
            )

            # Statement Pair 7
            types["g_8"], types["d_1"] = statement(
                'I\'ve been more of a "street-smart" survivor.',
                'I\'ve been more of a "high-minded" idealist.',
                "G",
                "D",
                types["g_8"],
                types["d_1"],
            )

            # Statement Pair 8
            types["f_2"], types["h_5"] = statement(
                "I have needed to show affection to people.",
                "I have preferred to maintain some distance with people.",
                "F",
                "H",
                types["f_2"],
                types["h_5"],
            )

            # Statement Pair 9
            types["c_3"], types["i_7"] = statement(
                "When presented with a new experience, I've usually asked "
                "myself if it would be useful to me.",
                "When presented with a new experience, I've usually asked myself "
                "if it would be enjoyable.",
                "C",
                "I",
                types["c_3"],
                types["i_7"],
            )

            # Statement Pair 10
            types["e_4"], types["a_9"] = statement(
                "I have tended to focus too much on myself.",
                "I have tended to focus too much on others.",
                "E",
                "A",
                types["e_4"],
                types["a_9"],
            )

            # Statement Pair 11
            types["h_5"], types["g_8"] = statement(
                "Others have depended on my insight and knowledge.",
                "Others have depended on my strength and decisiveness.",
                "H",
                "G",
                types["h_5"],
                types["g_8"],
            )

            # Statement Pair 12
            types["b_6"], types["d_1"] = statement(
                "I have come across as being too unsure of myself.",
                "I have come across as being too sure of myself.",
                "B",
                "D",
                types["b_6"],
                types["d_1"],
            )

            # Statement Pair 13
            types["f_2"], types["c_3"] = statement(
                "I have been more relationship-oriented than goal-oriented.",
                "I have been more goal-oriented than relationship-oriented.",
                "F",
                "C",
                types["f_2"],
                types["c_3"],
            )

            # Statement Pair 14
            types["e_4"], types["i_7"] = statement(
                "I have not been able to speak up for myself very well.",
                "I have been outspoken – I've said what others wished they had "
                "the nerve to say.",
                "E",
                "I",
                types["e_4"],
                types["i_7"],
            )

            # Statement Pair 15
            types["h_5"], types["d_1"] = statement(
                "It's been difficult for me to stop considering alternatives and do "
                "something definite.",
                "It's been difficult for me to take it easy and be more flexible.",
                "H",
                "D",
                types["h_5"],
                types["d_1"],
            )

            # Statement Pair 16
            types["b_6"], types["g_8"] = statement(
                "I have tended to be careful and hesitant.",
                "I have tended to be bold and domineering.",
                "B",
                "G",
                types["b_6"],
                types["g_8"],
            )

            # Statement Pair 17
            types["a_9"], types["f_2"] = statement(
                "My reluctance to get too involved has gotten me into trouble "
                "with people.",
                "My eagerness to have people depend on me has gotten me into "
                "trouble with them.",
                "A",
                "F",
                types["a_9"],
                types["f_2"],
            )

            # Statement Pair 18
            types["c_3"], types["e_4"] = statement(
                "Usually, I have been able to put my feelings aside to get the "
                "job done.",
                "Usually, I have needed to work through my feelings before I "
                "could act.",
                "C",
                "E",
                types["c_3"],
                types["e_4"],
            )

            # Statement Pair 19
            types["b_6"], types["i_7"] = statement(
                "Generally, I've been methodical and cautious.",
                "Generally, I've been adventurous and taken risks.",
                "B",
                "I",
                types["b_6"],
                types["i_7"],
            )

            # Statement Pair 20
            types["f_2"], types["d_1"] = statement(
                "I have tended to be a supportive, giving person who seeks "
                "intimacy with others.",
                "I have tended to be a serious, reserved person who likes "
                "discussing issues.",
                "F",
                "D",
                types["f_2"],
                types["d_1"],
            )

            # Statement Pair 21
            types["g_8"], types["c_3"] = statement(
                'I\'ve often felt the need to be a "pillar of strength".',
                "I've often felt the need to perform perfectly.",
                "G",
                "C",
                types["g_8"],
                types["c_3"],
            )

            # Statement Pair 22
            types["h_5"], types["a_9"] = statement(
                "I've typically been interested in asking tough questions and "
                "maintaining my independence.",
                "I've typically been interested in maintaining my stability and "
                "peace of mind.",
                "H",
                "A",
                types["h_5"],
                types["a_9"],
            )

            # Statement Pair 23
            types["b_6"], types["f_2"] = statement(
                "I've been a bit cynical and skeptical.",
                "I've been a bit mushy and sentimental.",
                "B",
                "F",
                types["b_6"],
                types["f_2"],
            )

            # Statement Pair 24
            types["i_7"], types["g_8"] = statement(
                "I've often worried that I'm missing out on something better.",
                "I've often worried that if I let down my guard, someone will take "
                "advantage of me.",
                "I",
                "G",
                types["i_7"],
                types["g_8"],
            )

            # Statement Pair 25
            types["e_4"], types["d_1"] = statement(
                'My habit of being "stand-offish" has annoyed people.',
                "My habit of telling people what to do has annoyed people.",
                "E",
                "D",
                types["e_4"],
                types["d_1"],
            )

            # Statement Pair 26
            types["a_9"], types["i_7"] = statement(
                "I have tended to get anxious if there was too much excitement and "
                "stimulation.",
                "I have tended to get anxious if there wasn't enough excitement and "
                "stimulation.",
                "A",
                "I",
                types["a_9"],
                types["i_7"],
            )

            # Statement Pair 27
            types["b_6"], types["c_3"] = statement(
                "I have depended on my friends and they have known that they "
                "can depend on me.",
                "I have not depended on people, I have done things on my own.",
                "B",
                "C",
                types["b_6"],
                types["c_3"],
            )

            # Statement Pair 28
            types["h_5"], types["e_4"] = statement(
                "I have tended to be detached and preoccupied.",
                "I have tended to be moody and self-absorbed.",
                "H",
                "E",
                types["h_5"],
                types["e_4"],
            )

            # Statement Pair 29
            types["g_8"], types["f_2"] = statement(
                'I have liked to challenge people and "shake them up".',
                "I have liked to comfort people and calm them down.",
                "G",
                "F",
                types["g_8"],
                types["f_2"],
            )

            # Statement Pair 30
            types["i_7"], types["d_1"] = statement(
                "I have generally been an outgoing, sociable person.",
                "I have generally been an earnest, self-disciplined person.",
                "I",
                "D",
                types["i_7"],
                types["d_1"],
            )

            # Statement Pair 31
            types["a_9"], types["c_3"] = statement(
                'I\'ve wanted to "fit in" with others – I get uncomfortable '
                "when I stand out too much.",
                "I've wanted to stand out from others – I get uncomfortable when "
                "I don't distinguish myself.",
                "A",
                "C",
                types["a_9"],
                types["c_3"],
            )

            # Statement Pair 32
            types["h_5"], types["b_6"] = statement(
                "Pursuing my personal interests has been more important to me "
                "than having stability and security.",
                "Having stability and security has been more important to me than "
                "pursuing my personal interests.",
                "H",
                "B",
                types["h_5"],
                types["b_6"],
            )

            # Statement Pair 33
            types["e_4"], types["g_8"] = statement(
                "When I've had conflicts with others, I've tended to withdraw.",
                "When I've had conflicts with others, I've rarely backed down.",
                "E",
                "G",
                types["e_4"],
                types["g_8"],
            )

            # Statement Pair 34
            types["a_9"], types["d_1"] = statement(
                "I have given in too easily and let others push me around.",
                "I have been too uncompromising and demanding with others.",
                "A",
                "D",
                types["a_9"],
                types["d_1"],
            )

            # Statement Pair 35
            types["i_7"], types["f_2"] = statement(
                "I've been appreciated for my unsinkable spirit and resourcefulness.",
                "I've been appreciated for my deep caring and personal warmth.",
                "I",
                "F",
                types["i_7"],
                types["f_2"],
            )

            # Statement Pair 36
            types["c_3"], types["h_5"] = statement(
                "I have wanted to make a favorable impression on others.",
                "I have cared little about making a favorable impression on others.",
                "C",
                "H",
                types["c_3"],
                types["h_5"],
            )

            # Statement Pair 37
            types["b_6"], types["e_4"] = statement(
                "I've depended on my perseverance and common sense.",
                "I've depended on my imagination and moments of inspiration.",
                "B",
                "E",
                types["b_6"],
                types["e_4"],
            )

            # Statement Pair 38
            types["a_9"], types["g_8"] = statement(
                "Basically, I have been easy-going and agreeable.",
                "Basically, I have been hard-driving and assertive.",
                "A",
                "G",
                types["a_9"],
                types["g_8"],
            )

            # Statement Pair 39
            types["c_3"], types["d_1"] = statement(
                "I have worked hard to be accepted and well-liked.",
                "Being accepted and well-liked has not been a high priority for me.",
                "C",
                "D",
                types["c_3"],
                types["d_1"],
            )

            # Statement Pair 40
            types["h_5"], types["i_7"] = statement(
                "In reaction to pressure from others, I have become more withdrawn.",
                "In reaction to pressure from others, I have become more assertive.",
                "H",
                "I",
                types["h_5"],
                types["i_7"],
            )

            # Statement Pair 41
            types["f_2"], types["e_4"] = statement(
                "People have been interested in me because I've been outgoing, "
                "engaging, and interested in them.",
                "People have been interested in me because I've been quiet, "
                "unusual and deep.",
                "F",
                "E",
                types["f_2"],
                types["e_4"],
            )

            # Statement Pair 42
            types["b_6"], types["a_9"] = statement(
                "Duty and responsibility have been important values for me.",
                "Harmony and acceptance have been important values for me.",
                "B",
                "A",
                types["b_6"],
                types["a_9"],
            )

            # Statement Pair 43
            types["g_8"], types["d_1"] = statement(
                "I've tried to motivate people by making big plans and big promises.",
                "I've tried to motivate people by pointing out the consequences of not "
                "following my advice.",
                "G",
                "D",
                types["g_8"],
                types["d_1"],
            )

            # Statement Pair 44
            types["h_5"], types["f_2"] = statement(
                "I have seldom been emotionally demonstrative.",
                "I have often been emotionally demonstrative.",
                "H",
                "F",
                types["h_5"],
                types["f_2"],
            )

            # Statement Pair 45
            types["i_7"], types["c_3"] = statement(
                "Dealing with details has not been one of my strong suits.",
                "I have excelled at dealing with details.",
                "I",
                "C",
                types["i_7"],
                types["c_3"],
            )

            # Statement Pair 46
            types["e_4"], types["a_9"] = statement(
                "I have often emphasized how different I am from other people, "
                "especially my family.",
                "I have often emphasized how much I have in common with most "
                "people, especially my family.",
                "E",
                "A",
                types["e_4"],
                types["a_9"],
            )

            # Statement Pair 47
            types["h_5"], types["g_8"] = statement(
                "When situations have gotten heated, I have tended to stay on "
                "the sidelines.",
                "When situations have gotten heated, I have tended to get right "
                "into the middle of things.",
                "H",
                "G",
                types["h_5"],
                types["g_8"],
            )

            # Statement Pair 48
            types["b_6"], types["d_1"] = statement(
                "I have stood by my friends, even when they have been wrong.",
                "I have not wanted to compromise what is right, even for friendship.",
                "B",
                "D",
                types["b_6"],
                types["d_1"],
            )

            # Statement Pair 49
            types["f_2"], types["c_3"] = statement(
                "I've been a well-meaning supporter.",
                "I've been a highly-motivated go-getter.",
                "F",
                "C",
                types["f_2"],
                types["c_3"],
            )

            # Statement Pair 50
            types["e_4"], types["i_7"] = statement(
                "When troubled, I have tended to brood about my problems.",
                "When troubled, I have tended to find distractions for myself.",
                "E",
                "I",
                types["e_4"],
                types["i_7"],
            )

            # Statement Pair 51
            types["d_1"], types["h_5"] = statement(
                "Generally, I've had strong convictions and a sense of how things "
                "should be.",
                "Generally, I've had serious doubts and have questioned how things "
                "seemed to be.",
                "D",
                "H",
                types["d_1"],
                types["h_5"],
            )

            # Statement Pair 52
            types["b_6"], types["g_8"] = statement(
                "I've created problems with others by being pessimistic and "
                "complaining.",
                "I've created problems with others by being bossy and controlling.",
                "B",
                "G",
                types["b_6"],
                types["g_8"],
            )

            # Statement Pair 53
            types["f_2"], types["a_9"] = statement(
                'I have tended to act on my feelings and let the "chips fall '
                'where they may".',
                "I have tended not to act on my feelings lest they stir up more "
                "problems.",
                "F",
                "A",
                types["f_2"],
                types["a_9"],
            )

            # Statement Pair 54
            types["c_3"], types["e_4"] = statement(
                "Being the center of attention has usually felt natural to me.",
                "Being the center of attention has usually felt strange to me.",
                "C",
                "E",
                types["c_3"],
                types["e_4"],
            )

            # Statement Pair 55
            types["b_6"], types["i_7"] = statement(
                "I've been careful and have tried to prepare for unforeseen "
                "problems.",
                "I've been spontaneous and have preferred to improvise as "
                "problems come up.",
                "B",
                "I",
                types["b_6"],
                types["i_7"],
            )

            # Statement Pair 56
            types["f_2"], types["d_1"] = statement(
                "I have gotten angry when others have not shown enough "
                "appreciation for what I have done for them.",
                "I have gotten angry when others have not listened to what I have "
                "told them.",
                "F",
                "D",
                types["f_2"],
                types["d_1"],
            )

            # Statement Pair 57
            types["g_8"], types["c_3"] = statement(
                "Being independent and self-reliant has been important to me.",
                "Being valued and admired has been important to me.",
                "G",
                "C",
                types["g_8"],
                types["c_3"],
            )

            # Statement Pair 58
            types["h_5"], types["a_9"] = statement(
                "When I've debated with friends, I've tended to press my arguments "
                "forcefully.",
                "When I've debated with friends, I've tended to let things go to "
                "prevent hard feelings.",
                "H",
                "A",
                types["h_5"],
                types["a_9"],
            )

            # Statement Pair 59
            types["f_2"], types["b_6"] = statement(
                "I have often been possessive of loved ones – I have had "
                "trouble letting them be.",
                'I have often "tested" loved ones to see if they were really '
                "there for me.",
                "F",
                "B",
                types["f_2"],
                types["b_6"],
            )

            # Statement Pair 60
            types["g_8"], types["i_7"] = statement(
                "Organizing resources and making things happen has been one of "
                "my major strengths.",
                "Coming up with new ideas and getting people excited about them "
                "has been one of my major strengths.",
                "G",
                "I",
                types["g_8"],
                types["i_7"],
            )

            # Statement Pair 61
            types["d_1"], types["e_4"] = statement(
                "I've tended to be driven and very hard on myself.",
                "I've tended to be too emotional and rather undisciplined.",
                "D",
                "E",
                types["d_1"],
                types["e_4"],
            )

            # Statement Pair 62
            types["i_7"], types["a_9"] = statement(
                "I have tried to keep my life fast-paced, intense, and exciting.",
                "I have tried to keep my life regular, stable, and peaceful.",
                "I",
                "A",
                types["i_7"],
                types["a_9"],
            )

            # Statement Pair 63
            types["b_6"], types["c_3"] = statement(
                "Even though I've had successes, I've tended to doubt my " "abilities.",
                "Even though I've had setbacks, I've had a lot of confidence in "
                "my abilities.",
                "B",
                "C",
                types["b_6"],
                types["c_3"],
            )

            # Statement Pair 64
            types["e_4"], types["h_5"] = statement(
                "I generally have tended to dwell on my feelings and to hold "
                "onto them for a long time.",
                "I generally have tended to minimize my feelings and not pay very "
                "much attention to them.",
                "E",
                "H",
                types["e_4"],
                types["h_5"],
            )

            # Statement Pair 65
            types["f_2"], types["g_8"] = statement(
                "I have provided many people with attention and nurturance.",
                "I have provided many people with direction and motivation.",
                "F",
                "G",
                types["f_2"],
                types["g_8"],
            )

            # Statement Pair 66
            types["d_1"], types["i_7"] = statement(
                "I've been a bit serious and strict with myself.",
                "I've been a bit free-wheeling and permissive with myself.",
                "D",
                "I",
                types["d_1"],
                types["i_7"],
            )

            # Statement Pair 67
            types["c_3"], types["a_9"] = statement(
                "I've been self-assertive and driven to excel.",
                "I've been modest and have been happy to go at my own pace.",
                "C",
                "A",
                types["c_3"],
                types["a_9"],
            )

            # Statement Pair 68
            types["h_5"], types["b_6"] = statement(
                "I have been proud of my clarity and objectivity.",
                "I have been proud of my reliability and commitment.",
                "H",
                "B",
                types["h_5"],
                types["b_6"],
            )

            # Statement Pair 69
            types["e_4"], types["g_8"] = statement(
                "I have spent a lot of time looking inward – understanding my "
                "feelings has been important to me.",
                "I have not spent much time looking inward – getting things done "
                "has been important to me.",
                "E",
                "G",
                types["e_4"],
                types["g_8"],
            )

            # Statement Pair 70
            types["a_9"], types["d_1"] = statement(
                "Generally, I have thought of myself as a sunny, casual person.",
                "Generally, I have thought of myself as a serious, dignified person.",
                "A",
                "D",
                types["a_9"],
                types["d_1"],
            )

            # Statement Pair 71
            types["i_7"], types["f_2"] = statement(
                "I've had an agile mind and boundless energy.",
                "I've had a caring heart and deep dedication.",
                "I",
                "F",
                types["i_7"],
                types["f_2"],
            )

            # Statement Pair 72
            types["c_3"], types["h_5"] = statement(
                "I have pursued activities that had a substantial potential "
                "for reward and personal recognition.",
                "I have been willing to give up reward and personal recognition "
                "if it meant doing work I was really interested in.",
                "C",
                "H",
                types["c_3"],
                types["h_5"],
            )

            # Statement Pair 73
            types["e_4"], types["b_6"] = statement(
                "Fulfilling social obligations has seldom been high on my agenda.",
                "I have usually taken my social obligations very seriously.",
                "E",
                "B",
                types["e_4"],
                types["b_6"],
            )

            # Statement Pair 74
            types["g_8"], types["a_9"] = statement(
                "In most situations, I have preferred to take the lead.",
                "In most situations, I have preferred to let someone else take "
                "the lead.",
                "G",
                "A",
                types["g_8"],
                types["a_9"],
            )

            # Statement Pair 75
            types["c_3"], types["d_1"] = statement(
                "Over the years, my values and lifestyle have changed several "
                "times.",
                "Over the years, my values and lifestyle have remained fairly "
                "consistent.",
                "C",
                "D",
                types["c_3"],
                types["d_1"],
            )

            # Statement Pair 76
            types["i_7"], types["h_5"] = statement(
                "Typically, I have not had much self-discipline.",
                "Typically, I have not had much connection with people.",
                "I",
                "H",
                types["i_7"],
                types["h_5"],
            )

            # Statement Pair 77
            types["e_4"], types["f_2"] = statement(
                "I have tended to withhold my affection and have wanted others "
                "to come into my world.",
                "I have tended to give my affection too freely and have wanted to "
                "extend myself to others.",
                "E",
                "F",
                types["e_4"],
                types["f_2"],
            )

            # Statement Pair 78
            types["b_6"], types["a_9"] = statement(
                "I have had a tendency to think of worst-case scenarios.",
                "I have had a tendency to think that everything will work out for "
                "the best.",
                "B",
                "A",
                types["b_6"],
                types["a_9"],
            )

            # Statement Pair 79
            types["g_8"], types["d_1"] = statement(
                "People have trusted me because I am confident and can look out for "
                "them.",
                "People have trusted me because I am fair and will do what is right.",
                "G",
                "D",
                types["g_8"],
                types["d_1"],
            )

            # Statement Pair 80
            types["h_5"], types["f_2"] = statement(
                "Often, I have been so involved in my own projects that I have "
                "become isolated from others.",
                "Often, I have been so involved with others that I have neglected "
                "my own projects.",
                "H",
                "F",
                types["h_5"],
                types["f_2"],
            )

            # Statement Pair 81
            types["c_3"], types["i_7"] = statement(
                "When meeting someone new, I have usually been poised and "
                "self-contained.",
                "When meeting someone new, I have usually been chatty and "
                "entertaining.",
                "C",
                "I",
                types["c_3"],
                types["i_7"],
            )

            # Statement Pair 82
            types["e_4"], types["a_9"] = statement(
                "Generally speaking, I have tended to be pessimistic.",
                "Generally speaking, I have tended to be optimistic.",
                "E",
                "A",
                types["e_4"],
                types["a_9"],
            )

            # Statement Pair 83
            types["h_5"], types["g_8"] = statement(
                "I have preferred to inhabit my own little world.",
                "I have preferred to let the world know I'm here.",
                "H",
                "G",
                types["h_5"],
                types["g_8"],
            )

            # Statement Pair 84
            types["b_6"], types["d_1"] = statement(
                "I have often been troubled by nervousness, insecurity, and doubt.",
                "I have often been troubled by anger, perfectionism, and impatience.",
                "B",
                "D",
                types["b_6"],
                types["d_1"],
            )

            # Statement Pair 85
            types["f_2"], types["c_3"] = statement(
                "I realize that I have often been too personal and intimate.",
                "I realize that I have often been too cool and aloof.",
                "F",
                "C",
                types["f_2"],
                types["c_3"],
            )

            # Statement Pair 86
            types["e_4"], types["i_7"] = statement(
                "I have lost out because I have not felt up to taking opportunities.",
                "I have lost out because I have pursued too many possibilities.",
                "E",
                "I",
                types["e_4"],
                types["i_7"],
            )

            # Statement Pair 87
            types["h_5"], types["d_1"] = statement(
                "I have tended to take a long time to get into action.",
                "I have tended to get into action quickly.",
                "H",
                "D",
                types["h_5"],
                types["d_1"],
            )

            # Statement Pair 88
            types["b_6"], types["g_8"] = statement(
                "I usually have had difficulty making decisions.",
                "I seldom have had difficulty making decisions.",
                "B",
                "G",
                types["b_6"],
                types["g_8"],
            )

            # Statement Pair 89
            types["f_2"], types["a_9"] = statement(
                "I have had a tendency to come on a little too strong with people.",
                "I have had a tendency not to assert myself enough with people.",
                "F",
                "A",
                types["f_2"],
                types["a_9"],
            )

            # Statement Pair 90
            types["c_3"], types["e_4"] = statement(
                "Typically, I have been even-tempered.",
                "Typically, I have had strong changes of mood.",
                "C",
                "E",
                types["c_3"],
                types["e_4"],
            )

            # Statement Pair 91
            types["b_6"], types["i_7"] = statement(
                "When I've been unsure of what to do, I've often sought the "
                "advice of others.",
                "When I've been unsure of what to do, I've tried different things "
                "to see what worked best for me.",
                "B",
                "I",
                types["b_6"],
                types["i_7"],
            )

            # Statement Pair 92
            types["f_2"], types["d_1"] = statement(
                "I have worried that I would be left out of others' activities.",
                "I have worried that others' activities would distract me from what I "
                "had to do.",
                "F",
                "D",
                types["f_2"],
                types["d_1"],
            )

            # Statement Pair 93
            types["g_8"], types["c_3"] = statement(
                "Typically, when I have gotten angry, I have told people off.",
                "Typically, when I have gotten angry, I have become distant.",
                "G",
                "C",
                types["g_8"],
                types["c_3"],
            )

            # Statement Pair 94
            types["h_5"], types["a_9"] = statement(
                "I've tended to have trouble falling asleep.",
                "I've tended to fall asleep easily.",
                "H",
                "A",
                types["h_5"],
                types["a_9"],
            )

            # Statement Pair 95
            types["f_2"], types["b_6"] = statement(
                "I have often tried to figure out how I could get closer to " "others.",
                "I have often tried to figure out what others want from me.",
                "F",
                "B",
                types["f_2"],
                types["b_6"],
            )

            # Statement Pair 96
            types["g_8"], types["i_7"] = statement(
                "I have usually been measured, straight-talking, and deliberate.",
                "I have usually been excitable, fast-talking, and witty.",
                "G",
                "I",
                types["g_8"],
                types["i_7"],
            )

            # Statement Pair 97
            types["e_4"], types["d_1"] = statement(
                "Often, I have not spoken up when I've seen others making a mistake.",
                "Often, I have helped others see that they are making a mistake.",
                "E",
                "D",
                types["e_4"],
                types["d_1"],
            )

            # Statement Pair 98
            types["i_7"], types["a_9"] = statement(
                "During most of my life, I have been a stormy person who has "
                "had many volatile feelings.",
                "During most of my life, I have been a steady person in whom "
                '"still waters run deep".',
                "I",
                "A",
                types["i_7"],
                types["a_9"],
            )

            # Statement Pair 99
            types["c_3"], types["b_6"] = statement(
                "When I have disliked people, I have usually tried hard to stay "
                "cordial – despite my feelings.",
                "When I have disliked people, I have usually let them know it – "
                "one way or another.",
                "C",
                "B",
                types["c_3"],
                types["b_6"],
            )

            # Statement Pair 100
            types["e_4"], types["h_5"] = statement(
                "Much of my difficulty with people has come from my "
                "touchiness and taking everything too personally.",
                "Much of my difficulty with people has come from me not caring "
                "about social conventions.",
                "E",
                "H",
                types["e_4"],
                types["h_5"],
            )

            # Statement Pair 101
            types["f_2"], types["g_8"] = statement(
                "My approach has been to jump in and rescue people.",
                "My approach has been to show people how to help themselves.",
                "F",
                "G",
                types["f_2"],
                types["g_8"],
            )

            # Statement Pair 102
            types["i_7"], types["d_1"] = statement(
                'Generally, I have enjoyed "letting go" and pushing the limits.',
                "Generally, I have not enjoyed losing control of myself very much.",
                "I",
                "D",
                types["i_7"],
                types["d_1"],
            )

            # Statement Pair 103
            types["c_3"], types["a_9"] = statement(
                "I've been overly concerned with doing better than others.",
                "I've been overly concerned with making things okay for others.",
                "C",
                "A",
                types["c_3"],
                types["a_9"],
            )

            # Statement Pair 104
            types["h_5"], types["b_6"] = statement(
                "My thoughts generally have been speculative involving my "
                "imagination and curiosity.",
                "My thoughts generally have been practical – just trying to keep "
                "things going.",
                "H",
                "B",
                types["h_5"],
                types["b_6"],
            )

            # Statement Pair 105
            types["g_8"], types["e_4"] = statement(
                "One of my main assets has been my ability to take charge of "
                "situations.",
                "One of my main assets has been my ability to describe internal "
                "states.",
                "G",
                "E",
                types["g_8"],
                types["e_4"],
            )

            # Statement Pair 106
            types["d_1"], types["a_9"] = statement(
                "I have pushed to get things done correctly, even if it made people "
                "uncomfortable.",
                "I have not liked feeling pressured, so I have not liked pressuring "
                "anyone else.",
                "D",
                "A",
                types["d_1"],
                types["a_9"],
            )

            # Statement Pair 107
            types["f_2"], types["i_7"] = statement(
                "I've often taken pride in how important I am in others' lives.",
                "I've often taken pride in my gusto and openness to new experiences.",
                "F",
                "I",
                types["f_2"],
                types["i_7"],
            )

            # Statement Pair 108
            types["c_3"], types["h_5"] = statement(
                "I have perceived that I've often come across to others as "
                "presentable, even admirable.",
                "I have perceived that I've often come across to others as "
                "unusual, even odd.",
                "C",
                "H",
                types["c_3"],
                types["h_5"],
            )

            # Statement Pair 109
            types["b_6"], types["e_4"] = statement(
                "I've mostly done what I had to do.",
                "I've mostly done what I wanted to do.",
                "B",
                "E",
                types["b_6"],
                types["e_4"],
            )

            # Statement Pair 110
            types["g_8"], types["a_9"] = statement(
                "I have usually enjoyed high-pressure, even difficult, " "situations.",
                "I have usually disliked being in high-pressure, even difficult, "
                "situations.",
                "G",
                "A",
                types["g_8"],
                types["a_9"],
            )

            # Statement Pair 111
            types["c_3"], types["d_1"] = statement(
                "I've been proud of my ability to be flexible – what's "
                "appropriate or important often changes.",
                "I've been proud of my ability to take a stand – I've been firm "
                "about what I believe in.",
                "C",
                "D",
                types["c_3"],
                types["d_1"],
            )

            # Statement Pair 112
            types["h_5"], types["i_7"] = statement(
                "My style has leaned towards spareness and austerity.",
                "My style has leaned towards excess and overdoing things.",
                "H",
                "I",
                types["h_5"],
                types["i_7"],
            )

            # Statement Pair 113
            types["f_2"], types["e_4"] = statement(
                "My own health and well-being have suffered because of my "
                "strong desire to help others.",
                "My relationships have suffered because of my strong desire to "
                "attend to my personal needs.",
                "F",
                "E",
                types["f_2"],
                types["e_4"],
            )

            # Statement Pair 114
            types["a_9"], types["b_6"] = statement(
                "Generally speaking, I've been too open and naive.",
                "Generally speaking, I've been too wary and guarded.",
                "A",
                "B",
                types["a_9"],
                types["b_6"],
            )

            # Statement Pair 115
            types["g_8"], types["d_1"] = statement(
                "I have sometimes put people off by being too aggressive.",
                'I have sometimes put people off by being too "uptight".',
                "G",
                "D",
                types["g_8"],
                types["d_1"],
            )

            # Statement Pair 116
            types["f_2"], types["h_5"] = statement(
                "Being of service and attending to the needs of others has "
                "been a high priority for me.",
                "Finding alternative ways of seeing and doing things has been a "
                "high priority for me.",
                "F",
                "H",
                types["f_2"],
                types["h_5"],
            )

            # Statement Pair 117
            types["c_3"], types["i_7"] = statement(
                "I've been single-minded and persistent in pursuing my goals.",
                "I've preferred to explore various courses of action to see where they "
                "lead.",
                "C",
                "I",
                types["c_3"],
                types["i_7"],
            )

            # Statement Pair 118
            types["e_4"], types["a_9"] = statement(
                "I have frequently been drawn to situations that stir up deep, "
                "intense emotions.",
                "I have frequently been drawn to situations that make me feel calm and "
                "at ease.",
                "E",
                "A",
                types["e_4"],
                types["a_9"],
            )

            # Statement Pair 119
            types["h_5"], types["g_8"] = statement(
                "I have cared less about practical results than about pursuing my "
                "interests.",
                "I have been practical and have expected my work to have concrete "
                "results.",
                "H",
                "G",
                types["h_5"],
                types["g_8"],
            )

            # Statement Pair 120
            types["b_6"], types["d_1"] = statement(
                "I have had a deep need to belong.",
                "I have had a deep need to feel balanced.",
                "B",
                "D",
                types["b_6"],
                types["d_1"],
            )

            # Statement Pair 121
            types["f_2"], types["c_3"] = statement(
                "In the past, I've probably insisted on too much closeness in my "
                "friendships.",
                "In the past, I've probably kept too much distance in my "
                "relationships.",
                "F",
                "C",
                types["f_2"],
                types["c_3"],
            )

            # Statement Pair 122
            types["e_4"], types["i_7"] = statement(
                "I've had a tendency to keep thinking about things from the past.",
                "I've had a tendency to keep anticipating things I'm going to do.",
                "E",
                "I",
                types["e_4"],
                types["i_7"],
            )

            # Statement Pair 123
            types["h_5"], types["d_1"] = statement(
                "I've tended to see people as intrusive and demanding.",
                "I've tended to see people as disorganized and irresponsible.",
                "H",
                "D",
                types["h_5"],
                types["d_1"],
            )

            # Statement Pair 124
            types["b_6"], types["g_8"] = statement(
                "Generally, I have not had much confidence in myself.",
                "Generally, I have had confidence only in myself.",
                "B",
                "G",
                types["b_6"],
                types["g_8"],
            )

            # Statement Pair 125
            types["a_9"], types["f_2"] = statement(
                "I've probably been too passive and uninvolved.",
                "I've probably been too controlling and manipulative.",
                "A",
                "F",
                types["a_9"],
                types["f_2"],
            )

            # Statement Pair 126
            types["e_4"], types["c_3"] = statement(
                "I've frequently been stopped in my tracks by my self-doubt.",
                "I've rarely let self-doubt stand in my way.",
                "E",
                "C",
                types["e_4"],
                types["c_3"],
            )

            # Statement Pair 127
            types["i_7"], types["b_6"] = statement(
                "Given a choice between something familiar and something new, "
                "I've usually chosen something new.",
                "I've generally chosen what I knew I already liked: why be "
                "disappointed with something I might not like?",
                "I",
                "B",
                types["i_7"],
                types["b_6"],
            )

            # Statement Pair 128
            types["f_2"], types["d_1"] = statement(
                "I have given a lot of physical contact to reassure others "
                "about how I feel about them.",
                "I have generally felt that real love does not depend on physical "
                "contact.",
                "F",
                "D",
                types["f_2"],
                types["d_1"],
            )

            # Statement Pair 129
            types["g_8"], types["c_3"] = statement(
                "When I've needed to confront someone, I've often been too "
                "harsh and direct.",
                "When I've needed to confront someone, I've often \"beaten around "
                'the bush" too much.',
                "G",
                "C",
                types["g_8"],
                types["c_3"],
            )

            # Statement Pair 130
            types["h_5"], types["a_9"] = statement(
                "I have been attracted to subjects that others would probably find "
                "disturbing, even frightening.",
                "I have preferred not to spend my time dwelling on disturbing, "
                "frightening subjects.",
                "H",
                "A",
                types["h_5"],
                types["a_9"],
            )

            # Statement Pair 131
            types["f_2"], types["b_6"] = statement(
                "I have gotten into trouble with people by being too intrusive and "
                "interfering.",
                "I have gotten into trouble with people by being too evasive and "
                "uncommunicative.",
                "F",
                "B",
                types["f_2"],
                types["b_6"],
            )

            # Statement Pair 132
            types["g_8"], types["i_7"] = statement(
                "I've worried that I don't have the resources to fulfill the "
                "responsibilities "
                "I've taken on.",
                "I've worried that I don't have the self-discipline to focus on "
                "what will really fulfill me.",
                "G",
                "I",
                types["g_8"],
                types["i_7"],
            )

            # Statement Pair 133
            types["e_4"], types["d_1"] = statement(
                "Generally, I've been a highly intuitive, individualistic " "person.",
                "Generally, I've been a highly organized, responsible person.",
                "E",
                "D",
                types["e_4"],
                types["d_1"],
            )

            # Statement Pair 134
            types["a_9"], types["i_7"] = statement(
                "Overcoming inertia has been one of my main problems.",
                "Being unable to slow down has been one of my main problems.",
                "A",
                "I",
                types["a_9"],
                types["i_7"],
            )

            # Statement Pair 135
            types["c_3"], types["b_6"] = statement(
                "When I've felt insecure, I've reacted by becoming arrogant and "
                "dismissive.",
                "When I've felt insecure, I've reacted by becoming defensive and "
                "argumentative.",
                "C",
                "B",
                types["c_3"],
                types["b_6"],
            )

            # Statement Pair 136
            types["h_5"], types["e_4"] = statement(
                "I have generally been open-minded and willing to try new "
                "approaches.",
                "I have generally been self-revealing and willing to share my "
                "feelings with others.",
                "H",
                "E",
                types["h_5"],
                types["e_4"],
            )

            # Statement Pair 137
            types["g_8"], types["f_2"] = statement(
                "I've presented myself to others as tougher than I really am.",
                "I've presented myself to others as caring more than I really do.",
                "G",
                "F",
                types["g_8"],
                types["f_2"],
            )

            # Statement Pair 138
            types["d_1"], types["i_7"] = statement(
                "I usually have followed my conscience and reason.",
                "I usually have followed my feelings and impulses.",
                "D",
                "I",
                types["d_1"],
                types["i_7"],
            )

            # Statement Pair 139
            types["c_3"], types["a_9"] = statement(
                "Serious adversity has made me feel hardened and resolute.",
                "Serious adversity has made me feel discouraged and resign.",
                "C",
                "A",
                types["c_3"],
                types["a_9"],
            )

            # Statement Pair 140
            types["b_6"], types["h_5"] = statement(
                'I usually have made sure that I had some kind of "safety '
                'net" to fall back on.',
                "I usually have chosen to live on the edge and to depend on "
                "others as little as possible.",
                "B",
                "H",
                types["b_6"],
                types["h_5"],
            )

            # Statement Pair 141
            types["g_8"], types["e_4"] = statement(
                "I've had to be strong for others, so I haven't had time to "
                "deal with my feelings and fears.",
                "I've had difficulty coping with my feelings and fears, so it's "
                "been hard for me to be strong for others.",
                "G",
                "E",
                types["g_8"],
                types["e_4"],
            )

            # Statement Pair 142
            types["a_9"], types["d_1"] = statement(
                "I have often wondered why people focus on the negative when there "
                "is so much that's wonderful about life.",
                "I have often wondered why people are so happy when so much in life is "
                "messed up.",
                "A",
                "D",
                types["a_9"],
                types["d_1"],
            )

            # Statement Pair 143
            types["f_2"], types["i_7"] = statement(
                "I have tried hard not to be seen as a selfish person.",
                "I have tried hard not to be seen as a boring person.",
                "F",
                "I",
                types["f_2"],
                types["i_7"],
            )

            # Statement Pair 144
            types["h_5"], types["c_3"] = statement(
                "I have avoided intimacy when I feared I would be overwhelmed "
                "by people's needs and demands.",
                "I have avoided intimacy when I feared I would not be able to "
                "live up to people's expectations of me.",
                "H",
                "C",
                types["h_5"],
                types["c_3"],
            )

        case consts.PORTUGUESE:
            # Par de Frases 1
            types["e_4"], types["b_6"] = statement(
                "Eu tenho sido romântico e imaginativo.",
                "Eu tenho sido pragmático e pé-no-chão.",
                "E",
                "B",
                types["e_4"],
                types["b_6"],
            )

            # Par de Frases 2
            types["g_8"], types["a_9"] = statement(
                "Eu tenho tendido a enfrentar confrontos.",
                "Eu tenho tendido a evitar confrontos.",
                "G",
                "A",
                types["g_8"],
                types["a_9"],
            )

            # Par de Frases 3
            types["c_3"], types["d_1"] = statement(
                "Eu normalmente tenho sido diplomático, encantador e ambicioso.",
                "Eu normalmente tenho sido direto, formal e idealista.",
                "C",
                "D",
                types["c_3"],
                types["d_1"],
            )

            # Par de Frases 4
            types["h_5"], types["i_7"] = statement(
                "Eu tenho tendido a ser focado e intenso.",
                "Eu tenho tendido a ser espontâneo e um amante da diversão.",
                "H",
                "I",
                types["h_5"],
                types["i_7"],
            )

            # Par de Frases 5
            types["f_2"], types["e_4"] = statement(
                "Eu tenho sido uma pessoa hospitaleira e tenho gostado de "
                "receber novos "
                "amigos na minha vida.",
                "Eu tenho sido uma pessoa reservada e não tenho me misturado "
                "muito com os outros.",
                "F",
                "E",
                types["f_2"],
                types["e_4"],
            )

            # Par de Frases 6
            types["b_6"], types["a_9"] = statement(
                "Tem sido difícil para mim relaxar e parar de me preocupar com "
                "possíveis problemas.",
                "Tem sido difícil para mim me agitar com possíveis problemas.",
                "B",
                "A",
                types["b_6"],
                types["a_9"],
            )

            # Par de Frases 7
            types["g_8"], types["d_1"] = statement(
                'Eu tenho sido um sobrevivente com "malícia".',
                'Eu tenho sido um idealista "elevado".',
                "G",
                "D",
                types["g_8"],
                types["d_1"],
            )

            # Par de Frases 8
            types["f_2"], types["h_5"] = statement(
                "Eu precisei demonstrar afeto às pessoas.",
                "Eu precisei manter uma certa distância das pessoas.",
                "F",
                "H",
                types["f_2"],
                types["h_5"],
            )

            # Par de Frases 9
            types["c_3"], types["i_7"] = statement(
                "Quando apresentado a uma nova experiência, eu geralmente me "
                "perguntei se ela seria útil para mim.",
                "Quando apresentado a uma nova experiência, eu geralmente me "
                "perguntei se seria agradável.",
                "C",
                "I",
                types["c_3"],
                types["i_7"],
            )

            # Par de Frases 10
            types["e_4"], types["a_9"] = statement(
                "Eu tenho tendido a focar muito em mim mesmo.",
                "Eu tenho tendido a focar muito nos outros.",
                "E",
                "A",
                types["e_4"],
                types["a_9"],
            )

            # Par de Frases 11
            types["h_5"], types["g_8"] = statement(
                "Os outros têm dependido da minha perspicácia e conhecimento.",
                "Os outros têm dependido da minha força e decisão.",
                "H",
                "G",
                types["h_5"],
                types["g_8"],
            )

            # Par de Frases 12
            types["b_6"], types["d_1"] = statement(
                "Eu tenho dado a impressão de ser muito inseguro.",
                "Eu tenho dado a impressão de ser muito seguro de si.",
                "B",
                "D",
                types["b_6"],
                types["d_1"],
            )

            # Par de Frases 13
            types["f_2"], types["c_3"] = statement(
                "Eu tenho sido mais orientado a relacionamentos do que a " "objetivos.",
                "Eu tenho sido mais orientado a objetivos do que a " "relacionamentos.",
                "F",
                "C",
                types["f_2"],
                types["c_3"],
            )

            # Par de Frases 14
            types["e_4"], types["i_7"] = statement(
                "Eu não tenho conseguido me defender muito bem.",
                "Eu tenho sido franco – eu disse o que os outros desejavam ter a "
                "coragem de dizer.",
                "E",
                "I",
                types["e_4"],
                types["i_7"],
            )

            # Par de Frases 15
            types["h_5"], types["d_1"] = statement(
                "Tem sido difícil para mim parar de considerar alternativas e fazer "
                "algo definitivo.",
                "Tem sido difícil para mim relaxar e ser mais flexível.",
                "H",
                "D",
                types["h_5"],
                types["d_1"],
            )

            # Par de Frases 16
            types["b_6"], types["g_8"] = statement(
                "Eu tenho tendido a ser cuidadoso e hesitante.",
                "Eu tenho tendido a ser audacioso e dominador.",
                "B",
                "G",
                types["b_6"],
                types["g_8"],
            )

            # Par de Frases 17
            types["a_9"], types["f_2"] = statement(
                "Minha relutância em me envolver demais tem me causado problemas com "
                "as pessoas.",
                "Minha vontade de ter as pessoas dependendo de mim tem me causado "
                "problemas com elas.",
                "A",
                "F",
                types["a_9"],
                types["f_2"],
            )

            # Par de Frases 18
            types["c_3"], types["e_4"] = statement(
                "Normalmente, eu tenho sido capaz de deixar meus sentimentos "
                "de lado para cumprir o trabalho.",
                "Normalmente, eu precisei trabalhar nos meus sentimentos antes de "
                "agir.",
                "C",
                "E",
                types["c_3"],
                types["e_4"],
            )

            # Par de Frases 19
            types["b_6"], types["i_7"] = statement(
                "Geralmente, eu tenho sido metódico e cauteloso.",
                "Geralmente, eu tenho sido aventureiro e arriscado.",
                "B",
                "I",
                types["b_6"],
                types["i_7"],
            )

            # Par de Frases 20
            types["f_2"], types["d_1"] = statement(
                "Eu tenho tendido a ser uma pessoa solidária e generosa, que "
                "busca intimidade com os outros.",
                "Eu tenho tendido a ser uma pessoa séria e reservada, que gosta "
                "de discutir questões.",
                "F",
                "D",
                types["f_2"],
                types["d_1"],
            )

            # Par de Frases 21
            types["g_8"], types["c_3"] = statement(
                'Eu frequentemente senti a necessidade de ser um "pilar de ' 'força".',
                "Eu frequentemente senti a necessidade de realizar algo "
                "perfeitamente.",
                "G",
                "C",
                types["g_8"],
                types["c_3"],
            )

            # Par de Frases 22
            types["h_5"], types["a_9"] = statement(
                "Eu normlamente tenho interesse em fazer perguntas difíceis e manter "
                "minha independência.",
                "Eu normalmente tenho interesse em manter minha estabilidade e paz "
                "de espírito.",
                "H",
                "A",
                types["h_5"],
                types["a_9"],
            )

            # Par de Frases 23
            types["b_6"], types["f_2"] = statement(
                "Eu tenho sido um pouco cínico e cético.",
                "Eu tenho sido um pouco sentimental e emotivo.",
                "B",
                "F",
                types["b_6"],
                types["f_2"],
            )

            # Par de Frases 24
            types["i_7"], types["g_8"] = statement(
                "Eu costumo me preocupar em estar perdendo algo melhor.",
                "Eu costumo me preocupar em ser explorado se abaixar minha guarda.",
                "I",
                "G",
                types["i_7"],
                types["g_8"],
            )

            # Par de Frases 25
            types["e_4"], types["d_1"] = statement(
                'Meu hábito de me "excluir" tem irritado as pessoas.',
                "Meu hábito de dizer às pessoas o que fazer tem as irritado.",
                "E",
                "D",
                types["e_4"],
                types["d_1"],
            )

            # Par de Frases 26
            types["a_9"], types["i_7"] = statement(
                "Eu tenho tendido a ficar ansioso se houver muita agitação e "
                "estímulo.",
                "Eu tenho tendido a ficar ansioso se não houver agitação e "
                "estímulo suficientes.",
                "A",
                "I",
                types["a_9"],
                types["i_7"],
            )

            # Par de Frases 27
            types["b_6"], types["c_3"] = statement(
                "Eu tenho dependido dos meus amigos e eles sabem que podem "
                "depender de mim.",
                "Eu não tenho dependido das pessoas, tenho feito as coisas " "sozinho.",
                "B",
                "C",
                types["b_6"],
                types["c_3"],
            )

            # Par de Frases 28
            types["h_5"], types["e_4"] = statement(
                "Eu tenho tendido a ser distante e preocupado.",
                "Eu tenho tendido a ser melancólico e absorto em mim mesmo.",
                "H",
                "E",
                types["h_5"],
                types["e_4"],
            )

            # Par de Frases 29
            types["g_8"], types["f_2"] = statement(
                "Eu gostava de desafiar as pessoas e abalá-las.",
                "Eu gostava de confortar as pessoas e acalmá-las.",
                "G",
                "F",
                types["g_8"],
                types["f_2"],
            )

            # Par de Frases 30
            types["i_7"], types["d_1"] = statement(
                "Eu geralmente fui uma pessoa extrovertida e sociável.",
                "Eu geralmente fui uma pessoa séria e disciplinada.",
                "I",
                "D",
                types["i_7"],
                types["d_1"],
            )

            # Par de Frases 31
            types["a_9"], types["c_3"] = statement(
                'Eu tenho desejado "me encaixar" com os outros – eu fico '
                "desconfortável quando me destaco de mais.",
                "Eu tenho desejado me destacar dos demais – eu fico "
                "desconfortável quando não me distingo.",
                "A",
                "C",
                types["a_9"],
                types["c_3"],
            )

            # Par de Frases 32
            types["h_5"], types["b_6"] = statement(
                "Perseguir meus interesses pessoais tem sido mais importante para mim "
                "do que ter estabilidade e segurança.",
                "Ter estabilidade e segurança tem sido mais importante para mim do que "
                "perseguir meus interesses pessoais.",
                "H",
                "B",
                types["h_5"],
                types["b_6"],
            )

            # Par de Frases 33
            types["e_4"], types["g_8"] = statement(
                "Quando eu tive conflitos com os outros, eu tendi a me afastar.",
                "Quando eu tive conflitos com os outros, raramente recuei.",
                "E",
                "G",
                types["e_4"],
                types["g_8"],
            )

            # Par de Frases 34
            types["a_9"], types["d_1"] = statement(
                "Eu tenho cedido muito facilmente e deixado que os outros me "
                "dominem.",
                "Eu tenho sido muito inflexível e exigente com os outros.",
                "A",
                "D",
                types["a_9"],
                types["d_1"],
            )

            # Par de Frases 35
            types["i_7"], types["f_2"] = statement(
                "Eu tenho sido apreciado pela minha determinação e " "desenvoltura.",
                "Eu tenho sido apreciado pela minha preocupação e calor humano "
                "pessoal.",
                "I",
                "F",
                types["i_7"],
                types["f_2"],
            )

            # Par de Frases 36
            types["c_3"], types["h_5"] = statement(
                "Eu tenho desejado causar uma boa impressão aos outros.",
                "Eu não tenho me importado muito em causar uma boa impressão aos "
                "outros.",
                "C",
                "H",
                types["c_3"],
                types["h_5"],
            )

            # Par de Frases 37
            types["b_6"], types["e_4"] = statement(
                "Eu tenho dependido da minha perseverança e bom senso.",
                "Eu tenho dependido da minha imaginação e momentos de inspiração.",
                "B",
                "E",
                types["b_6"],
                types["e_4"],
            )

            # Par de Frases 38
            types["a_9"], types["g_8"] = statement(
                "Basicamente, tenho sido tranquilo e conciliador.",
                "Basicamente, tenho sido determinado e assertivo.",
                "A",
                "G",
                types["a_9"],
                types["g_8"],
            )

            # Par de Frases 39
            types["c_3"], types["d_1"] = statement(
                "Eu trabalhei duro para ser aceito e querido.",
                "Ser aceito e querido não tem sido uma alta prioridade para mim.",
                "C",
                "D",
                types["c_3"],
                types["d_1"],
            )

            # Par de Frases 40
            types["h_5"], types["i_7"] = statement(
                "Em reação à pressão dos outros, eu me tornei mais reservado.",
                "Em reação à pressão dos outros, eu me tornei mais assertivo.",
                "H",
                "I",
                types["h_5"],
                types["i_7"],
            )

            # Par de Frases 41
            types["f_2"], types["e_4"] = statement(
                "As pessoas se interessaram em mim porque fui extrovertido, "
                "envolvente, e interessado nelas.",
                "As pessoas se interessaram em mim porque fui quieto, incomum "
                "e profundo.",
                "F",
                "E",
                types["f_2"],
                types["e_4"],
            )

            # Par de Frases 42
            types["b_6"], types["a_9"] = statement(
                "Dever e responsabilidade têm sido valores importantes para mim.",
                "Harmonia e aceitação têm sido valores importantes para mim.",
                "B",
                "A",
                types["b_6"],
                types["a_9"],
            )

            # Par de Frases 43
            types["g_8"], types["d_1"] = statement(
                "Eu tentei motivar as pessoas fazendo grandes planos e promessas.",
                "Eu tentei motivar as pessoas apontando as consequências de não "
                "seguir meus conselhos.",
                "G",
                "D",
                types["g_8"],
                types["d_1"],
            )

            # Par de Frases 44
            types["h_5"], types["f_2"] = statement(
                "Eu raramente fui emocionalmente demonstrativo.",
                "Eu frequentemente fui emocionalmente demonstrativo.",
                "H",
                "F",
                types["h_5"],
                types["f_2"],
            )

            # Par de Frases 45
            types["i_7"], types["c_3"] = statement(
                "Lidar com detalhes não tem sido um dos meus pontos fortes.",
                "Eu me destaquei em lidar com detalhes.",
                "I",
                "C",
                types["i_7"],
                types["c_3"],
            )

            # Par de Frases 46
            types["e_4"], types["a_9"] = statement(
                "Eu tenho enfatizado frequentemente o quão diferente eu sou "
                "das outras pessoas, especialmente da minha família.",
                "Eu tenho enfatizado frequentemente o quanto eu tenho em comum "
                "com a maioria das pessoas, especialmente a minha família.",
                "E",
                "A",
                types["e_4"],
                types["a_9"],
            )

            # Par de Frases 47
            types["h_5"], types["g_8"] = statement(
                "Quando as coisas esquentaram, eu tendi a ficar nos bastidores.",
                "Quando as coisas esquentaram, eu tendi a ficar bem no meio " "delas.",
                "H",
                "G",
                types["h_5"],
                types["g_8"],
            )

            # Par de Frases 48
            types["b_6"], types["d_1"] = statement(
                "Eu tenho ficado do lado dos meus amigos, até quando eles "
                "estiveram errados.",
                "Eu não quis comprometer o que é certo, nem mesmo por amizade.",
                "B",
                "D",
                types["b_6"],
                types["d_1"],
            )

            # Par de Frases 49
            types["f_2"], types["c_3"] = statement(
                "Eu tenho sido um apoiador bem-intencionado.",
                "Eu tenho sido um batalhador altamente motivado.",
                "F",
                "C",
                types["f_2"],
                types["c_3"],
            )

            # Par de Frases 50
            types["e_4"], types["i_7"] = statement(
                "Quando conturbado, eu tendi a remoer meus problemas.",
                "Quando conturbado, eu tendi a encontrar distrações para mim.",
                "E",
                "I",
                types["e_4"],
                types["i_7"],
            )

            # Par de Frases 51
            types["d_1"], types["h_5"] = statement(
                "Geralmente, eu tive convicções fortes e uma noção de como as coisas "
                "deveriam ser.",
                "Geralmente, eu tive sérias dúvidas e questionei como as coisas "
                "pareciam ser.",
                "D",
                "H",
                types["d_1"],
                types["h_5"],
            )

            # Par de Frases 52
            types["b_6"], types["g_8"] = statement(
                "Eu criei problemas com os outros sendo pessimista e reclamão.",
                "Eu criei problemas com os outros sendo mandão e controlador.",
                "B",
                "G",
                types["b_6"],
                types["g_8"],
            )

            # Par de Frases 53
            types["f_2"], types["a_9"] = statement(
                'Eu tendi a agir sob minhas emoções e "deixar as coisas '
                'acontecerem".',
                "Eu tendi a não agir sob minhas emoções para evitar causar "
                "mais problemas.",
                "F",
                "A",
                types["f_2"],
                types["a_9"],
            )

            # Par de Frases 54
            types["c_3"], types["e_4"] = statement(
                "Ser o centro das atenções geralmente me pareceu natural.",
                "Ser o centro das atenções geralmente me pareceu estranho.",
                "C",
                "E",
                types["c_3"],
                types["e_4"],
            )

            # Par de Frases 55
            types["b_6"], types["i_7"] = statement(
                "Eu tenho sido cuidadoso e tenho tentado me preparar para "
                "problemas imprevistos.",
                "Eu tenho sido espontâneo e preferido improvisar conforme os "
                "problemas surgem.",
                "B",
                "I",
                types["b_6"],
                types["i_7"],
            )

            # Par de Frases 56
            types["f_2"], types["d_1"] = statement(
                "Eu fiquei com raiva quando os outros não mostraram apreciação "
                "suficiente pelo o que fiz por eles.",
                "Eu fiquei com raiva quando os outros não ouviram o que eu disse "
                "a eles.",
                "F",
                "D",
                types["f_2"],
                types["d_1"],
            )

            # Par de Frases 57
            types["g_8"], types["c_3"] = statement(
                "Ser independente e auto-suficiente tem sido importante para mim.",
                "Ser valorizado e admirado tem sido importante para mim.",
                "G",
                "C",
                types["g_8"],
                types["c_3"],
            )

            # Par de Frases 58
            types["h_5"], types["a_9"] = statement(
                "Quando debati com amigos, tendi a pressionar meus argumentos "
                "fortemente.",
                "Quando debati com amigos, tendi a deixar as coisas passarem para "
                "evitar ressentimentos.",
                "H",
                "A",
                types["h_5"],
                types["a_9"],
            )

            # Par de Frases 59
            types["f_2"], types["b_6"] = statement(
                "Eu muitas vezes fui possessivo em relação àqueles que amo – tive "
                "dificuldade em deixá-los em paz.",
                'Eu muitas vezes "testei" aqueles que amo para ver se eles realmente '
                "estavam lá para mim.",
                "F",
                "B",
                types["f_2"],
                types["b_6"],
            )

            # Par de Frases 60
            types["g_8"], types["i_7"] = statement(
                "Organizar recursos e fazer as coisas acontecerem tem sido uma "
                "das minhas maiores qualidades.",
                "Ter novas ideias e animar as pessoas com elas tem sido uma das "
                "minhas maiores qualidades.",
                "G",
                "I",
                types["g_8"],
                types["i_7"],
            )

            # Par de Frases 61
            types["d_1"], types["e_4"] = statement(
                "Eu tendi a ser motivado e bem exigente comigo mesmo.",
                "Eu tendi a ser muito emotivo e um tanto indisciplinado.",
                "D",
                "E",
                types["d_1"],
                types["e_4"],
            )

            # Par de Frases 62
            types["i_7"], types["a_9"] = statement(
                "Eu tentei manter minha vida acelerada, intensa e animada.",
                "Eu tentei manter minha vida normal, estável e tranquila.",
                "I",
                "A",
                types["i_7"],
                types["a_9"],
            )

            # Par de Frases 63
            types["b_6"], types["c_3"] = statement(
                "Mesmo tendo tido sucesso, tendi a duvidar das minhas habilidades.",
                "Mesmo tendo tido contratempos, sempre tive muita confiança nas minhas "
                "habilidades.",
                "B",
                "C",
                types["b_6"],
                types["c_3"],
            )

            # Par de Frases 64
            types["e_4"], types["h_5"] = statement(
                "Eu geralmente tenho tendido a me apegar aos meus sentimentos "
                "e me agarrar neles por muito tempo.",
                "Eu geralmente tenho tendido a minimizar meus sentimentos e não "
                "prestar muita atenção neles.",
                "E",
                "H",
                types["e_4"],
                types["h_5"],
            )

            # Par de Frases 65
            types["f_2"], types["g_8"] = statement(
                "Eu tenho proporcionado muitas pessoas com atenção e apoio emocional.",
                "Eu tenho proporcionado muitas pessoas com direção e motivação.",
                "F",
                "G",
                types["f_2"],
                types["g_8"],
            )

            # Par de Frases 66
            types["d_1"], types["i_7"] = statement(
                "Eu tenho sido um pouco sério e rigoroso comigo mesmo.",
                "Eu tenho sido um pouco descompromissado e permissivo comigo mesmo.",
                "D",
                "I",
                types["d_1"],
                types["i_7"],
            )

            # Par de Frases 67
            types["c_3"], types["a_9"] = statement(
                "Eu tenho sido auto-assertivo e motivado a ser o melhor.",
                "Eu tenho sido modesto e estado feliz em ir no meu próprio ritmo.",
                "C",
                "A",
                types["c_3"],
                types["a_9"],
            )

            # Par de Frases 68
            types["h_5"], types["b_6"] = statement(
                "Eu tenho me orgulhado da minha clareza e objetividade.",
                "Eu tenho me orgulhado da minha confiabilidade e comprometimento.",
                "H",
                "B",
                types["h_5"],
                types["b_6"],
            )

            # Par de Frases 69
            types["e_4"], types["g_8"] = statement(
                "Eu tenho dedicado muito tempo olhando para dentro de mim – "
                "entender minhas emoções tem sido importante para mim.",
                "Eu não não tenho dedicado muito tempo olhando para dentro de mim "
                "– fazer as coisas tem sido importante para mim.",
                "E",
                "G",
                types["e_4"],
                types["g_8"],
            )

            # Par de Frases 70
            types["a_9"], types["d_1"] = statement(
                "Geralmente, eu me vi como uma pessoa alegre e descontraída.",
                "Geralmente, eu me vi como uma pessoa séria e digna.",
                "A",
                "D",
                types["a_9"],
                types["d_1"],
            )

            # Par de Frases 71
            types["i_7"], types["f_2"] = statement(
                "Eu tive uma mente ágil e energia ilimitada.",
                "Eu tive um coração acolhedor e uma profunda dedicação.",
                "I",
                "F",
                types["i_7"],
                types["f_2"],
            )

            # Par de Frases 72
            types["c_3"], types["h_5"] = statement(
                "Eu tenho buscado atividades que tinham um potencial substancial de "
                "recompensa e reconhecimento pessoal.",
                "Eu tenho estado disposto a abrir mão de recompensas e reconhecimento "
                "pessoal "
                "se isso significasse fazer algo que realmente me interessasse.",
                "C",
                "H",
                types["c_3"],
                types["h_5"],
            )

            # Par de Frases 73
            types["e_4"], types["b_6"] = statement(
                "Cumprir obrigações sociais raramente foi uma prioridade minha.",
                "Eu geralmente levo minhas obrigações sociais muito a sério.",
                "E",
                "B",
                types["e_4"],
                types["b_6"],
            )

            # Par de Frases 74
            types["g_8"], types["a_9"] = statement(
                "Na maioria das situações, eu preferi assumir o comando.",
                "Na maioria das situações, eu preferi deixar outra pessoa assumir "
                "o comando.",
                "G",
                "A",
                types["g_8"],
                types["a_9"],
            )

            # Par de Frases 75
            types["c_3"], types["d_1"] = statement(
                "Ao longo dos anos, meus valores e estilo de vida mudaram várias "
                "vezes.",
                "Ao longo dos anos, meus valores e estilo de vida permaneceram "
                "um tanto consistentes.",
                "C",
                "D",
                types["c_3"],
                types["d_1"],
            )

            # Par de Frases 76
            types["i_7"], types["h_5"] = statement(
                "Tipicamente, eu não tenho tido muita disciplina.",
                "Tipicamente, eu não tenho tido muita conexão com as pessoas.",
                "I",
                "H",
                types["i_7"],
                types["h_5"],
            )

            # Par de Frases 77
            types["e_4"], types["f_2"] = statement(
                "Eu tendi a reter meu afeto e querer que os outros entrem no meu "
                "mundo.",
                "Eu tendi a dar meu afeto com facilidade e querer me expandir para os "
                "outros.",
                "E",
                "F",
                types["e_4"],
                types["f_2"],
            )

            # Par de Frases 78
            types["b_6"], types["a_9"] = statement(
                "Eu tenho tendência a pensar no pior.",
                "Eu tendência de pensar que tudo vai dar certo.",
                "B",
                "A",
                types["b_6"],
                types["a_9"],
            )

            # Par de Frases 79
            types["g_8"], types["d_1"] = statement(
                "As pessoas têm confiado em mim porque eu sou confiante e "
                "posso cuidar delas.",
                "As pessoas têm confiado em mim porque sou justo e farei o que é "
                "certo.",
                "G",
                "D",
                types["g_8"],
                types["d_1"],
            )

            # Par de Frases 80
            types["h_5"], types["f_2"] = statement(
                "Frequentemente, eu tenho estado tão envolvido nos meus "
                "projetos que eu me isolei dos outros.",
                "Frequentemente, eu tenho estado tão envolvido com os outros que "
                "eu negligenciei meus projetos.",
                "H",
                "F",
                types["h_5"],
                types["f_2"],
            )

            # Par de Frases 81
            types["c_3"], types["i_7"] = statement(
                "Ao conhecer alguém novo, geralmente sou calmo e contido.",
                "Ao conhecer alguém novo, geralmente sou falante e divertido.",
                "C",
                "I",
                types["c_3"],
                types["i_7"],
            )

            # Par de Frases 82
            types["e_4"], types["a_9"] = statement(
                "Geralmente, eu tenho tendido a ser pessimista.",
                "Geralmente, eu tenho tendido a ser otimista.",
                "E",
                "A",
                types["e_4"],
                types["a_9"],
            )

            # Par de Frases 83
            types["h_5"], types["g_8"] = statement(
                "Eu prefiro habitar meu próprio mundo.",
                "Eu prefiro fazer o mundo saber que eu estou aqui.",
                "H",
                "G",
                types["h_5"],
                types["g_8"],
            )

            # Par de Frases 84
            types["b_6"], types["d_1"] = statement(
                "Eu frequentemente fui perturbado por ansiedade, insegurança e "
                "dúvida.",
                "Eu frequentemente fui perturbado por raiva, perfeccionismo e "
                "impaciência.",
                "B",
                "D",
                types["b_6"],
                types["d_1"],
            )

            # Par de Frases 85
            types["f_2"], types["c_3"] = statement(
                "Percebo que muitas vezes fui pessoal e íntimo de mais.",
                "Percebo que muitas vezes fui frio e distante demais.",
                "F",
                "C",
                types["f_2"],
                types["c_3"],
            )

            # Par de Frases 86
            types["e_4"], types["i_7"] = statement(
                "Eu perdi oportunidades porque não me senti capaz de aproveitá-las.",
                "Eu perdi oportunidades porque perseguia muitas possibilidades.",
                "E",
                "I",
                types["e_4"],
                types["i_7"],
            )

            # Par de Frases 87
            types["h_5"], types["d_1"] = statement(
                "Eu tenho tendido a levar muito tempo para agir.",
                "Eu tenho tendido a agir rapidamente.",
                "H",
                "D",
                types["h_5"],
                types["d_1"],
            )

            # Par de Frases 88
            types["b_6"], types["g_8"] = statement(
                "Eu geralmente tenho dificuldade em tomar decisões.",
                "Eu raramente tenho dificuldade em tomar decisões.",
                "B",
                "G",
                types["b_6"],
                types["g_8"],
            )

            # Par de Frases 89
            types["f_2"], types["a_9"] = statement(
                "Eu tenho tido uma tendência a ser um pouco intenso com as pessoas.",
                "Eu tenho tido uma tendência de não me impor o suficiente com as "
                "pessoas.",
                "F",
                "A",
                types["f_2"],
                types["a_9"],
            )

            # Par de Frases 90
            types["c_3"], types["e_4"] = statement(
                "Tipicamente, eu tenho sido equilibrado.",
                "Tipicamente, eu tenho tido fortes mudanças de humor.",
                "C",
                "E",
                types["c_3"],
                types["e_4"],
            )

            # Par de Frases 91
            types["b_6"], types["i_7"] = statement(
                "Quando estive incerto do que fazer, muitas vezes busquei "
                "conselhos dos outros.",
                "Quando estive incerto do que fazer, tentei diferentes coisas "
                "para ver o que funcionava melhor para mim.",
                "B",
                "I",
                types["b_6"],
                types["i_7"],
            )

            # Par de Frases 92
            types["f_2"], types["d_1"] = statement(
                "Eu tenho me preocupado em ser deixado de fora das atividades dos "
                "outros.",
                "Eu tenho me preocupado que as atividades dos outros possam me "
                "distrair do que eu tenho que fazer.",
                "F",
                "D",
                types["f_2"],
                types["d_1"],
            )

            # Par de Frases 93
            types["g_8"], types["c_3"] = statement(
                "Tipicamente, quando fico com raiva, eu repreendo as pessoas.",
                "Tipicamente, quando fico com raiva, me torno distante.",
                "G",
                "C",
                types["g_8"],
                types["c_3"],
            )

            # Par de Frases 94
            types["h_5"], types["a_9"] = statement(
                "Eu tenho tendido a ter problemas para dormir.",
                "Eu tenho tendido a adormecer facilmente.",
                "H",
                "A",
                types["h_5"],
                types["a_9"],
            )

            # Par de Frases 95
            types["f_2"], types["b_6"] = statement(
                "Eu frequentemente tentei descobrir como eu poderia me aproximar mais "
                "dos outros.",
                "Eu frequentemente tentei descobrir o que os outros queriam de mim.",
                "F",
                "B",
                types["f_2"],
                types["b_6"],
            )

            # Par de Frases 96
            types["g_8"], types["i_7"] = statement(
                "Eu geralmente fui ponderado, franco e deliberado.",
                "Eu geralmente fui animado, espirituoso e falei rápido.",
                "G",
                "I",
                types["g_8"],
                types["i_7"],
            )

            # Par de Frases 97
            types["e_4"], types["d_1"] = statement(
                "Muitas vezes, eu não me manifestei quando vi os outros "
                "cometendo um erro.",
                "Muitas vezes, eu ajudei os outros a perceberem que estavam "
                "cometendo um erro.",
                "E",
                "D",
                types["e_4"],
                types["d_1"],
            )

            # Par de Frases 98
            types["i_7"], types["a_9"] = statement(
                "Durante a maior parte da minha vida, tenho sido uma pessoa turbulenta "
                "que teve muitas emoções voláteis.",
                "Durante a maior parte da minha vida, tenho sido uma pessoa estável e "
                "tranquila por fora, porém profunda por dentro.",
                "I",
                "A",
                types["i_7"],
                types["a_9"],
            )

            # Par de Frases 99
            types["c_3"], types["b_6"] = statement(
                "Quando não gostei de alguém, geralmente tentei me manter "
                "cordial – apesar das minhas emoções.",
                "Quando não gostei de alugém, geralmente os deixei saber disso "
                "– de uma forma ou de outra.",
                "C",
                "B",
                types["c_3"],
                types["b_6"],
            )

            # Par de Frases 100
            types["e_4"], types["h_5"] = statement(
                "Grande parte das minhas dificuldades com as pessoas vem da minha "
                "sensibilidade e levar tudo para o lado pessoal.",
                "Grande parte das minhas dificuldades com as pessoas vem do meu "
                "desapego com as convenções sociais.",
                "E",
                "H",
                types["e_4"],
                types["h_5"],
            )

            # Par de Frases 101
            types["f_2"], types["g_8"] = statement(
                "Minha abordagem tem sido me meter e resgatar as pessoas.",
                "Minha abordagem tem sido mostrar às pessoas como se ajudarem.",
                "F",
                "G",
                types["f_2"],
                types["g_8"],
            )

            # Par de Frases 102
            types["i_7"], types["d_1"] = statement(
                'Geralmente, eu tenho gostado de "me deixar levar" e levar as coisas '
                "a seus limites.",
                "Geralmente, eu não tenho gostado muito de perder o controle de mim "
                "mesmo.",
                "I",
                "D",
                types["i_7"],
                types["d_1"],
            )

            # Par de Frases 103
            types["c_3"], types["a_9"] = statement(
                "Eu tenho me preocupado de mais em fazer as coisas melhor do que "
                "os outros.",
                "Eu estive preocupado de mais em fazer das coisas agradáveis aos "
                "outros.",
                "C",
                "A",
                types["c_3"],
                types["a_9"],
            )

            # Par de Frases 104
            types["h_5"], types["b_6"] = statement(
                "Meus pensamentos geralmente têm sido especulativos, envolvendo "
                "minha imaginação e curiosidade.",
                "Meus pensamentos geralmente têm sido práticos – apenas tentando "
                "manter as coisas andando.",
                "H",
                "B",
                types["h_5"],
                types["b_6"],
            )

            # Par de Frases 105
            types["g_8"], types["e_4"] = statement(
                "Um dos meus principais recursos tem sido a minha habilidade em "
                "assumir o controle das situações.",
                "Um dos meus principais recursos tem sido a minha habilidade em "
                "descrever estados internos.",
                "G",
                "E",
                types["g_8"],
                types["e_4"],
            )

            # Par de Frases 106
            types["d_1"], types["a_9"] = statement(
                "Eu pressionei as pessoas para que as coisas fossem feitas "
                "corretamente, até se isso as deixassem desconfortáveis.",
                "Eu não gosto de me sentir pressionado, então eu não gosto de "
                "pressionar os outros.",
                "D",
                "A",
                types["d_1"],
                types["a_9"],
            )

            # Par de Frases 107
            types["f_2"], types["i_7"] = statement(
                "Eu frequentemente me orgulhei da minha importância na vida "
                "dos outros.",
                "Eu frequentemente me orgulhei do meu gosto e abertura a novas "
                "experiências.",
                "F",
                "I",
                types["f_2"],
                types["i_7"],
            )

            # Par de Frases 108
            types["c_3"], types["h_5"] = statement(
                "Eu percebi que muitas vezes passei a impressão aos outros de ser "
                "apresentável, até admirável.",
                "Eu percebi que muitas vezes passei a impressão aos outros de ser "
                "incomum, até estranho.",
                "C",
                "H",
                types["c_3"],
                types["h_5"],
            )

            # Par de Frases 109
            types["b_6"], types["e_4"] = statement(
                "Eu tenho feito o que eu tinha que fazer.",
                "Eu tenho feito o que eu quis fazer.",
                "B",
                "E",
                types["b_6"],
                types["e_4"],
            )

            # Par de Frases 110
            types["g_8"], types["a_9"] = statement(
                "Eu geralmente gostei de situações de alta pressão, mesmo as difíceis.",
                "Eu geralmente não gostei de estar em situações de alta pressão ou "
                "difíceis.",
                "G",
                "A",
                types["g_8"],
                types["a_9"],
            )

            # Par de Frases 111
            types["c_3"], types["d_1"] = statement(
                "Eu tenho orgulho da minha habilidade de ser flexível – "
                "o que é apropriado ou importante frequentemente muda.",
                "Eu tenho orgulho da minha habilidade de me posicionar sobre "
                "algo – eu tenho sido firme no que acredito.",
                "C",
                "D",
                types["c_3"],
                types["d_1"],
            )

            # Par de Frases 112
            types["h_5"], types["i_7"] = statement(
                "Meu estilo pende à simplicidade e austeridade.",
                "Meu estilo pende ao excesso e ao exagero.",
                "H",
                "I",
                types["h_5"],
                types["i_7"],
            )

            # Par de Frases 113
            types["f_2"], types["e_4"] = statement(
                "Minha própria saúde e bem-estar sofreram por causa do meu "
                "forte desejo de ajudar os outros.",
                "Meus relacionamentos sofreram por causa do meu forte desejo de "
                "atender às minhas necessidades pessoais.",
                "F",
                "E",
                types["f_2"],
                types["e_4"],
            )

            # Par de Frases 114
            types["a_9"], types["b_6"] = statement(
                "De maneira geral, eu tenho sido muito aberto e ingênuo.",
                "De maneira geral, eu tenho sido muito cauteloso e guardado.",
                "A",
                "B",
                types["a_9"],
                types["b_6"],
            )

            # Par de Frases 115
            types["g_8"], types["d_1"] = statement(
                "Eu às vezes afasto as pessoas por ser muito agressivo.",
                'Eu às vezes afasto as pessoas por ser muito "certinho".',
                "G",
                "D",
                types["g_8"],
                types["d_1"],
            )

            # Par de Frases 116
            types["f_2"], types["h_5"] = statement(
                "Servir e atender às necessidades dos outros tem sido "
                "uma prioridade minha.",
                "Encontrar formas alternativas de ver e fazer as coisas tem sido uma "
                "prioridade minha.",
                "F",
                "H",
                types["f_2"],
                types["h_5"],
            )

            # Par de Frases 117
            types["c_3"], types["i_7"] = statement(
                "Eu tenho sido determinado e persistente na busca pelos meus "
                "objetivos.",
                "Eu prefiro explorar várias opções para ver onde elas levam.",
                "C",
                "I",
                types["c_3"],
                types["i_7"],
            )

            # Par de Frases 118
            types["e_4"], types["a_9"] = statement(
                "Com frequência, tenho sido atraído por situações que despertam "
                "emoções profundas e intensas.",
                "Com frequência, tenho sido atraído por situações que me fazem sentir "
                "calmo e à vontade.",
                "E",
                "A",
                types["e_4"],
                types["a_9"],
            )

            # Par de Frases 119
            types["h_5"], types["g_8"] = statement(
                "Eu tenho me importado menos com resultados práticos do que em "
                "perseguir "
                "meus interesses.",
                "Eu tenho sido prático e esperado que meu trabalho tenha resultados "
                "concretos.",
                "H",
                "G",
                types["h_5"],
                types["g_8"],
            )

            # Par de Frases 120
            types["b_6"], types["d_1"] = statement(
                "Eu tenho tido uma necessidade profunda de pertencer.",
                "Eu tenho tido uma necessidade profunda de me sentir equilibrado.",
                "B",
                "D",
                types["b_6"],
                types["d_1"],
            )

            # Par de Frases 121
            types["f_2"], types["c_3"] = statement(
                "No passado, eu provavelmente insisti em ter muita proximidade "
                "nas minhas amizades.",
                "No passado, eu provavelmente mantive muita distância nos meus "
                "relacionamentos.",
                "F",
                "C",
                types["f_2"],
                types["c_3"],
            )

            # Par de Frases 122
            types["e_4"], types["i_7"] = statement(
                "Eu tenho tido uma tendência a ficar pensando em " "coisas do passado.",
                "Eu tenho tido uma tendência a ficar antecipando as coisas que "
                "vou fazer.",
                "E",
                "I",
                types["e_4"],
                types["i_7"],
            )

            # Par de Frases 123
            types["h_5"], types["d_1"] = statement(
                "Eu tendi a ver as pessoas como invasivas e exigentes.",
                "Eu tendi a ver as pessoas como desorganizadas e irresponsáveis.",
                "H",
                "D",
                types["h_5"],
                types["d_1"],
            )

            # Par de Frases 124
            types["b_6"], types["g_8"] = statement(
                "Em geral, eu não tive muita confiança em mim mesmo.",
                "Em geral, eu tive confiança apenas em mim mesmo.",
                "B",
                "G",
                types["b_6"],
                types["g_8"],
            )

            # Par de Frases 125
            types["a_9"], types["f_2"] = statement(
                "Eu provavelmente fui muito passivo e pouco envolvido.",
                "Eu provavelmente fui muito controlador e manipulador.",
                "A",
                "F",
                types["a_9"],
                types["f_2"],
            )

            # Par de Frases 126
            types["e_4"], types["c_3"] = statement(
                "Com frequência, minha insegurança me impediu de avançar.",
                "Eu raramente deixei a insegurança ficar no meu caminho.",
                "E",
                "C",
                types["e_4"],
                types["c_3"],
            )

            # Par de Frases 127
            types["i_7"], types["b_6"] = statement(
                "Podendo escolher entre algo familiar e algo novo, eu geralmente "
                "escolhi algo novo.",
                "Eu geralmente escolhi o que eu sabia que gostava: por que me "
                "desapontar com algo que eu posso não gostar?",
                "I",
                "B",
                types["i_7"],
                types["b_6"],
            )

            # Par de Frases 128
            types["f_2"], types["d_1"] = statement(
                "Eu tenho dado muito contato físico para assegurar os outros de como "
                "eu me sinto em relação a eles.",
                "Eu geralmente senti que o amor verdadeiro não depende de contato "
                "físico.",
                "F",
                "D",
                types["f_2"],
                types["d_1"],
            )

            # Par de Frases 129
            types["g_8"], types["c_3"] = statement(
                "Quando precisei confrontar alguém, muitas vezes fui "
                "muito duro e direto.",
                "Quando precisei confrontar alguém, eu frequentemente enrolei "
                "de mais.",
                "G",
                "C",
                types["g_8"],
                types["c_3"],
            )

            # Par de Frases 130
            types["h_5"], types["a_9"] = statement(
                "Eu tenho me atraído por assuntos que os outros provavelmente "
                "achariam perturbadores, até assustadores.",
                "Eu tenho preferido não passar meu tempo refletindo sobre assuntos "
                "perturbadores e assustadores.",
                "H",
                "A",
                types["h_5"],
                types["a_9"],
            )

            # Par de Frases 131
            types["f_2"], types["b_6"] = statement(
                "Eu já me meti em problemas com as pessoas por ser muito intrusivo e "
                "interferente.",
                "Eu já me meti em problemas com as pessoas por ser muito evasivo e "
                "taciturno.",
                "F",
                "B",
                types["f_2"],
                types["b_6"],
            )

            # Par de Frases 132
            types["g_8"], types["i_7"] = statement(
                "Eu me preocupo que eu não tenha os recursos para cumprir as "
                "responsabilidades que assumi.",
                "Eu me preocupo que eu não tenha a disciplina para focar no que "
                "realmente me satisfaz.",
                "G",
                "I",
                types["g_8"],
                types["i_7"],
            )

            # Par de Frases 133
            types["e_4"], types["d_1"] = statement(
                "Em geral, eu tenho sido uma pessoa altamente intuitiva e "
                "individualista.",
                "Em geral, eu tenho sido uma pessoa altamente organizada e "
                "responsável.",
                "E",
                "D",
                types["e_4"],
                types["d_1"],
            )

            # Par de Frases 134
            types["a_9"], types["i_7"] = statement(
                "Superar a inércia tem sido um dos meus principais problemas.",
                "Não conseguir desacelerar tem sido um dos meus principais problemas.",
                "A",
                "I",
                types["a_9"],
                types["i_7"],
            )

            # Par de Frases 135
            types["c_3"], types["b_6"] = statement(
                "Quando eu me senti inseguro, eu reagi me tornando arrogante e "
                "desdenhoso.",
                "Quando eu me senti inseguro, eu reagi me tornando defensivo e "
                "argumentativo.",
                "C",
                "B",
                types["c_3"],
                types["b_6"],
            )

            # Par de Frases 136
            types["h_5"], types["e_4"] = statement(
                "Eu geralmente tenho sido mente aberta e disposto a tentar novas "
                "abordagens.",
                "Eu geralmente tenho sido auto-revelador e disposto a "
                "compartilhar meus sentimentos com os outros.",
                "H",
                "E",
                types["h_5"],
                types["e_4"],
            )

            # Par de Frases 137
            types["g_8"], types["f_2"] = statement(
                "Eu me apresento aos outros como sendo mais durão do que "
                "realmente sou.",
                "Eu me apresento aos outros como me importando mais do que "
                "realmente me importo.",
                "G",
                "F",
                types["g_8"],
                types["f_2"],
            )

            # Par de Frases 138
            types["d_1"], types["i_7"] = statement(
                "Eu geralmente segui minha consciência e razão.",
                "Eu geralmente segui meus sentimentos e impulsos.",
                "D",
                "I",
                types["d_1"],
                types["i_7"],
            )

            # Par de Frases 139
            types["c_3"], types["a_9"] = statement(
                "Grandes adversidades me fizeram sentir firme e resoluto.",
                "Grandes adversidades me fizeram sentir desencorajado e resignado.",
                "C",
                "A",
                types["c_3"],
                types["a_9"],
            )

            # Par de Frases 140
            types["b_6"], types["h_5"] = statement(
                "Eu geralmente me certifiquei de ter algum plano B.",
                "Eu geralmente escolhi viver no limite e depender dos outros o mínimo "
                "possível.",
                "B",
                "H",
                types["b_6"],
                types["h_5"],
            )

            # Par de Frases 141
            types["g_8"], types["e_4"] = statement(
                "Eu tive que ser forte pelos outros, então eu não tive "
                "tempo para lidar com minhas emoções e medos.",
                "Eu tenho tido dificuldade em lidar com minhas emoções e medos, "
                "então ser forte pelos outros tem sido difícil para mim.",
                "G",
                "E",
                types["g_8"],
                types["e_4"],
            )

            # Par de Frases 142
            types["a_9"], types["d_1"] = statement(
                "Eu frequentemente me pergunto por que as pessoas "
                "se concentram no negativo "
                "quando há tantas coisas maravilhosas na vida.",
                "Eu frequentemente me pergunto por que as pessoas são tão "
                "felizes quando há tanta coisa falha na vida.",
                "A",
                "D",
                types["a_9"],
                types["d_1"],
            )

            # Par de Frases 143
            types["f_2"], types["i_7"] = statement(
                "Eu tenho tentado bastante não parecer uma pessoa egoísta.",
                "Eu tenho tentado bastante não parecer uma pessoa chata.",
                "F",
                "I",
                types["f_2"],
                types["i_7"],
            )

            # Par de Frases 144
            types["h_5"], types["c_3"] = statement(
                "Eu evitei intimidade quando eu temi que seria sobrecarregado "
                "pelas necessidades e exigências das pessoas.",
                "Eu evitei intimidade quando eu temi que não seria capaz de atender "
                "às expectativas das pessoas sobre mim.",
                "H",
                "C",
                types["h_5"],
                types["c_3"],
            )
