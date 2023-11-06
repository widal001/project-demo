import json
import shlex
import subprocess


ISSUE_FILE = "data/issue-data.json"
SPRINT_FILE = "data/sprint-data.json"


def pipe_command_to_file(command: str, output_file: str):
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
    command = f"gh issue list --json number,createdAt,closedAt -R {owner}/{repo} -L 1000 --state all"
    pipe_command_to_file(command, output_file)


def export_github_data(owner: str, repo: str, project: str):
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
    with open(ISSUE_FILE) as f:
        issues = json.loads(f.read())
    print(f"Total number of issues: {len(issues)}")
    print("First issue:")
    print(issues[0])
