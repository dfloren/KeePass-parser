#!/usr/bin/python

# Input Format:
# Title: <title>
# Email: <email>
# Username: <username>
# Password: <password>
# URL: <url>
# Comments:
# <comment1>
# <comment2>

# Output Format:
# "Group", "Title", "Email", "Username", "Password", "URL", "Note(s)",
# "Email", "Google", "testmail@gmail.com", , "password123", "https://google.com/", "Note1, Note2",

import sys
from collections import OrderedDict


class Entry:
    def __init__(self):
        self.attr = OrderedDict()
        self.attr['Group'] = ""
        self.attr['Title'] = ""
        self.attr['Email'] = ""
        self.attr['Username'] = ""
        self.attr['Password'] = ""
        self.attr['URL'] = ""
        self.attr['Comments'] = ""


def write_entry(entry, file):
    str_entry = ""
    attr = entry.attr
    attr['Comments'] = attr['Comments'].rstrip(',')
    attr['Comments'] = attr['Comments'].rstrip('\n')

    for key in attr:
        str_entry = str_entry + '"' + attr[key] + '",'
    beg, part, end = str_entry.rpartition(',')
    file.write(beg + end + "\n")


def main(arg):
    extension = str(arg).split('.')[1]
    if extension != "txt":
        print("Error: input is not of type '.txt'")
        print("Input type:", "'." + extension + "'")
        sys.exit()

    is_comment = False

    outfile = open(str(arg).split('.')[0] + "-kp.txt", 'w')

    with open(''.join(arg), 'r') as infile:
        for line in infile:
            if line == "\n":
                is_comment = False
                write_entry(new_entry, outfile)
                continue

            if not is_comment:
                key, val = line.split(':', 1)
                if "title" in key.lower():
                    new_entry = Entry()
                    new_entry.attr["Title"] = val.strip()
                    new_entry.attr["Group"] = str(arg).split('.')[0]
                elif "mail" in key.lower():
                    new_entry.attr["Email"] = val.strip()
                elif "user" in key.lower():
                    new_entry.attr["Username"] = val.strip()
                elif "password" in key.lower():
                    new_entry.attr["Password"] = val.strip()
                elif "url" in key.lower():
                    new_entry.attr["URL"] = val.strip()
                elif "security question" in key.lower() or "comments" in key.lower():
                    is_comment = True
            else:
                new_entry.attr["Comments"] = (new_entry.attr["Comments"] + line.rstrip("\n") + ',')

    write_entry(new_entry, outfile)

    outfile.close()
    infile.close()


if __name__ == "__main__":
    if len(sys.argv) != 2 or '.' not in str(sys.argv[1]):
        print("Usage: python3 parser.py inputfile.txt", end='')
        sys.exit()
    main(sys.argv[1])
