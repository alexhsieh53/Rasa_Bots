from rasa_nlu.model import Interpreter
from opencc import OpenCC
import json
interpreter = Interpreter.load("C:\\Users\\user\\Desktop\\Spacy_Rasa_NLU\\models\\current\\nlu")
cc = OpenCC('t2s')
message = "告訴我後天星期幾"
converted = cc.convert(message)
result = interpreter.parse(converted)
print(json.dumps(result, indent=2))