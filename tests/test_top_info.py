from jinja_render import get_repo_and_hash, get_hash_from_branch

import os


def test_get_repo_and_hash():
    hash_repo = "be0a1f7b95249cbce2d224d9f09fe52fbad8d8fe"
    expected = {"repo": "jinja_render", "hash": hash_repo}
    obtained = get_repo_and_hash(branch="for_testing")
    assert expected == obtained

    command = "git clone https://github.com/IslasGECI/dummy_for_testing.git"
    os.system(command)
    current_working_directory = os.getcwd()
    repo = "dummy_for_testing"
    os.chdir(repo)
    hash_repo = "3fa7073ca36dfbf4031fe1350a33869b0ce4574c"
    expected = {"repo": repo, "hash": hash_repo}
    obtained = get_repo_and_hash()
    os.chdir(current_working_directory)
    assert expected == obtained


def test_get_hash_from_branch():
    hash_repo = "be0a1f7b95249cbce2d224d9f09fe52fbad8d8fe"
    expected = hash_repo
    obtained = get_hash_from_branch(branch="for_testing")
    assert expected == obtained
