class FileSystem:
    def __init__(self, name_='/', size_=0, parent_=None):
        self.name = name_
        self.files = []
        self.size = size_
        self.parent = parent_

    def add_dir(self, name):
        self.files.append(FileSystem(name, parent_=self))

    def add_dir(self, dir_):
        self.files.append(dir_)

    def add_file(self, name, size=0):
        file = FileSystem(name, int(size), self)
        self.files.append(file)

    def __len__(self):
        return len(self.files)

    def get_total_size(self):
        tot = self.size
        for d in self.files:
            tot += d.get_total_size()
        return tot

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def get_dirs(self):
        return [f for f in self.files if f.get_size() == 0]

    def get_files(self):
        return [f for f in self.files if f.get_size() != 0]


def parse_dir(commands,parent, line=0):
    dirs = parent.get_dirs()
    files = parent.get_files()
    while line < len(commands)-1:
        # print(f"dirs = {dirs}")
        # print(f"files = {files}")

        command = commands[line].replace("\n", "")

        #print(command)
        while (line < len(commands)-1) and (not commands[line].startswith("$ cd")):
            if command.startswith("dir"):
                cmd = command.split(" ")
                # print(cmd)
                dirs.append(FileSystem(name_=cmd[1], parent_=parent))
            elif not command.startswith("$"):
                files.append(command)
            if line >= len(commands)-1:
                break
            line += 1
            command = commands[line].replace("\n", "")

        if ".." in command:
            for file in files:
                file = file.split(" ")
                parent.add_file(file[1], file[0])
            for dir_ in dirs:
                parent.add_dir(dir_)
            line += 1
            # print(f"<--- returning from {parent.get_name()}")
            return parent, line

        elif command.startswith("$ cd"):
            l = command.split(" ")
            # print(l)
            for d in range(len(dirs)):
                name = l[2].replace("\n","")

                # print(dirs[d].get_name())
                if dirs[d].get_name() == name:
                    # print(f"\n\ndoing $cd {dirs[d].get_name()}\n")
                    (dirs[d], line) = parse_dir(commands, dirs[d], line+2)
                    #print(dirs[d])
                    parent.add_dir(dirs[d])
                    # print(f"Returned from {name}")

        elif command.startswith("$ ls"):
            line += 1

    #print("returning")
    if line == len(commands)-1:
        files.append(commands[line].replace("\n", ""))
    for file in files:
        file = file.split(" ")
        parent.add_file(file[1], file[0])
    for dir_ in dirs:
        parent.add_dir(dir_)

    return parent, line


# Find all directories in FileSystem fs with size of at most "limit"
def find_small_directories(filesystem, limit, small_dirs, found_dirs):
    if filesystem.get_total_size() <= limit and filesystem.get_size() == 0:
        if filesystem not in found_dirs:
            print(filesystem.get_name())
            small_dirs.append(filesystem.get_total_size())
            found_dirs.append(filesystem)
    else:
        for file in filesystem.files:
            find_small_directories(file, limit, small_dirs, found_dirs)

    return small_dirs


def main():
    filename = "input.txt"
    file = open(filename, "r").readlines()
    fs = FileSystem()
    parse_dir(file[2:], fs)

    found_dirs = []
    small_dirs = []
    print(sum(find_small_directories(fs, 100000, small_dirs, found_dirs)))





if __name__ == "__main__":
    main()