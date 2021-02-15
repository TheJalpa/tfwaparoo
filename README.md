# tfwaparoo
swap terraform versions with python

# Usage
command to execute:
tfswap.py --version x.xx --osystem windows/linux

Example:
tfswap.py --version 12.29 --osystem linux

This would utilize your source directory you have entered, copy the terraform12.29 you have in there, and then copy it to 
your source directory as "terraform" - note, this deletes the current version of "terraform" so be sure you have all versions
you are working with present in the /src directory of this project.