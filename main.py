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
        return parser.parse_args()

    def scan_path(self):
        for root, dirs, files in os.walk(self.path):
            for entry in files:
                self.recursive_walk_list.append(os.path.join(root, entry))

    def main(self):
        args = self.get_args()
        self.path = args.path
        self.scan_path()
        print(self.recursive_walk_list)

class DirectoryWalk:
    def __init__(self):
        self.path = ''

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description='Scan files in a directory')
        parser.add_argument('-p', '--path', metavar='path', type=str, help='Path to directory')
        return parser.parse_args()

    def scan_path(self):
        with os.scandir(self.path) as iter_path:
            for entry in iter_path:
                print(entry.name)

    def main(self):
        args = self.get_args()
        self.path = args.path
        self.scan_path()

if __name__ == '__main__':
    walk_instance = RecursiveWalk()
    walk_instance.main()
    
    # recursive_directory_walk_instance = DirectoryWalk()
    # recursive_directory_walk_instance.main()