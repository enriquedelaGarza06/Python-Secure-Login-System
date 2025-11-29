import bcrypt  # Import security library

#==================================================
# PRACTICE: SIGN IN BASIC SYSTEM (SECURE VERSION)
#==================================================

# Dictionary simulating a database.
# NOTE: In a real system, we would have stored the hashes here, not plain text.
# As an example, we leave the dictionary empty at the start so you can register new users.
registered_users = {} 


#==================================================
# FUNCTION: show_menu()
#==================================================
def show_menu():
    print("\n====== MENU ======")
    print("1. Sign In")
    print("2. Register User")
    print("3. Exit")
    print("========================")


#=================================================
# FUNCTION: sign_in()
# Validates the encrypted password
#=================================================
def sign_in():
    print("\n--- SIGN IN ---")
    
    user = input("Enter your username: ")
    password = input("Enter your password: ")

    # 1. Check if the user exists
    if user in registered_users:
        
        # Retrieve the stored HASH (the encrypted text)
        stored_password_hash = registered_users[user]

        # 2. Convert the password typed by the user to bytes
        password_bytes = password.encode('utf-8')

        # 3. SECURE VERIFICATION:
        # bcrypt compares the typed password with the stored hash.
        # It automatically extracts the "salt" from the hash and performs the calculation.
        if bcrypt.checkpw(password_bytes, stored_password_hash):
            print(f"✓ Welcome {user}! You have logged in successfully.")
        else:
            print("✘ Incorrect password.")
    
    else:
        print("✘ The user does not exist. Register it first.")


#=================================================
# FUNCTION: sign_up()
# Creates users with encrypted password
#=================================================
def sign_up():
    print("\n--- SIGN UP ---")

    new_user = input("Choose a username: ")

    if new_user in registered_users:
        print("✘ This username is already taken.")
        return
    
    new_password = input("Choose a password: ")

    # --- HERE IS WHERE THE SECURITY MAGIC HAPPENS ---
    
    # 1. Convert the password to bytes (required by the library)
    password_bytes = new_password.encode('utf-8')

    # 2. Generate the "salt" and encrypt the password
    # This meets the requirement: uses a dynamic key (gensalt)
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    # 3. Save THE HASH (not the real password) in the dictionary
    registered_users[new_user] = hashed_password

    print(f"✓ User '{new_user}' registered successfully.")
    # (Optional) Print the hash so you can see how it looks in the DB
    print(f"(Secret stored in DB: {hashed_password})")


#=================================================
# MAIN PROGRAM
#=================================================
while True:
    show_menu()
    option = input("Pick an option (1-3): ")

    if option == "1":
        sign_in()
    elif option == "2":
        sign_up() 
    elif option == "3":
        print("👋 Shutting down... Goodbye")
        break
    else:
        print("✘ Invalid option. Try again.")