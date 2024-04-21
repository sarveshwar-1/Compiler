symbols = ['{','}','(',')',';','+','=','>','<','~','|','&','*','/','-','%','.','[',']',',']
keywords = ['if','let','var','else','while','class','function','method','int','void','char','static','do','null','this','true','false','return']
integer = "0123456789"

class Token:
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __repr__(self):
        return f"<{self.type}>{self.value}</{self.type}>"

data = "2+hi3+4 if\"hello\""
tokens = []
i = 0

while i < len(data):
    if data[i] in integer:
        num = data[i]
        while i + 1 < len(data) and data[i + 1] in integer:
            i += 1
            num += data[i]
        tokens.append(Token(num, 'integerConstant'))
    elif data[i] in symbols:
        tokens.append(Token(data[i], 'symbol'))
    elif data[i] == "\"":
        i += 1
        text = ''
        while i < len(data) and data[i] != "\"":
            text += data[i]
            i += 1
        tokens.append(Token(text, 'stringConstant'))
    elif data[i].isalpha():
        text = data[i]
        while i + 1 < len(data) and data[i + 1].isalpha():
            i += 1
            text += data[i]
        if text in keywords:
            tokens.append(Token(text, 'keyword'))
        else:
            tokens.append(Token(text, 'identifier'))
    i += 1

for token in tokens:
    print(token)
