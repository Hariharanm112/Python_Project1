import logging

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler("app.log",mode="w"),
    logging.StreamHandler()
    ]
)

users={
    "admin":"1234",

}

# Login function with logging
def login(username,password):
    logging.info(f"Login attempt started for user: {username}")

    if username not in users:
        logging.warning(f"Login failed: User '{username}' does not exist")
        return False

    if users[username] != password:
        logging.critical(f"Login failed: Incorrect password for '{username}'")
        return False

    logging.info(f"Login successful for user: {username}")
    return True


# Interactive login simulation
def main():
    print("===== Welcome to the Login System =====")
    username = input("Enter username: ")
    password = input("Enter password: ")

    success = login(username, password)

    if success:
        print("Login successful ✅")
    else:
        print("Login failed ❌")


# Run the program
if __name__ == "__main__":
    main()
