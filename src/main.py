from generatepage import *

def main():
    copy_static()
    print(extract_title("# Hello\n# World"))

if __name__ == "__main__":
    main()