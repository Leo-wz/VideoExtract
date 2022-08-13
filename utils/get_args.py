
from distutils.log import error

list_of_args = [['-c:v', 'copy', '-an'],
                ['-c', 'copy'],
                ['-vn', '-c:a', 'copy']]
def get_args():
    choice = input('Choose action:\n\
                    1. Video stream only\n\
                    2. Video and audio\n\
                    3. Audio only\n\
                    Your selection: ')
    try: 
        choice = int(choice)
        if choice > len(list_of_args): raise error # Not in the list of args
    except: 
        print('Invalid selection, exiting now')
        quit()
    return list_of_args[choice-1]
