with open('mailadr', 'r+') as file:
    lines = file.readlines()
    file.seek(0)
    file.writelines(line for line in lines if line.strip())

lst = []
for x in lines:
    lst.append(x.replace('\n', " "))

def email_splitter(email):
    password = email.split()[1]
    username = email.split('@')[0]
    vorname = username.split('.')[0]
    nachname = username.split('.')[1]
    domain = email.split('@')[1]
    domain_1 = domain.split(' ')[0]

    print('Username : ', username)
    print('Vorname : ', vorname)
    print('Nachname :', nachname)
    print('Domain :', domain_1)
    print('Password : ', password,'\n')

for i in range(0, len(lst), 2):
    new_list = ''.join(lst[i:i + 2])
    email_splitter(new_list)