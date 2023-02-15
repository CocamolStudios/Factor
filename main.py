from os import path
import art
from colorama import Fore

art.tprint("Factor")
print(Fore.RED+"Factor is a Console-based Text Editor for python.")
print(Fore.RESET+"")

def inputs():
    while True:
        a = input(Fore.GREEN+"~")
        if a == "Editor":
            file_path = input("\nCreate file (please enter the path to file): ")

            if path.exists(file_path):
                print("\n\tFile already exists!")
                ans = input("\nDo you want to use this file? (y/n)\n-> ")

                if ans == 'y' or ans == 'Y':
                    file = open(file_path, "a")
                    ans = input("\nDo you want to erase all content? (y/n)\n-> ")

                    if ans == 'y' or ans == 'Y':
                        print("\n\tErasing...\n")
                        file.seek(0)
                        file.truncate()

                    else:
                        pass

                else:
                    exit()

            else:
                print("\n\tCreating new file...\n")
                file = open(file_path, "a")

            print("\nPress RETURN to start a new line.\nPress Ctrl + C to save and close.\n\n")

            line_count = 1

            while line_count > 0:
                try:
                    line = input("\t" + str(line_count) + " ")
                    file.write(line)
                    file.write('\n')
                    line_count += 1
                except KeyboardInterrupt:
                    print("\n\n\tClosing...")
                    break

            file.close()

