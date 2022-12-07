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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 7000))

#read cli prompt
test_command_success("CLI not found")

#send login command
s.send('user admin\r\n')
data = s.recv(1024)

#send passwd
s.send('adamopel\r\n')
test_command_success("User or Password wrong")

print("1. Create account ")
print("2. Delete account ")
print("3. Accounts from list ")
while True:

    try:
        choice = int(input("Choose action "))
        break
    except:
        print("Please enter number ")

if choice == 1:
    #UPDATE domain
    domain_name = input('Domain Name?: ')
    check_for_space(domain_name)
    s.send('update domain '+domain_name+'\r\n')
    test_command_success("Domain "+domain_name+" not found/exists")

    #Get Account Infos
    first_name = input('First Name?: ')
    last_name = input('Last Name?: ')
    account_name = input('Account Name?: ')
    check_for_space(account_name)
    password = input('Password: ')
    check_for_space(password)

    #Create Account
    s.send('add account '+account_name+' password '+password+'\r\n')
    test_command_success("add account error")

    #save
    s.send('commit\r\n')
    test_command_success("commit Error")

    #go sleep
    time.sleep(2)
    print("Basic Account created (Username and Password)")

    #UPDATE domain
    s.send('update domain '+domain_name+'\r\n')
    test_command_success("Domain "+domain_name+" not found/exists")

    # select account
    s.send('update account ' +account_name+'\r\n')
    test_command_success("Account "+account_name+" not found/exists")

    # set account type basic
    s.send('set accountType basic\r\n')
    test_command_success("Account type basic error")

    # switch to config contactinfos
    s.send('CONFIG ContactInfo\r\n')
    data = s.recv(1024)

    # set first name
    s.send('set firstName \"'+first_name+'\"\r\n')
    test_command_success("firstname error")

    # set last name
    s.send('set lastName \"'+last_name+'\"\r\n')
    test_command_success("lastname error")

    #save
    s.send('done\r\n')
    test_command_success("done Error")
    s.send('commit\r\n')
    test_command_success("commit Error")
    print("Full Account created (First Name, Last Name, Account Type Basic)")

elif choice == 2:
    #UPDATE domain
    domain_name = input('Domain Name?: ')
    check_for_space(domain_name)
    s.send('update domain '+domain_name+'\r\n')
    test_command_success("Domain "+domain_name+" not found/exists")

    # select account
    account_name = input('Account Name?: ')
    check_for_space(account_name)
    s.send('update account ' +account_name+ '\r\n')
    test_command_success("Account not found/exists")

    #rename account
    s.send('set name 00_'+str(now.year)+'0'+str(now.month)+''+str(now.day)+'_'+account_name+'\r\n')
    test_command_success("rename error")

    #create password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    temp = random.sample(all,10)
    password = "".join(temp)

    # set password for user
    s.send('set password '+password+'\r\n')
    test_command_success("set password error")

    # disable contact info
    s.send('set publishContactInfo no\r\n')
    test_command_success("disable contact info error")

    # disable all services only maxmo
    if domain_name == "maxmo.de":
        s.send('INHERIT SETTINGS FROM accountClass disabled_accounts\r\n')
        test_command_success("disable all services error")

        #save
        s.send('commit\r\n')
        test_command_success("commit Error")
if choice == 3:

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
        firstname = username.split('.')[0]
        lastname = username.split('.')[1]
        domain = email.split('@')[1]
        domain_1 = domain.split(' ')[0]
        # Output of generated User
        print('Username : ', username)
        print('Vorname : ', firstname)
        print('Nachname :', lastname)
        print('Domain :', domain_1)
        print('Password : ', password, '\n')


    for i in range(0, len(lst)), 2):
        new_list = ''.join(lst[i:i + 2])
        email_splitter(new_list)

        #Domain
        #domain_name = input('Domain Name?: ')
        check_for_space(domain_1)
        s.send('update domain '+domain_1+'\r\n')
        test_command_success("Domain "+domain_1+" not found/exists")

        #Get Account Infos
        #first_name = input('First Name?: ')
        #last_name = input('Last Name?: ')
        #account_name = input('Account Name?: ')
        check_for_space(username)
        #password = input('Password: ')
        check_for_space(password)

        #Create Account
        s.send('add account '+username+' password '+password+'\r\n')
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
        s.send('update account ' +username+'\r\n')
        test_command_success("Account "+username+" not found/exists")

        # set account type basic
        s.send('set accountType basic\r\n')
        test_command_success("Account type basic error")

        # switch to config contactinfos
        s.send('CONFIG ContactInfo\r\n')
        data = s.recv(1024)

        # set first name
        s.send('set firstName \"'+firstname+'\"\r\n')
        test_command_success("firstname error")

        # set last name
        s.send('set lastName \"'+lastname+'\"\r\n')
        test_command_success("lastname error")

        #save
        s.send('done\r\n')
        test_command_success("done Error")
        s.send('commit\r\n')
        test_command_success("commit Error")
        print("Full Account created (First Name, Last Name, Account Type Basic)")

else:
    print("Bitte nur Zahlen zwischen 1 und 2 eingeben!")

# close
    s.close()
