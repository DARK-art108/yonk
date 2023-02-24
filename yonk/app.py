from yonk import createcli
import argparse

def main():
    parser = argparse.ArgumentParser(description='Create a new project')
    parser.add_argument('create', help='Create a new project')
    parser.add_argument('--name', type=str, required=True)
    args = parser.parse_args()
    if 'create' in args:
        createcli.gen_structure(args.name)
    else:
        print('Check the help menu with --help.')

if __name__ == '__main__':
    main()





