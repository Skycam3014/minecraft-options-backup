from shutil import copyfile
from shutil import rmtree

# Create New Backup

# Declare Paths [options.txt]
source = r'C:\Users\skyca\AppData\Roaming\.minecraft\options.txt'
target = r'C:\Users\skyca\Documents\Python Code\Minecraft Options Loader\data\1.8.9\options.txt'

# Try To Copy
try:
    copyfile(source, target)
    print("\nFile copy successful!\n")
except IOError as e:
    print("Unable to copy file. %s" % e)
except:
    print("Unexpected error:", sys.exc_info())


# Declare Paths [optionsof.txt]
source = r'C:\Users\skyca\AppData\Roaming\.minecraft\optionsof.txt'
target = r'C:\Users\skyca\Documents\Python Code\Minecraft Options Loader\data\1.8.9\optionsof.txt'

# Try To Copy
try:
    copyfile(source, target)
    print("\nFile copy successful!\n")
except IOError as e:
    print("Unable to copy file. %s" % e)
except:
    print("Unexpected error:", sys.exc_info())


# Declare Paths [optionsLC.txt]
source = r'C:\Users\skyca\AppData\Roaming\.minecraft\optionsLC.txt'
target = r'C:\Users\skyca\Documents\Python Code\Minecraft Options Loader\data\1.8.9\optionsLC.txt'

# Try To Copy
try:
    copyfile(source, target)
    print("\nFile copy successful!\n")
except IOError as e:
    print("Unable to copy file. %s" % e)
except:
    print("Unexpected error:", sys.exc_info())


print("\nFile copy attempt done!\n")
