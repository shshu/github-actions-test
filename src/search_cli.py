import click
from pathlib import Path


@click.command()
@click.option(
    "--path",
    prompt="Path to search for files",
    type=click.Path(),
    help="This is the path to search for files: /tmp",
)
@click.option(
    "--ftype",
    prompt="Please enter the file type",
    help="file type: txt",
)
def search_files(path: str, ftype: str):
    """
    This is command line tool to search files with spesific extention
    """

    path = Path(path).expanduser()

    # Check if path is valid directory
    assert path.is_dir(), "Invalid path should be valid directory"

    results = path.glob(f"**/*.{ftype}")
    click.echo(
        click.style(f"Searching file in {path} with extention {ftype}", fg="yellow")
    )

    for result in results:
        click.echo(click.style(f"{result}", bg="black", fg="green"))


if __name__ == "__main__":
    search_files()  # pylint: disable=no-value-for-parameter
