tachy_word = ["tachycardic"]

def is_tachycardic(candidate)
    clean_candidate = candidate.strip()
    for item in tachy_word:
        if item == clean_candidate:
            return true

    return false
