# -------
# IMPORTS
# -------
import random

# ---------
# VARIABLES
# ---------
passwords = {}
running = True


def create_password(long: "type in the length for the password" = 10):
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
              "abcdefghijklmnopqrstuvwxyz" \
              "0123456789" \
              "^°!§$%&/()=?`´+*#'-_.:,;<>"
    password = "".join(random.choice(symbols) for _ in range(long))
    return password


def save_pass(dic, site: str, password: str, username: str):
    dic[site] = [username, password]


def remove_pass(dic, name):
    dic.pop(name)


if __name__ == '__main__':
    # just for console
    while running:
        start = input("Wanna create a password or see your passwords? (C/S): ")
        if start in ["c", "C"]:
            length = int(input("Length: "))
            password = create_password(length)
            print(f"Your password is: {password}")
            add_to_dic = input("Wanna add password to dic? (Y/N): ")
            if add_to_dic == "Y" or add_to_dic == "y":
                website = input("For what is the password (e.g. website): ")
                save_pass(passwords, website, password, "adwa")
                # shows the passwords separated (not in list)
                for name in passwords:
                    print(f"{name}: {passwords[name][0]}; Password: {passwords[name][1]}")

        elif start in ["s", "S"]:
            for name in passwords:
                print(f"{name}: {passwords[name]}")

        if input("Add another password (Y/N): ") in ["N", "n"]:
            running = False
