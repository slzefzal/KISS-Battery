

import os
import shutil


def main():
    root_path = r"C:\Users\PETA-Anwender\KISS Bat"
    extension = ".json"
    for path, _, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.endswith(extension):
                source = os.path.join(path, filename)
                target = source[:-len(extension)]
                os.mkdir(target)
                #shutil.move(source, target)


if __name__ == '__main__':
	main()