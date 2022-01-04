# No es necesario agregar la palabra return

palindrome = lambda string: string == string[::-1]

print(palindrome('ana'))

# funcion normal
def palindrome_two(string):
    return string == string[::-1]

print(palindrome_two('oto'))