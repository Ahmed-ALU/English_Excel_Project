# Temp imports, we should move it later to __init__.py


# Class object sentence as provided in the design
class Sentence:
    def __init__(self):
        self.sentence = str()
        self.keywords = dict()

    def getSentence(self) -> str:
        return self.sentence

    def setSentence(self, sentence) -> int:
        self.sentence = sentence
        return 0

    def suggest(self) -> str:
        pass


# Class object translator as provided in the design
class Translator:
    def __init__(self):
        self.makeSense = bool()
        self.validated = bool()
        self.finalSentence = str()

    def getMakeSense(self) -> bool():
        return self.makeSense

    def getValidated(self) -> bool:
        return self.validated

    def __setMakeSense(self, makesense) -> int:
        self.makeSense = makesense
        return 0

    def setValidated(self, validated) -> int:
        self.validated = validated
        return 0

    def getFinalSentence(self) -> str:
        return self.finalSentence

    def __setFinalSentence(self, final_sentence) -> int:
        self.finalSentence = final_sentence
        return 0

    def validate(self):
        pass

    def translate(self) -> list:  # This function return will be passed to the compiler
        pass


# Class object compiler as provided in the design
class Compiler:
    def __init__(self):
        self.compiledSentence = list()

    def __setCompiledSentence(self, sentence=list()) -> 0:
        self.compiledSentence = sentence
        return 0

    def getCompiledSentence(self) -> list:
        return self.compiledSentence
