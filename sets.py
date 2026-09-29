registered_users = {
    "user101",
    "user102",
    "user103",
    "user104"
}

username = input("Enter username: ")

if username in registered_users:
    print("Access granted.")
else:
    print("Access denied. User not registered.")