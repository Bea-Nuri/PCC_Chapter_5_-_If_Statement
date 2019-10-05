current_users = ['eric', 'rita', 'danny', 'shawn', 'cherry', 'sandra']
new_users = ['Shawn', 'thomas', 'james', 'eric', 'matt']
for new_user in new_users:
    if new_user.lower() in current_users:  #.lower case method make this new user even with different case, insensitive
        print("user name is unavailable, enter new user name")
    else:
        print("that user name is available")