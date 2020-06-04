class bcolors:
	DARKPURPLE = "\033[1;35m"
	DARKGREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	ENDC = "\033[1;m"


def print_info(message):
    print((bcolors.RED) + ("[*] ") + (bcolors.YELLOW) + (str(message)))

def print_shell(message):
    print((bcolors.DARKGREEN) + ("[*] ") + (bcolors.RED) + (str(message)) + (bcolors.ENDC))

def print_error(message):
    print((bcolors.DARKGREEN) + ("[*] ") + (bcolors.RED) + (str(message)) + (bcolors.ENDC))

