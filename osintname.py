#! /usr/bin/env python3
import argparse
from itertools import permutations

def banner():
    print("""
        _     _                       
 ___ __(_)_ _| |_ _ _  __ _ _ __  ___ 
/ _ (_-< | ' \  _| ' \/ _` | '  \/ -_)
\___/__/_|_||_\__|_||_\__,_|_|_|_\___|
        Emails and Usernames Generator
    """)

def username_gen(firstname, lastname, domain=None):
    username_set = set()

    # Generate permutations
    permuted_names = permutations([firstname, lastname])

    # Format and add to the set
    for perm in permuted_names:
        username_set.add(".".join(perm))
        username_set.add("".join(perm))
        username_set.add("".join(perm[::-1]))

    # Add combinations
    username_set.add(firstname + lastname)
    username_set.add(lastname + firstname)

    if domain:
        # Add email format
        for username in username_set:
            email_username = f"{username}@{domain}"
            print(email_username)

        # Print individual components in the email format
        email_firstname = f"{firstname.lower()}@{domain}"
        email_lastname = f"{lastname.lower()}@{domain}"
        print(email_firstname)
        print(email_lastname)
    else:
        # Print regular usernames and individual components with or without domain
        for username in username_set:
            print(username)

        if domain:
            # Print individual components in the email format
            email_firstname = f"{firstname.lower()}@{domain}"
            email_lastname = f"{lastname.lower()}@{domain}"
            print(email_firstname)
            print(email_lastname)
        else:
            # Print individual components without domain
            print(firstname.lower())
            print(lastname.lower())

    return list(username_set)

def name_list(filename):
    try:
        with open(filename, 'r') as file:
            names = file.read().splitlines()
            return [name.lower() for name in names]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def main():
    parser = argparse.ArgumentParser(description='Generate Emails and Usernames from Provided Lists of Names')
    parser.add_argument('--list', '-l', type=str, required=True, help='File containing a list of names.')
    parser.add_argument('--domain', '-d', type=str, help='Email domain for generating email-format usernames.')

    args = parser.parse_args()

    names = name_list(args.list)

    if names:
        for name in names:
            name_parts = name.split()
            if len(name_parts) == 2:
                firstname, lastname = name_parts
                username_gen(firstname.lower(), lastname.lower(), args.domain)
            elif len(name_parts) > 2:
                firstname, lastname = name_parts[0], name_parts[-1]
                username_gen(firstname.lower(), lastname.lower(), args.domain)
            elif len(name_parts) == 1:
                if args.domain:
                    # Print individual components in the email format
                    email_firstname = f"{name.lower()}@{args.domain}"
                    print(email_firstname)
                else:
                    # Print the name if only one word without domain
                    print(name.lower())
            else:
                print(f"Invalid format for name: {name}.")
            
if __name__ == "__main__":
    banner()
    main()
