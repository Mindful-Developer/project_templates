import pathlib
import argparse


def create_project_directory(args: argparse.Namespace) -> None:
    if args.folder:
        folder = pathlib.Path(args.folder)
    else:
        folder = pathlib.Path.home() / 'projects'

    if not folder.exists():
        folder.mkdir()

    project_dir = folder / args.name
    if project_dir.exists():
        print(f'Project {args.name} already exists')
        raise Exception('Project already exists')

    project_dir.mkdir()


def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--private', action='store_true', help='create private github repository')
    parser.add_argument('-f', '--folder', help='your projects folder(defaults to ~/projects)')
    parser.add_argument('-n', '--no-init', action='store_true', help='avoid initializing package')
    parser.add_argument('name', help='name of the project')
    args = parser.parse_args()

    # create project directory
    create_project_directory(args)


if __name__ == '__main__':
    main()
