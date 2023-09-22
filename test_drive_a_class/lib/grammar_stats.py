class GrammarStats():
    def __init__(self):
        pass

    def check(self, text):
        return text[0].isupper() and (text[-1] in ".!?")
