from Token import Token

symbols = ['{','}','(',')',';','+','=','>','<','~','|','&','*','/','-','%','.','[',']',',']
keywords = ['if','let','var','else','while','class','function','method','int','void','char','static','do','null','this','true','false','return']
integer = "0123456789"

def remove_comments(data):
    i = 0
    while i < len(data):
        if data[i] == '/' and data[i+1] == '/':
            while data[i] != '\n':
                data.pop(i)
        
        if data[i] == '/' and data[i+1] == '*' and data[i+2] == '*':
            #.    **
            while data[i:i+2] != list('*/'):
                data.pop(i)
        if data[i] == '*' and data[i+1] == '/':
            data.pop(i)
            data.pop(i)
        
        i+=1
    return "".join(data)


def make_tokens(data):
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
    
    return tokens


def run(data):
    data = remove_comments(data)
    tokens = make_tokens(data)
    return tokens