uname = 'Admin'
pwd = 'Admin123'

attempt = 0
while True:
    attempt+= 1
    print (f'Attempt{attempt} of 3')
    username = input('Enter username: ')
    password = input('Enter password: ')
    if attempt == 3:
        print('too many attempt')
    if username !=uname:
        print('❌ Invalid username')
    if password !=pwd:
        print('❌ Invalid password')
    if username == uname and password == pwd:
        print('🟩 Login successful')
        break