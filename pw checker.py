def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        print('de lengte moet minimaal 6 characters lang zijn')
        val = False

    if len(passwd) > 20:
        print('de lengte mag niet groter dan 20 characters zijn')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Het wachtwoord moet minimaal 1 nummer bevatten')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Het wachtwoord moet minimaal 1 hoofdletter bevatten')
        val = False

    if not any(char.islower() for char in passwd):
        print('Het wachtwoord moet minimaal 1 kleine letter bevatten')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Het wachtwoord moet minimaal 1 $@# van deze symbolen bevatten ')
        val = False
    if val:
        return val

def main():
    passwd = input('Voer hier je wachtwoord in ')

    if (password_check(passwd)):
        print("Password is valid")
    else:
        print("Invalid Password !!")

if __name__ == '__main__':
    main()
