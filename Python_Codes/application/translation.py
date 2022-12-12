# Temp imports, we should move it later to __init__.py
import language_tool_python
import re


# Class object sentence as provided in the design
class Sentence:
    def __init__(self):
        self.sentence = str()
        self.keywords = dict()
        self.validated = bool()
        self.tool = language_tool_python.LanguageTool('en-US', config={'cacheSize': 1000, 'pipelineCaching': True})
        # In case the local server didn't work
        # self.tool = language_tool_python.LanguageToolPublicAPI('es',
        #                                                        config={'cacheSize': 1000, 'pipelineCaching': True})

    @property
    def sentence(self) -> str:
        return self.sentence

    @sentence.setter
    def sentence(self, sentence) -> int:
        self.sentence = sentence
        return 0

    @property
    def validated(self) -> bool:
        return self.validated

    @validated.setter
    def validated(self, validated) -> int:
        self.validated = validated
        return 0

    def suggest(self, sentence) -> int | str:
        try:
            suggestion = self.tool.correct(sentence)
        except BaseException as e:
            print(e, "suggest function error")
            return -1
        return suggestion

    def validate(self, sentence):
        try:
            if not self.tool.check(sentence):
                self.validated = 1
                return 0
            else:
                self.validated = 0
                return 0
        except BaseException as e:
            print(e, "validate function")
            self.validated = 0
            return -1


# Class object translator as provided in the design
class Translator:
    # Solve case issues, and make sure all verbs are capitalized
    def __init__(self, sentence):
        # Initiating relationships (aggregation)
        self.obj_sentence = sentence
        self.makeSense = bool()
        self.finalSentence = str()
        self.dictionary = {
            "CHOOSE": ["choose", "select", "pick", "pick out", "opt for", "plump for", "go for", "take", "settle on",
                       "decide on", "fix on", "vote for", "single out", "handpick", "set", "designate", "determine",
                       "specify", "appoint "],
            "and": ["and", "along with", "also", "as a consequence", "as well as", "furthermore", "including",
                    "moreover", "together with"],
            "from": ["from", "against", "in distinction to", "out of possession of", "taken away", "of"],
            "if": ["if", "on condition that", "provided that", "providing that", "presuming that", "supposing that",
                   "assuming that", "on the assumption that", "allowing that"],
            "or": ["or", "as a choice", "as a substitute", "as an alternative", "conversely", "either",
                   "in other words", "in preference to", "in turn", "on the other hand", "or but", "or else",
                   "or only", "preferentially"],
            "to": ["to", "into", "at", "for"],
            "WRITE": ["write", "address", "compose", "draft", "note", "print", "record", "rewrite", "scrawl",
                      "scribble", "sign", "tell", "autograph", "communicate", "inscribe", "transcribe", "typewrite",
                      "draw up", "draw", "drop a line", "drop a note", "jot down", "note down", "put in", "put",
                      "write down", "write up"],
            "COPY": ["copy", "image", "reproduce", "clone", "mirror", "reflect", "replicate", "reprint", "simulate",
                     "mimic", "imitate", "emulate", "mime"],
            "CUT": ["cut", "slit", "slice", "rip", "split", "chop", "crosscut", "scissor", "chip", "cut off", "snip",
                    "clip", "scissor", "cut off", "break", "cut out", "separate"],
            "REMOVE": ["remove", "strip", "put off", "get rid off", "take off", "kick", "kick off", "eliminate",
                       "rest", "clear", "eject", "bring out"]

        }
        self.catg_list = ["choose01", "choose02", "write01", "write02", "write03", "copy01", "copy02", "cut01", "cut02",
                          "remove01"]
        self.regexes_first = {
            "choose01": "(\w[a-z]*)\s(\w*)\s(\w*)\s(\w[a-z]*\(\w[A-Z]*\d*\))",
            "choose02": "(\w[A-z]*)\s(\w*)\s(\w[a-z]*\(\w[A-Z]*\d*\))",
            "write01": '(\w[A-Z]*)\s(".*")\s(\w[A-z])\s(\w[a-z]*\(\w[A-Z]*\d*\))',
            "write02": "(\w[A-Z]*)\s(\w*)\s(\w*)\s(\w[a-z]*\(\w[A-Z]*\d*\))",
            "write03": "(\w[A-Z]*)\s(\(.*\))\s(\w*)\s(\w[a-z]*\(\w[A-Z]*\d*\))",
            "copy01": "(\w[A-Z]*)\s(\w*\(\w*\d*\))\s(\w*)\s(\w[a-z]*\(\w[A-Z]*\d*\))",
            "copy02": "(\w[A-Z]*)\s(\w*)\s(\w*)\s(\w[a-z]*\(\w[A-Z]*\d*\))",
            "cut01": "(\w[A-Z]*)\s(\w*\(\w*\d*\))\s(\w*)\s(\w[a-z]*\(\w[A-Z]*\d*\))",
            "cut02": "(\w[A-Z]*)\s(\w*)\s(\w*)\s(\w[a-z]*\(\w[A-Z]*\d*\))",
            "remove01": "(\w*)\s(\w[a-z]*\(\w[A-Z]*\d*\))"
        }
        self.regexes_strict = {
            "choose01": "(choose)\s(\w*)\s(from)\s(cell\(\w[a-a]*\d*\))",
            "choose02": "(\w*)\s(from)\s(cell\(\w*\d*\))",
            "write01": '(WRITE)\s(".*")\s(to)\s(cell\(\w*\d*\))',
            "write02": "(WRITE)\s(\w*)\s(to)\s(cell\(\w*\d*\))",
            "write03": "(WRITE)\s(\(.*\))\s(to)\s(cell\(\w*\d*\))",
            "copy01": "(COPY)\s(cell\(\w*\d*\))\s(to)\s(cell\(\w*\d*\))",
            "copy02": "(COPY)\s(\w*)\s(to)\s(cell\(\w[A-Z]*\d*\))",
            "cut01": "(CUT)\s(cell\(\w*\d*\))\s(to)\s(cell\(\w*\d*\))",
            "cut02": "(CUT)\s(\w*)\s(to)\s(cell\(\w[A-Z]*\d*\))",
            "remove01": "(REMOVE)\s(cell\(\w[A-Z]*\d*\))"
        }

    @staticmethod  # Helper function to replace strings, will be used in translate method
    def replacer(main_string, new_string, index, no_fail=False):
        # raise an error if index is outside the string
        if not no_fail and max([abs(index[0]), abs(index[1])]) not in range(len(main_string) + 1):
            raise ValueError("index outside given string")

        # Making sure everything is ok, and it will work
        if abs(index[0] - index[1]) <= len(main_string) >= max([abs(index[0]), abs(index[1])]):  # add it to the end
            if index[0] == 0:
                return new_string + main_string[index[1]:]
            elif index[1] == len(main_string):
                return main_string[:index[0]] + new_string
            else:
                return main_string[:index[0]] + new_string + main_string[index[1]:]

    def translate(self,
                  input_sentence) -> int | str:  # This function return will be passed to the compiler (final_sentence)
        """
        This function works on taking the input sentence from the user and return the final standard
        sentence to compile

        -1 --> error
        -2 --> no matches

        - step01 taking the input sentence from the sentence class
        - step 02 check which regex does it follow, (Change makesense depending on)
            makesense = True / False
        - (undergoing) change the sentence to the standard one
        :return: self.finalSentence
        """

        # BLOCK01: this block of code should give us two variables, and those variables are:
        # 1- The match (The matched sentence)
        # 2- The matched category

        for catg, pattern in self.regexes_first.items():
            match = 0
            # compiling the pattern
            try:
                re.compile(pattern)

            except re.error as e:
                print("Non valid regex pattern, translate function", e)
                return -1
            # check which pattern the sentence matches
            try:
                match = re.search(pattern, input_sentence).group(0)
                if not match:
                    self.makeSense = False
                    continue
                else:
                    category = catg
                    break
            # in case of a None return from the function indicating a non match
            except AttributeError as e:
                # print(pattern)
                # print("Error in finding a match, translate function\n", e)
                continue

        if not match:
            self.makeSense = False
            return -2  # No matches and you should write a correct sentence

        # BLOCK02: This block is responsible on changing the current sentence to standard sentence
        # "match" is the variable we are manipulating here
        for regex_piece in self.regexes_first[catg].split("\s"):
            compile_ = re.compile(regex_piece)

            for each in compile_.finditer(match):
                for key, synonyms in self.dictionary.items():
                    if each.group(0).lower() in synonyms:
                        match = self.replacer(match, key, [each.span()[0], each.span()[1]])
                        break
        self.makeSense = True

        # BLOCK03: check strict regexes to make sure everything is ok
        if not re.search(self.regexes_strict[catg], match):
            self.makeSense = False
        else:
            self.makeSense = True

        # BLOCK04: Return the final sentence
        self.finalSentence = match
        return self.finalSentence

    @property
    def makeSense(self) -> bool():
        return self.makeSense

    @makeSense.setter
    def makeSense(self, makesense) -> int:
        self.makeSense = makesense
        return 0

    @property
    def finalSentence(self) -> str:
        return self.finalSentence

    @finalSentence.setter
    def finalSentence(self, final_sentence) -> int:
        self.finalSentence = final_sentence
        return 0


# Class object compiler as provided in the design
class Compiler:
    def __init__(self, translator):
        self.compiledSentence = list()
        # Initiating relationships (aggregation)
        self.obj_translator = translator

    @property
    def compiledSentence(self, sentence=list) -> 0:
        self.compiledSentence = sentence
        return 0

    @compiledSentence.setter
    def compiledSentence(self) -> list:
        return self.compiledSentence


if __name__ == "__main__":
    inst = Translator()
    a = inst.translate("CLONE cell(A02) into cell(A01)")
    print(a, inst.finalSentence, inst.makeSense)
