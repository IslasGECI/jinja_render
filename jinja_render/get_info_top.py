import os


def get_hash_from_branch(branch):
    command = "git config --global --add safe.directory /workdir"
    run_command(command)
    stream = os.popen(f"git rev-parse {branch}")
    output = stream.read()
    return output.split("\n")[0]


def run_command(command):
    exit_code = os.system(command)
    assert exit_code == 0



def get_repo_name():
    command = "git config --global --add safe.directory /workdir"
    run_command(command)
    stream = os.popen("basename $(git remote get-url origin)")
    output = stream.read()
    return output.split(".")[0].strip("\n")


def get_repo_and_hash(branch="develop"):
    hash = get_hash_from_branch(branch=branch)
    name = get_repo_name()
    return {"repo": name, "hash": hash}
