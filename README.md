# Password List Maker

A simple Python script that generates a password list based on user input.

Requirements
------------

* Python 3.x
* `colorama` library
* `termcolor` library
* `pyfiglet` library

Installation
------------

1. Install the required libraries using pip:
   
   ```
   pip install colorama termcolor pyfiglet
   ```

2. Save the script to a file with a `.py` extension, such as `password_list_maker.py`.

Usage
-----

Run the script using the following command:

```
python password_list_maker.py
```

The script will print a banner and ask for user input for various personal information fields, such as name, surname, age, birthday, phone number, nickname, pet name, favorite color, favorite artist, and favorite sport. The user can also manually add other words to the list.

The script will then generate all possible permutations of the words in the list and save them to a text file. The user will be prompted to enter a file name to save the password list.
