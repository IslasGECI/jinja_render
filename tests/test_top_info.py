from jinja_render import get_repo_and_hash, get_hash_from_branch

hash_repo = "31c31a791e017550f11986d5a766ddef8803fbd1"


def test_get_repo_and_hash():
    expected = {"repo": "gatos_guadalupe", "hash": hash_repo}
    obtained = get_repo_and_hash(branch="for_testing")
    assert expected == obtained


def test_get_hash_from_develop():
    expected = hash_repo
    obtained = get_hash_from_branch(branch="for_testing")
    assert expected == obtained