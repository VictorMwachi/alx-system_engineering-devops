#echo"Hello world"-----prints hello world in the terminal
#echo \"\(Ôo\)\'----------prints smilley inthe terminal by escaping the characters that will prompt error by use of backslash
#cat /etc/passwd ---------display contents of passwd file which is in etc folder
#cat /etc/passwd /etc/hosts -----displays contents of  hosts and passwd
#tail /etc/passwd --------displays the last 10 lines of /etc/passwd
#head /etec/passwd ---------displays the first 10 lines of /etc/passwd
#head -n 3 iacta|tail -n 1 -------displayss the third line of the file
#echo "Best School" | cat > '\*\\'\''"Best School"\'\''\\*$\?\*\*\*\*\*:)' ----------creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.
#ls -la > ls_cwd_content---------script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
#tail -n 1 iacta >> iacta ----duplicates the last line of iacta file
# find . -name "*.js" -type f -delete ---------deltes all files with .js extension in current directory and sub directories
#find . -type d | wc -l ------- counts the number of directories and sub-directories in the current directory.
	    The current and parent directories should not be taken into account, Hidden directories should be counted
#ls -t | head ----------displays the 10 newest files in the current directory.
	    One file per line,  Sorted from the newest to the oldest
# sort| unique -u -----------takes a list of words as input and prints only words that appear exactly once. Input format: One line, one word Output format: One line, one word;  Words should be sorted
#grep root /etc/passwd --------prints line that contains "root" in it
#grep bin /etc/passwd |wc -l -------displays the number of lines that contain bin
#grep -A 3 "root" /etc/passwd-------Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd
#grep -v bin /etc/passwd-------Display all the lines in the file /etc/passwd that do not contain the pattern “bin”
#grep ^[[:alpha:]] /etc/ssh/sshd_config-----Display all lines of the file /etc/ssh/sshd_config starting with a letter.; include capital letters as well
#tr 'AC' 'Ze' ------Replace all characters A and c from input to Z and e respectively.
#tr -d "cC"  --------removes all letters c and C from input.
#rev ---------reverses input
#cut -d":" --fields=1,6 /etc/passwd | sort--------displays all users and their home directories, sorted by users. Based on the the /etc/passwd file
#find . -empty -printf "%f\n" --------finds all empty files and directories in the current directory and all sub-directories.

    Only the names of the files and directories should be displayed (not the entire path)
    Hidden files should be listed
    One file name per line
   The listing should end with a new line
#find . -type f -name "*.gif" -printf "%f\n"| rev | cut -d '.' -f2- | rev | LC_ALL=C sort -f    -----------Hidden files should be listed
Only regular files (not directories) should be listed
The names of the files should be displayed without their extensions
The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)
One file name per line
The listing should end with a new line
