# KeePass-parser
I whipped up this little script to convert my password text files (don't ask why) into a format that KeePass can use via their Generic CSV Importer feature.

### Usage
`python3 parser.py inputfile.txt`

### Input format example
This was the format of my password text files. Key-value pairs are separated by a colon.  
  
Title: GitHub  
Email: sample@gmail.com  
Username: user1  
Password: Uk%Wzk8;==^.D5mo  
URL: https://github.com/  

Title: Scotiabank  
Email: sample@gmail.com  
Password: Uk%Wzk8;==^.D5mo  
URL: https://scotiabank.com/  
Comments:  
comment1  
comment2  
Security Questions:  
What is your favorite color? Purple  

**Important:** Comments and Security Questions must come after the URL field. The field *Comments* and *Security Questions* must have their values strictly below them, even if there is only one value.  

### Output format example
The output is stored in a text file with the same name as the input except it has '-kp' appended to it. The input file is called 'test.txt' in the example below.  
  
"test","GitHub","sample@gmail.com","user1","Uk%Wzk8;==^.D5mo","https://github.com/",""  
"test","Scotiabank","sample@gmail.com","","Uk%Wzk8;==^.D5mo","https://scotiabank.com/","comment1,comment2,Security Questions:,What is your favorite color? Purple"  

### Password Limitations  
Because KeePass uses certain characters for parsing when importing from a generic text file, I lazily decided that some characters cannot be used in value entries. These are:  
\ - backslash  (include this if you're not using it as an escape character)  
" - double quotation mark (used as text qualifier)  
  
These constraints obviously reduce password strength but as long as you're generating a lengthy password (16 to 18 characters), and you're not protecting nuke launch codes I think it's enough.
### Importing to KeePass  
The column ordering in the KeePass table is as follows:  
"Group", "Title", "Email", "Username", "Password", "URL", "Note(s)"  
where "Note(s)" can be either Comments or Security Questions or both.
#### Groups
The script uses the file name to create a group for each KeePass entry. For example, the file *games.txt* will have its entries put under a group called *games*.  
#### Email field
Since KeePass doesn't have an Email field, a custom string field should be created and named Email. You will have to add this column manually in the KeePass table to view its value.