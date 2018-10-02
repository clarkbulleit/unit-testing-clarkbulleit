
def is_tachycardic(candidate)
    clean_candidate = candidate.strip().lower()
    for item in tachy_word:
        if item == clean_candidate:
            return true

    return false
