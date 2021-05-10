from shutil import copyfile

# Load Backup

# Declare Paths [options.txt]
source = r'C:\Users\skyca\Documents\Python Code\Minecraft Options Loader\data\1.16\options.txt'
target = r'C:\Users\skyca\AppData\Roaming\.minecraft\options.txt'

# Try To Copy
try:
    copyfile(source, target)
    print("\nFile copy successful!\n")
except IOError as e:
    print("Unable to copy file. %s" % e)
except:
    print("Unexpected error:", sys.exc_info())


# Declare Paths [optionsof.txt]
source = r'C:\Users\skyca\Documents\Python Code\Minecraft Options Loader\data\1.16\optionsof.txt'
target = r'C:\Users\skyca\AppData\Roaming\.minecraft\optionsof.txt'

# Try To Copy
try:
    copyfile(source, target)
    print("\nFile copy successful!\n")
except IOError as e:
    print("Unable to copy file. %s" % e)
except:
    print("Unexpected error:", sys.exc_info())


# Declare Paths [optionsLC.txt]
source = r'C:\Users\skyca\Documents\Python Code\Minecraft Options Loader\data\1.16\optionsLC.txt'
target = r'C:\Users\skyca\AppData\Roaming\.minecraft\optionsLC.txt'

# Try To Copy
try:
    copyfile(source, target)
    print("\nFile copy successful!\n")
except IOError as e:
    print("Unable to copy file. %s" % e)
except:
    print("Unexpected error:", sys.exc_info())


print("\nFile copy attempt done!\n")
