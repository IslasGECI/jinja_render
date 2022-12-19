import hashlib
import os

from jinja_render import (
    get_rendered_report,
    write_tex,
)


report_name = "paper"
summary_path = "tests/data/results.json"


def test_write_rendered_report():
    tex_path = "reports/paper.tex"
    if os.path.exists(tex_path):
        os.remove(tex_path)
    write_tex(report_name)
    assert os.path.exists(tex_path)


def test_rendered_report():
    expected_hash = "239431b70e3e6f770c21cef4ee6d22ee"
    report_name = "paper"
    obtained_hash = _get_hash_from_tex_file(report_name)
    assert obtained_hash == expected_hash, "El hash del archivo reports/paper.tex"

    expected_hash = "74b0b5fed1926ff3c6f641553d32866f"
    report_name_without_summary = "paper_without_summary"
    obtained_hash = _get_hash_from_tex_file(report_name_without_summary)
    assert obtained_hash == expected_hash, "El hash del archivo reports/paper_without_summary.tex"


def _get_hash_from_tex_file(report_name):
    rendered_report = get_rendered_report(report_name, summary_path)
    report_content = rendered_report.encode("utf-8")
    obtained_hash = hashlib.md5(report_content).hexdigest()
    return obtained_hash
