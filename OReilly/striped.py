VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    text = text.upper()
    text += " "
    match_str = ""
    words = 0
    words_ok = 0
    for l in text:
        if l in VOWELS or l  in CONSONANTS:
            if l in VOWELS:
                match_str += 'v'
            if l in CONSONANTS:
                match_str += 'c'
        elif l.isdigit():
            match_str += 'n'
        else:
            words += 1
            if not 'vv' in match_str and not 'cc' in match_str and match_str and not 'n' in match_str and len(match_str) >1:
                words_ok += 1
            match_str = ""
    return words_ok

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio(u"1st 2a ab3er root rate ") == 1, "only rate"
    assert checkio(u"JJJ:qwerty,iddqd,hoho") == 1 , "only hoho"
