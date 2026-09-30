def login(username, password):
    if username == "admin" and password == "1234":
        return "Login successful"
    return "Invalid username or password"

print(login("admin", "1234"))
