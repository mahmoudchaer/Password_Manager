print("Welcome to the password manager!")
print("This program will help you store your passwords securely.\n")

print("Commands:")
print("cmds - Show commands")
print("add - Add a new password")
print("view all - View all passwords")
print("view category - View passwords by category")
print("change category - Change the category of a password with a new or existing category")
print("search - Search for a term in the passwords")
print("edit - Edit a password\n")

categories = set()  # Set to store existing categories

# Function to check if a name already exists and return an enumerated version if necessary
def get_unique_name(name, entries):
    existing_names = [entry.split("\n")[1].split(": ")[1].strip().lower() for entry in entries]
    original_name = name.lower()
    counter = 1
    while name.lower() in existing_names:
        name = f"{original_name}{counter}"
        counter += 1
    return name

# Updated function to add a password with or without a category and handle name enumeration
def add():
    with open("mypasswords.txt", "r") as file:
        entries = file.read().strip().split("\n\n")

    category = input("Enter the category (leave empty if no category): ").strip().lower()
    name = input("Enter the name: ").strip()

    # Check if name exists and get a unique name if necessary
    name = get_unique_name(name, entries)

    username = input("Enter the username: ")
    password = input("Enter the password: ")
    email = input("Enter the email: ")
    info = input("Enter any other information: ")

    with open("mypasswords.txt", "a") as file:
        if category:
            categories.add(category)  # Add to categories if provided
            file.write(f"Category: {category}\n")
        else:
            file.write("Category: None\n")  # Mark as 'None' if no category
        file.write(f"Name: {name}\n")
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Info: {info}\n\n")

    print(f"Password added with name: {name}!")

# Updated function to edit a password entry and handle name enumeration
def edit():
    search_name = input("Enter the name of the password you want to edit: ").strip()

    with open("mypasswords.txt", "r") as file:
        entries = file.read().strip().split("\n\n")

    for i, entry in enumerate(entries):
        if f"Name: {search_name}" in entry:
            print("Current entry:\n")
            print(entry)
            print("\n" + "-" * 40 + "\n")

            field = input("Enter the field to edit (name, username, password, email, info, category): ").strip().lower()
            new_value = input(f"Enter new {field}: ")

            # Replace the chosen field with the new value
            lines = entry.split("\n")
            for j, line in enumerate(lines):
                if line.lower().startswith(field + ":"):
                    if field == "name":
                        # Ensure the new name is unique
                        new_value = get_unique_name(new_value, entries)
                    lines[j] = f"{field.capitalize()}: {new_value}"

            # Update the entry
            entries[i] = "\n".join(lines)
            break
    else:
        print("Password not found.")

    # Write updated entries back to the file
    with open("mypasswords.txt", "w") as file:
        file.write("\n\n".join(entries))

    print("Password updated!")

# Function to view all passwords
def view_all():
    with open("mypasswords.txt", "r") as file:
        entries = file.read().strip().split("\n\n")
        for entry in entries:
            print(entry)
            print("\n" + "-" * 40 + "\n")

# Function to view passwords by category
def view_category():
    with open("mypasswords.txt", "r") as file:
        entries = file.read().strip().split("\n\n")
        
        # Clear categories and populate it again based on the file content
        categories.clear()  # Clear any previous categories
        for entry in entries:
            lines = entry.split("\n")
            for line in lines:
                if line.startswith("Category: "):
                    category = line.split(": ")[1].strip().lower()
                    if category != "none":
                        categories.add(category)  # Add the category to the set

    if not categories:
        print("No categories available yet. Add a password with a category first.")
        return
    
    # Show available categories before prompting for input
    print(f"Available categories: {', '.join(categories)}")
    
    category = input("Enter the category you want to view: ").strip().lower()
    found = False
    for entry in entries:
        if f"Category: {category}" in entry:
            print(entry)
            print("\n" + "-" * 40 + "\n")
            found = True
    if not found:
        print(f"No passwords found under the category '{category}'.")

# Function to change the category of a password based on its username
def change_category():
    # Read the file and split into entries
    with open("mypasswords.txt", "r") as file:
        entries = file.read().strip().split("\n\n")

    # Clear categories and populate them again from the file content
    categories.clear()
    for entry in entries:
        lines = entry.split("\n")
        for line in lines:
            if line.startswith("Category: "):
                category = line.split(": ")[1].strip().lower()
                if category != "none":
                    categories.add(category)

    if not categories:
        print("No categories exist yet. Add a password with a category first.\n")
        return

    # Ask for username input and search for it
    search_username = input("Enter the username of the password to change its category: ").strip()
    found_entry = None

    # Search for the password entry by username
    for i, entry in enumerate(entries):
        # Split the entry into lines and look for the "Username:" field
        lines = entry.split("\n")
        for line in lines:
            if line.startswith("Username: "):
                stored_username = line.split(": ")[1].strip()  # Extract the username
                if stored_username == search_username:  # Compare with input username
                    found_entry = entry  # If found, assign the entry
                    break
        if found_entry:
            break  # Exit the loop once the entry is found

    if found_entry:
        print("Password found:\n")
        print(found_entry)
        print("\n" + "-" * 40 + "\n")

        # Show the current category
        for line in found_entry.split("\n"):
            if line.startswith("Category:"):
                current_category = line.split(": ")[1]
                break
        print(f"Current category: {current_category}\n")

        # Ask user to input the new category
        new_category = input(f"Enter new category (available categories: {', '.join(categories)}): ").strip().lower()

        # If the new category doesn't exist, add it to the categories set
        if new_category not in categories and new_category != "":
            print(f"Category '{new_category}' does not exist. It will be created.")
            categories.add(new_category)

        # Update the entry with the new category
        updated_lines = found_entry.split("\n")
        for j, line in enumerate(updated_lines):
            if line.startswith("Category:"):
                updated_lines[j] = f"Category: {new_category if new_category else 'None'}"

        # Update the password entry
        entries[i] = "\n".join(updated_lines)

        # Write the updated entries back to the file
        with open("mypasswords.txt", "w") as file:
            file.write("\n\n".join(entries))

        print(f"Category changed to '{new_category}' successfully!")
    else:
        print("Password not found.")


# Function to search for a term in passwords
def search():
    term = input("Enter the term you want to search for: ").strip().lower()
    with open("mypasswords.txt", "r") as file:
        entries = file.read().strip().split("\n\n")
        found = False
        for entry in entries:
            if term in entry.lower():
                print(entry)
                print("\n" + "-" * 40 + "\n")
                found = True
        if not found:
            print(f"No results found for '{term}'.")

# Function to show commands
def cmds():
    print("Commands:")
    print("cmds - Show commands")
    print("add - Add a new password")
    print("view all - View all passwords")
    print("view category - View passwords by category")
    print("change category - Change the category of a password with a new or existing category")
    print("search - Search for a term in the passwords")
    print("edit - Edit a password\n")

# Main loop
while True:
    command = input("Enter command: ").strip().lower()
    print("")

    if command == "add":
        add()
    elif command == "view all":
        view_all()
    elif command == "view category":
        view_category()
    elif command == "change category":
        change_category()
    elif command == "search":
        search()
    elif command == "edit":
        edit()
    elif command == "cmds":
        cmds()
    else:
        print("Invalid command. Type 'cmds' to see the list of available commands.")
