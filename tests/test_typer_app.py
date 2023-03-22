from typer.testing import CliRunner
from jinja_render import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "XXXX" not in result.stdout
