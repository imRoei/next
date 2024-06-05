def craked_password(password):
    return ''.join(list(chr(ord(x)+2) for x in password))



password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
print(craked_password(password))