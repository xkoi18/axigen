#split function to read out of mailadress


email = 'marius.rudat@web.de'

def email_splitter(email):
    username = email.split('@')[0]
    vorname = username.split('.')[0]
    nachname = username.split('.')[1]
    domain = email.split('@')[1]
    domain_name = domain.split('.')[0]
    domain_type = domain.split('.')[1]

    print('Username : ', username)
    print('Vorname : ', vorname)
    print('Nachname :', nachname)
    print('Domain :', domain)
    print('Domain   : ', domain_name)
    print('Type     : ', domain_type)


email_splitter(email)