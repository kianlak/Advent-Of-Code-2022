# Class designed to act as a File/Directory:
# A file will have a name and a size greater 
# than 0 assigned to it initially based on the 
# command inputs, however a file will not be able 
# to access children since it won't be able to 
# hold one. A directory will be assigned a name, 
# however should not have a size assigned at first, 
# but will have children and a parent assigned. 
 
class File:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.parent = None
        self.children = []

# This will return the total size of the directory being deleted to free up necessary space

def part2():
    outermost_directory = File('/')         # Outermost directory will be the root directory path
    current_directory = outermost_directory # Will be used to keep track of what file path we are currently on
    
    with open('commands.txt') as file:
        for line in file.readlines():
            # A command has been read in
            if line.startswith('$'):
                command = line.split()

                if (command[1] == "cd") and (command[2] == ".."):   # Go to parent directory
                    current_directory = current_directory.parent
                elif command[1] != "ls":                            # Go into a child directory
                    new_file = File(command[2])                 # Create new directory
                    new_file.parent = current_directory         # Set parent of new directory
                    current_directory.children.append(new_file) # Add new directory to child of current directory
                    current_directory = new_file                # Go into child directory
            # Line initializes a file within the directory or unecessary information
            else:
                size, file_name = line.split()
                
                # Makes sure file initialization is being done
                if size.isdigit():
                    new_file = File(file_name, int(size))       # Create new file with necessary info assigned
                    current_directory.children.append(new_file) # Add file to children of current directory
    
    # This will hold a dictionary of the files sizes
    DIR_SIZES = {}
    
    # Returns the size of a directory
    def directory_size(file):
        
        # Reads a file
        if not file.children:
            return file.size
        
        total_size = 0                          # Reading a new directories size
        for child in file.children:             # Go through directories children
            total_size += directory_size(child) # Add size of all children

        DIR_SIZES[file] = total_size    # Size of a directory assigned to dictionary
        return total_size

    USED_SPACE = directory_size(outermost_directory)    # Holds total amount of used space
    UNUSED_SPACE = 70000000 - USED_SPACE

    # Accounts for total, and sums all the sizes for necessary requirements
    for size in sorted(DIR_SIZES.values()):
        if UNUSED_SPACE + size >= 30000000:
            print("The total size of the directory being deleted to free up necessary space is: " + str(size))
            break