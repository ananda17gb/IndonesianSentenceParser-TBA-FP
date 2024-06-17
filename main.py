from tokens import TOKEN_RECOGNIZER
from parsers import PARSER

print("Check Indonesian Sentence Structure Parser\n")
print("""Made by:
    Ruly Bija (1301224171)
    Ananda Arti Widigdo (1301224386)
    Devin Prawira Arissaputra (1301224478)
""")

print("""
Token list:
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| 1   | 2   | 3   | 4   | 5   | 6       | 7        | 8        | 9         | 10       | 11       | 12     | 13     | 14     | 15     | 16       | 17       | 18       | 19        | 20        |
| --- | --- | --- | --- | --- | ------- | -------  | -------- | --------- | -------- | -------- | ------ | ------ | ------ | ------ | -------- | -------- | -------- | --------- | --------- |
| Ana | Ani | Anu | Ane | Ano | membaca | membakar | membayar |  membeli  | membuang |  sampah  | sampan | sampul | samsak | samsir | di pasar | di plaza |  di TPA  | di warteg | di warung |
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
""")

sentences = input("Enter sentences: ")
print()

token_recognizer = TOKEN_RECOGNIZER()
parser = PARSER()

tokens = token_recognizer.get_tokens(sentences)
structure = token_recognizer.classify_tokens(tokens)
print("Token Recognizer Results:")
print(tokens, structure)
print()

if parser.valid(tokens):
    print("The sentence is valid.")
else:
    print("The sentence is invalid.")