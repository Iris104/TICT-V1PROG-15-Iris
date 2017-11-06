cijferlijst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def new_password (oldpassword, newpassword):
    cin = False
    for nummer in cijferlijst:
        if nummer in newpassword:
            cin=True
    if oldpassword != newpassword and len(newpassword) >= 6 and cin:
        return True
    else:
        return False

res = new_password('vakProg17', 'python17')
print(res)

print(new_password('huProg17', 'huProg17'))

print(new_password('vakProg17', 'Prog17'))

print(new_password('vakProg17', 'huProgrammeren'))
