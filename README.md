
# Password Manager

A simple and secure password manager built with Python. This program helps you securely store, organize, and manage your passwords. It allows you to add, edit, view, and search passwords based on categories or other details

## Features

- **Add passwords**: Store passwords with associated details like username, category, and additional information.
- **Edit passwords**: Modify any stored password or its associated details.
- **View passwords**: Display all stored passwords or filter them by category.
- **Categorization**: Organize passwords into custom categories for easy management.
- **Search functionality**: Quickly locate passwords by searching for specific terms.
- **Change categories**: Update the category of any stored password.

## Requirements

- Python 3.6+

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mahmoudchaer/Password_Manager
   cd password-manager
   ```

2. Ensure Python is installed on your system.

3. Run the script:

   ```bash
   python password_manager.py
   ```

## Commands

| Command            | Description                                          |
|---------------------|------------------------------------------------------|
| **cmds**           | Show all available commands.                        |
| **add**            | Add a new password with details.                    |
| **view all**       | View all stored passwords.                          |
| **view category**  | View passwords filtered by a specific category.     |
| **change category**| Change the category of a stored password.           |
| **search**         | Search for a term across all stored passwords.      |
| **edit**           | Edit the details of a stored password.              |

## Usage Examples

### Add a New Password
- Run the script and type `add`.
- Follow the prompts to enter the category, name, username, password, email, and additional information.
- The password will be saved in the `mypasswords.txt` file.

### View All Passwords
- Type `view all` to display all stored passwords.

### View Passwords by Category
- Type `view category` and input the desired category to see relevant passwords.

### Edit a Password
- Type `edit` and follow the prompts to locate and modify a password.

### Search for a Term
- Type `search` and enter a term to locate matching passwords.

## Sample mypasswords.txt

```
Category: social media
Name: facebook account
Username: john.doe
Password: Passw0rd123!
Email: john.doe@example.com
Info: Facebook personal account

Category: banking
Name: online banking
Username: john.doe
Password: MySecureBank123
Email: john.doe@bank.com
Info: Main checking account

Category: email
Name: work email
Username: jdoe.work
Password: WorkEmail456!
Email: jdoe@company.com
Info: Corporate email account

Category: entertainment
Name: netflix account
Username: john.doe.netflix
Password: StreamLover789
Email: john.doe@gmail.com
Info: Shared family account
```

## Notes

- All passwords are stored in plaintext in the `mypasswords.txt` file. For enhanced security, consider encrypting the file.
- Ensure the `mypasswords.txt` file is stored in a secure location and avoid sharing it publicly.

## Contribution

Contributions are welcome! Feel free to fork the repository and submit a pull request.
