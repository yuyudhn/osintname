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

def generate_usernames(firstname, lastname):
    username_set = set()
    
    # Generate permutations and add various combinations
    for perm in permutations([firstname, lastname]):
        username_set.add(".".join(perm))
        username_set.add("".join(perm))
    
    # Basic combinations
    username_set.add(firstname + lastname)
    username_set.add(lastname + firstname)
    username_set.add(firstname)
    username_set.add(lastname)

    # Add permutations with first characters
    username_set.add(f"{firstname[0]}.{lastname}")
    username_set.add(f"{firstname}.{lastname[0]}")
    username_set.add(f"{firstname[0]}{lastname}")
    username_set.add(f"{firstname}{lastname[0]}")
    username_set.add(f"{lastname[0]}.{firstname}")
    username_set.add(f"{lastname}.{firstname[0]}")
    username_set.add(f"{lastname[0]}{firstname}")
    username_set.add(f"{lastname}{firstname[0]}")
    
    return username_set

def print_usernames(usernames, domain=None):
    if domain:
        for username in usernames:
            print(f"{username}@{domain}")
    else:
        for username in usernames:
            print(username)
            
def username_gen(firstname, lastname, domain=None):
    usernames = generate_usernames(firstname, lastname)
    print_usernames(usernames, domain)
    return list(usernames)

def name_list(filename):
    try:
        with open(filename, 'r') as file:
            return [name.lower() for name in file.read().splitlines()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

def main():
    parser = argparse.ArgumentParser(description='Generate Emails and Usernames from Provided Lists of Names or a Single Name')
    parser.add_argument('--list', '-l', type=str, help='File containing a list of names.')
    parser.add_argument('--name', '-n', type=str, help='Single name to generate usernames and emails.')
    parser.add_argument('--domain', '-d', type=str, help='Email domain for generating email-format usernames.')

    args = parser.parse_args()

    if args.list:
        names = name_list(args.list)
    elif args.name:
        names = [args.name.lower()]
    else:
        parser.error('No action requested, add --list or --name')

    if names:
        for name in names:
            name_parts = name.split()
            if len(name_parts) >= 2:
                firstname, lastname = name_parts[0], name_parts[-1]
                username_gen(firstname.lower(), lastname.lower(), args.domain)
            elif len(name_parts) == 1:
                if args.domain:
                    print(f"{name.lower()}@{args.domain}")
                else:
                    print(name.lower())
            else:
                print(f"Invalid format for name: {name}.")
            
if __name__ == "__main__":
    banner()
    main()
