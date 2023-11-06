import argparse

from boilerplate.export import export_github_data, load_files

if __name__ == "__main__":
    # create a parser for commandline arguments
    parser = argparse.ArgumentParser(
        prog="GitHub data exporter",
        description="Exports issue and project data from GitHub",
    )
    parser.add_argument("--owner")
    parser.add_argument("--repo")
    parser.add_argument("--project")
    args = parser.parse_args()
    for arg in ["owner", "repo", "project"]:
        if not getattr(args, arg):
            print(f"{arg} not passed")
    # export the data using the command line arguments
    export_github_data(
        owner=args.owner,
        repo=args.repo,
        project=args.project,
    )
    load_files()
