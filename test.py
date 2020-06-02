from os import system

name = ''
with open("name", "r") as f:
    name = f.read()
 
message = ''
with open("diff", "r") as f:
    message = f.read()
    message = message.replace('\n', '\\n')
    message = message.replace('<', '+')
    message = message.replace('>', '-')

system("messer --command='m \"" + name[:-1] + "\" " + message + '\'')
