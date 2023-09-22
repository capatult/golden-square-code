class GrammarStats():
    def __init__(self):
        self._text_correctness_log = []

    def check(self, text):
        result = text[0].isupper() and (text[-1] in ".!?")
        self._text_correctness_log.append(result)
        return result

    def percentage_good(self):
        if len(self._text_correctness_log) == 0:
            raise Exception("No texts checked so far.")
        else:
            return round(
                100 * sum([
                    1 if was_correct else 0
                    for was_correct in self._text_correctness_log
                ]) / len(self._text_correctness_log)
            )
