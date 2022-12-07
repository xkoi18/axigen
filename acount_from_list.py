### USES AXIGEN API TO CREATE NEW USERS FROM LIST. THERE FORE IT IS IMPORTANT TO HAVE A LIST NAMED "mailadr"
### WHICH HAS A STRUCTURE OF MAIL ADRESS AND PASSWORD IN CHANGE

import socket,sys,os,random,string,datetime,time

now = datetime.datetime.now()
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()

def test_command_success(error):
  data = s.recv(1024)
  if '+OK: command successful' in data:
        pass
  elif 'committing changes and switching back to previous context' in data:
        pass
  elif '+OK: Authentication successful' in data:
        pass
  elif 'Welcome to AXIGEN\'s Command Line Interface' in data:
        pass
  else:
        print(data)
        sys.exit("ACHTUNG: "+error+"\n\n-------"+data+"\n--------")

def check_for_space(input):
  if " " in input:
       sys.exit("ACHTUNG: Leerzeichen in der Eingabe")




with open('mailadr', 'r+') as file:
    lines = file.readlines()
    file.seek(0)
    file.writelines(line for line in lines if line.strip())

lst = []
for x in lines:
    lst.append(x.replace('\n', " "))

def email_splitter(email):
    global domain_1
    global password
    global username
    global firstname
    global lastname
    global domain
    password = email.split()[1]
    username = email.split('@')[0]
    firstname = username.split('.')[0]
    lastname = username.split('.')[1]
    domain = email.split('@')[1]
    domain_1 = domain.split(' ')[0]

    print('Username : ', username)
    print('Vorname : ', firstname)
    print('Nachname :', lastname)
    print('Domain :', domain_1)
    print('Password : ', password,'\n')

for i in range(0, len(lst), 2):
    new_list = ''.join(lst[i:i + 2])
    email_splitter(new_list)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 7000))

    # read cli prompt
    test_command_success("CLI not found")

    # send login command
    s.send('user admin\r\n')
    data = s.recv(1024)

    # send passwd
    s.send('adamopel\r\n')
    test_command_success("User or Password wrong")

    #Domain
    #domain_name = input('Domain Name?: ')
    check_for_space(domain_1)
    s.send('update domain '+domain_1+ '\r\n')
    test_command_success("Domain " +domain_1+ " not found/exists")


    #Get Account Infos
    #first_name = input('First Name?: ')
    #last_name = input('Last Name?: ')
    #account_name = input('Account Name?: ')
    check_for_space(username)
    #password = input('Password: ')
    check_for_space(password)

    #Create Account
    s.send('add account '+username+' password '+password+'\r\n')
    print('add account '+username+' password '+password+'\r\n')
    test_command_success("add account error")

    #save
    s.send('commit\r\n')
    test_command_success("commit Error")

    #go sleep
    time.sleep(2)
    print("Basic Account created (Username and Password)")

    #UPDATE domain
    s.send('update domain '+domain_1+'\r\n')
    test_command_success("Domain "+domain_1+" not found/exists")

    # select account
    s.send('update account '+username+'\r\n')
    test_command_success("Account "+username+" not found/exists")

    # set account type basic
    s.send('set accountType basic\r\n')
    test_command_success("Account type basic error")

    # switch to config contactinfos
    s.send('CONFIG ContactInfo\r\n')
    data = s.recv(1024)

    # set first name
    s.send('set firstName \"' +firstname+ '\"\r\n')
    test_command_success("firstname error")

    # set last name
    s.send('set lastName \"' +lastname+ '\"\r\n')
    test_command_success("lastname error")

    #save
    s.send('done\r\n')
    test_command_success("done Error")
    s.send('commit\r\n')
    test_command_success("commit Error")
    print("Full Account created (First Name, Last Name, Account Type Basic)")

    s.close()