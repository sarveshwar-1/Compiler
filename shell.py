from tokeniser import run

f = open("/Users/aksaykanthan/Development/nand2tetris/projects/10/Square/Main.jack", "r")
data = list(f.read())
f.close()


print(*run(data),sep='\n')


