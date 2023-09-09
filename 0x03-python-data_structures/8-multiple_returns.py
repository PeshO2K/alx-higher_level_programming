#!/usr/bin/python3
def multiple_returns(sentence):
    ln = len(sentence)
    if ln > 0:
        f = sentence[0]
    else:
        f = None
    return (ln, f)
