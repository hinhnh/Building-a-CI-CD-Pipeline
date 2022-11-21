from click.testing import CliRunner
from hello import hello

def test_hello():
    runner = CliRunner()
    result = runner.invoke(hello, ["--name", "Thor", "--color", "blue", "--year", "1990"])
    assert "Thor" in result.output