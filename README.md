# PASSWORD CHECKER (personal project)

This program checks if a password is secure or not based on whether it was ever leaked or not. The API (from https://haveibeenpwned.com/) accepts the first 5 characters of the password in hash form, and it respondes with the remaning hash of all the matching passwords, which are later processed locally to make the process more secure (the complete password never leaves the computer).

To run the program, on the root folder of the project run "python passwordChecker.py {password1} {password2} ... {password_n}."

The program is only going to work with an internet connection.