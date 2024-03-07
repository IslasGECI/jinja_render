import os


def get_hash_from_branch(branch):
    os.system("git config --global --add safe.directory /workdir")
    stream = os.popen(f"git rev-parse {branch}")
    output = stream.read()
    return output.split("\n")[0]


def get_hash_from_develop():
    return get_hash_from_branch("develop")


def get_repo_name():
    os.system("git config --global --add safe.directory /workdir")
    stream = os.popen("basename $(git remote get-url origin)")
    output = stream.read()
    return output.split(".")[0].strip("\n")


def get_repo_and_hash(branch="develop"):
    hash = get_hash_from_branch(branch=branch)
    name = get_repo_name()
    return {"repo": name, "hash": hash}
