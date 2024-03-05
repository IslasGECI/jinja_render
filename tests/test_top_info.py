from jinja_render import get_repo_and_hash, get_hash_from_branch

hash_repo = "be0a1f7b95249cbce2d224d9f09fe52fbad8d8fe"


def test_get_repo_and_hash():
    expected = {"repo": "jinja_render", "hash": hash_repo}
    obtained = get_repo_and_hash(branch="for_testing")
    assert expected == obtained


def test_get_hash_from_develop():
    expected = hash_repo
    obtained = get_hash_from_branch(branch="for_testing")
    assert expected == obtained
