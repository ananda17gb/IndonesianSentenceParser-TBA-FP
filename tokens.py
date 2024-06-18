from fa.S.ana import ANA
from fa.S.ani import ANI
from fa.S.anu import ANU
from fa.S.ane import ANE
from fa.S.ano import ANO

from fa.O.sampah import SAMPAH
from fa.O.sampan import SAMPAN
from fa.O.sampul import SAMPUL
from fa.O.samsak import SAMSAK
from fa.O.samsir import SAMSIR

from fa.P.membaca import MEMBACA
from fa.P.membakar import MEMBAKAR
from fa.P.membayar import MEMBAYAR
from fa.P.membeli import MEMBELI
from fa.P.membuang import MEMBUANG

from fa.K.di_pasar import DI_PASAR
from fa.K.di_plaza import DI_PLAZA
from fa.K.di_TPA import DI_TPA
from fa.K.di_warteg import DI_WARTEG
from fa.K.di_warung import DI_WARUNG

class TOKEN_RECOGNIZER:
    def get_lexical(self, word):
        if ANA().valid(word):
            return "1"
        elif ANI().valid(word):
            return "2"
        elif ANU().valid(word):
            return "3"
        elif ANE().valid(word):
            return "4"
        elif ANO().valid(word):
            return "5"
        elif SAMPAH().valid(word):
            return "11"
        elif SAMPAN().valid(word):
            return "12"
        elif SAMPUL().valid(word):
            return "13"
        elif SAMSAK().valid(word):
            return "14"
        elif SAMSIR().valid(word):
            return "15"
        elif MEMBACA().valid(word):
            return "6"
        elif MEMBAKAR().valid(word):
            return "7"
        elif MEMBAYAR().valid(word):
            return "8"
        elif MEMBELI().valid(word):
            return "9"
        elif MEMBUANG().valid(word):
            return "10"
        elif DI_PASAR().valid(word):
            return "16"
        elif DI_PLAZA().valid(word):
            return "17"
        elif DI_TPA().valid(word):
            return "18"
        elif DI_WARTEG().valid(word):
            return "19"
        elif DI_WARUNG().valid(word):
            return "20"
        else:
            return False

    def get_tokens(self, sentence):
        result_token = []
        words = sentence.split()

        # ["Ana", "membaca", "sampul", "di", "plaza"]

        i = 0
        while i < len(words):
            if words[i] == "di" and i + 1 < len(words):
                word = words[i] + " " + words[i + 1]
                i += 2
            else:
                word = words[i]
                i += 1
            result_token.append(self.get_lexical(word))

        # ["Ana", "membaca", "sampul", "di plaza"]

        result_token.append("#")
        return result_token

    def classify_tokens(self, tokens):
        subjects = ["1", "2", "3", "4", "5"]
        predicates = ["6", "7", "8", "9", "10"]
        objects = ["11", "12", "13", "14", "15"]
        adverbs = ["16", "17", "18", "19", "20"]

        structure = " => "

        for token in tokens:
            if token != "#":
                if token in subjects:
                    structure += "S "
                elif token in predicates:
                    structure += "P "
                elif token in objects:
                    structure += "O "
                elif token in adverbs:
                    structure += "K "

        return structure