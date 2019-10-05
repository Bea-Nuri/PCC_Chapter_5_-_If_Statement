users = ['eric', 'thomas', 'faldo', 'rita', 'danny', 'admin']
for user in users:
    if user == 'admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again.")
