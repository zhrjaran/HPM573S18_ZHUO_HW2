# HUI3 regression coefficients
Constant1= 1.371
Constant2= 0.371

dictCoefficients= {"Vision": [1, 0.98, 0.89, 0.84, 0.75, 0.61],
                   "Hearing": [1, 0.95, 0.89, 0.8, 0.74, 0.61],
                   "Speech": [1, 0.94, 0.89, 0.81, 0.68],
                   "Ambulation": [1, 0.93, 0.86, 0.73, 0.65, 0.58],
                   "Dexterity": [1, 0.95, 0.88, 0.76, 0.65, 0.56],
                   "Emotion": [1, 0.95, 0.85, 0.64, 0.46],
                   "Cognition": [1, 0.92, 0.95, 0.83, 0.6, 0.42],
                   "Pain": [1, 0.96, 0.9, 0.77, 0.55]};

def getScore(vision, hearing, speech, ambulation, dexterity, emotion, cognition, pain):
    """

    :param vision: scale of vision [1,6]
    :param hearing: scale of hearing [1,6]
    :param speech: scale of speech [1,5]
    :param ambulation: scale of ambulation [1,6]
    :param dexterity: scale of dexterity [1,6]
    :param emotion: scale of emotion [1,5]
    :param cognition: scale of cognition [1,6]
    :param pain: scale of pain [1,5]
    :return: HUI3 health score
    """

     # ensure the entered health scales are acceptable
    if not (vision in range(1,7,1)):
        raise ValueError ("Vision level can take only 1 to 6")
    if not (hearing in range(1,7,1)):
        raise ValueError ("Hearing level can take only 1 to 6")
    if not (speech in range(1,6,1)):
        raise ValueError ("Speech level can take only 1 to 5")
    if not (ambulation in range(1,7,1)):
        raise ValueError ("Ambulation level can take only 1 to 6")
    if not (dexterity in range(1,7,1)):
        raise ValueError ("Dexterity level can take only 1 to 6")
    if not (emotion in range(1,6,1)):
        raise ValueError ("Emotion level can take only 1 to 5")
    if not (cognition in range(1,7,1)):
        raise ValueError ("Cognition level can take only 1 to 6")
    if not (pain in range(1,6,1)):
        raise ValueError ("Pain level can take only 1 to 5")

    score= 1

    score = Constant1 * dictCoefficients['Vision'][vision-1]* dictCoefficients['Hearing'][hearing-1]* dictCoefficients['Speech'][speech-1]* dictCoefficients['Ambulation'][ambulation-1]*dictCoefficients['Dexterity'][dexterity-1]*dictCoefficients['Emotion'][emotion-1]* dictCoefficients['Cognition'][cognition-1]*dictCoefficients['Pain'][pain-1] - Constant2

    return score

