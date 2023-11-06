# pylint: disable=invalid-name, unspecified-encoding
import json
from pathlib import Path
import shlex
import subprocess


ISSUE_FILE = "data/issue-data.json"
SPRINT_FILE = "data/sprint-data.json"


def pipe_command_to_file(command: str, output_file: str):
    """Write the output of a sub-process to a file"""
    # Make sure the output file's parent directory exists
    file_path = Path(output_file)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    # Run the command and write the standard output to a file
    with open(output_file, "w") as f:
        subprocess.call(shlex.split(command), stdout=f)


def export_project_data(owner: str, project: int, output_file: str) -> None:
    """Exports and writes GitHub project data to a JSON file"""
    command = (
        f"gh project item-list {project} --format json --owner {owner} -L 1000"
    )
    pipe_command_to_file(command, output_file)


def export_issue_data(owner: str, repo: str, output_file: str) -> None:
    """Exports and writes GitHub issue data to a JSON file"""
    command = (
        "gh issue list --json number,createdAt,closedAt "
        f"-R {owner}/{repo} -L 1000 --state all"
    )
    pipe_command_to_file(command, output_file)


def export_github_data(owner: str, repo: str, project: str):
    """Export issues and project data from GitHub"""
    print("Exporting issue data")
    export_issue_data(
        owner=owner,
        repo=repo,
        output_file=ISSUE_FILE,
    )
    print("Exporting sprint data")
    export_project_data(
        owner=owner,
        project=project,
        output_file=SPRINT_FILE,
    )


def load_files():
    """Checks that the json files can be loaded correctly"""
    with open(ISSUE_FILE, "r") as f:
        issues = json.loads(f.read())
    print(f"Total number of issues: {len(issues)}")
    print("First issue:")
    print(issues[0])
