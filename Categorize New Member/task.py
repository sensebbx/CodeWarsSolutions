def openOrSenior(data):
    return ['Senior' if person[0] > 54 and person[1] > 7 else 'Open' for person in data]
