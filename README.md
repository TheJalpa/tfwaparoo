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

#Example Usage

python tfswap.py --version 12.1 --os windows

#Example tree
D:/terraform/terraform11.14.exe
D:/terraform/terraform13.5.exe
D:/terraform/terraform15.2.exe

Once you have updated your source folder to the directory containing your terraform versions named appropriately as above, you can then simply use the above command line.
Terraform will then replace the existing version of terraform.exe with the version you've chosen, leaving the others intact.