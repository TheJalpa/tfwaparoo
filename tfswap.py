import argparse
import system

#Pass the version you want of terraform
#Make sure it exists in the src directory as terraform and then the version
#example: terraform12.5
parser = argparse.ArgumentParser()
parser.add_argument("--version", required=True, type=str)
parser.add_argument("--osystem", required=True, type=str)
args = parser.parse_args()
version = args.version
osystem = args.osystem

#this is your terraform source directory:
tfsource = "/home/somethinghere"

if osystem == 'windows':
    os.system('del ' + tfsource + '\\terraform')
    os.system('copy src\\terraform' + version + ' ' + tfsource + '\\terraform')
elif osystem == 'linux':
    os.system('rm ' + tfsource + '/terraform && cp src/terraform' + version + ' ' + tfsource + '/terraform')
else:
    print ('No valid operating system type supported was entered')
    print ('Currently supported is windows and linux')
