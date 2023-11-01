import os
import argparse

class RecursiveWalk:
    def __init__(self):
        self.path = ''
        self.recursive_walk_list = []

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description='Scan files in a directory')
        parser.add_argument('-p', '--path', metavar='path', type=str, help='Path to directory')
        parser.add_argument('-r', '--recursive', action='store_true', help='Enable recursive scanning')
        return parser.parse_args()

    def scan_path(self):
        for root, dirs, files in os.walk(self.path):
            for entry in files:
                full_path = os.path.join(root, entry)
                self.recursive_walk_list.append(full_path)

    def main(self):
        args = self.get_args()
        self.path = args.path
        recursive = args.recursive  # Check if the -r flag is set

        if recursive:
            # Use RecursiveWalk for recursive scanning
            self.scan_path()
            print(self.recursive_walk_list)
            

class DirectoryWalk:
    def __init__(self):
        self.path = ''
        self.directories = []

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description='Scan files in a directory')
        parser.add_argument('-p', '--path', metavar='path', type=str, help='Path to directory')
        parser.add_argument('-r', '--recursive', action='store_true', help='Enable recursive scanning')
        return parser.parse_args()


    def scan_path(self):
        with os.scandir(self.path) as iter_path:
            for entry in iter_path:
                self.directories.append(entry)

    def main(self):
        args = self.get_args()
        self.path = args.path
        recursive = args.recursive  # Check if the -r flag is set
        
        if not recursive:
            self.scan_path()
            print(self.directories)


if __name__ == '__main__':
    recursive_directory_walk_instance = DirectoryWalk()
    recursive_directory_walk_instance.main()
    
    walk_instance = RecursiveWalk()
    walk_instance.main()