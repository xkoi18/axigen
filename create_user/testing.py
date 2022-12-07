with open('mailadr', 'r+') as file:
    lines = file.readlines()  # Read all lines and
    file.seek(0)  # Remove all existing lines
    file.writelines(line for line in lines if line.strip())  # Write all lines into file and skip all empty lines with line.strip()
    #print('before', lines)
lst = []
for x in lines:
    lst.append(x.replace('\n', " "))

print(lst)
'''new_lst = lst
global var
var = -1
while var < len(new_lst):
    var += 2
    new_str = ''.join(new_lst[var])
    print(new_str)'''

def email_splitter(email):
    password = email.split()[1]
    username = email.split('@')[0]
    vorname = username.split('.')[0]
    nachname = username.split('.')[1]
    domain = email.split('@')[1]
    domain_1 = domain.split(' ')[0]
    #domain_name = domain.split('.')[0]
    #domain_type = domain.split('.')[1]

    print('Password : ', password)
    print('Username : ', username)
    print('Vorname : ', vorname)
    print('Nachname :', nachname)
    print('Domain :', domain_1)
    #print('Domain   : ', domain_name)
    #print('Type     : ', domain_type)


for i in range(0, len(lst), 2):
    #pair = lst[i:i+2]
    #email_splitter(pair)
    new_list = ''.join(lst[i:i + 2])
    email_splitter(new_list)


'''new_lst = lst[:2]
print('after ', len(new_lst), new_lst)
new_str = ''.join(new_lst)
print(new_str)
email = new_str'''


'''
def email_splitter(email):
    password = email.split()[1]
    username = email.split('@')[0]
    vorname = username.split('.')[0]
    nachname = username.split('.')[1]
    domain = email.split('@')[1]
    domain_1 = domain.split(' ')[0]
    #domain_name = domain.split('.')[0]
    #domain_type = domain.split('.')[1]

    print('Password : ', password)
    print('Username : ', username)
    print('Vorname : ', vorname)
    print('Nachname :', nachname)
    print('Domain :', domain_1)
    #print('Domain   : ', domain_name)
    #print('Type     : ', domain_type)

email_splitter(email)

'''