import itertools
import colorama
import pyfiglet
import termcolor

listOfWords = []

# Banner and info about the program
def banner():
    print("\n\n")
    termcolor.cprint(pyfiglet.figlet_format("Password List Maker", font="slant"), "light_magenta")
    print(colorama.Fore.CYAN + "\nPassword List Maker v1.0\n")
    print(colorama.Fore.CYAN + "This program will create a password list for you. By entering the information of the target, all the possible permutations of passwords will be generated.\n")
    termcolor.cprint("This program is for educational purposes only. Don't use it for illegal activities. I don't accept responsibility for any illegal usage.\n", "red", attrs=["bold"])
    print(colorama.Fore.YELLOW + "Enter n/N or press enter to skip a word.\n")

# Input handling and adding the words to the list
def inputHandling(word):
    if word != 'n' and word != 'N' and word != '':
        while True:
            try:
                howMany = int(input(termcolor.colored("How many times do you want it to repeat? (1 for no repeat): ", "light_blue")))
                break
            except:
                print(colorama.Fore.RED + "Please enter a number!")
        for i in range(howMany):
            listOfWords.append(word)

banner()

# Getting the information of the target from the user
name = input(colorama.Fore.WHITE + "Name: ")
inputHandling(name)

surname = input(colorama.Fore.WHITE + "\nSurname: ")
inputHandling(surname)

age = input(colorama.Fore.WHITE + "\nAge: ")
inputHandling(age)

birthYear = input(colorama.Fore.WHITE + "\nBirthday Year: ")
inputHandling(birthYear)

birthMonth = input(colorama.Fore.WHITE + "\nBirthday Month: ")
inputHandling(birthMonth)

birthDay = input(colorama.Fore.WHITE + "\nBirthday Day: ")
inputHandling(birthDay)

phone = input(colorama.Fore.WHITE + "\nPhone Number: ")
inputHandling(phone)

nickname = input(colorama.Fore.WHITE + "\nNickname: ")
inputHandling(nickname)

petName = input(colorama.Fore.WHITE + "\nPet Name: ")
inputHandling(petName)

favColor = input(colorama.Fore.WHITE + "\nFavorite Color: ")
inputHandling(favColor)

favArtist = input(colorama.Fore.WHITE + "\nFavorite Artist: ")
inputHandling(favArtist)

favSport = input(colorama.Fore.WHITE + "\nFavorite Sport: ")
inputHandling(favSport)

print(colorama.Fore.YELLOW + "\nNow enter the words that you want to add to the list. They can be any word or character. @, #, $, %, &, *, !, ?, etc.\nYou can also enter the words that you think the target might use in their password; Such as leet versions of the words, etc.\n")

# Adding other words to the list
while(True):
    word = input(colorama.Fore.WHITE + "\nAdd other words (n/N or press enter to skip) : ")
    if(word == 'n' or word == 'N' or word == ''):
        break
    else:
        inputHandling(word)

# Creating the password list and saving it to a file
fileName = input(colorama.Fore.BLUE + "\nEnter the file name to save the password list in: ")

file = open(fileName+".txt", "w")

counter = 0

for i in range(len(listOfWords)):
    passwordList = list(itertools.permutations(listOfWords, i+1))
    for j in passwordList:
        file.write("".join(list(j)) + "\n")
        counter += 1

file.close()

# Printing the number of passwords and the file name
print(colorama.Fore.GREEN + "\nPassword list saved in " + fileName + ".txt successfully!\n")

print(colorama.Fore.GREEN + "Number of passwords: " + str(counter) + "\n")