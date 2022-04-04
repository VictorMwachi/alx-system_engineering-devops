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

