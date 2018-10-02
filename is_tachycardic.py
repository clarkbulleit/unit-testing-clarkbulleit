
def is_tachycardic(candidate):

    clean_candidate = candidate.strip().lower()
    clean_candidate = ''.join(letter for letter
                              in clean_candidate if letter.isalpha())

    if clean_candidate == 'tachycardic':
            return True

    return False
