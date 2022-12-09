import os

import click
import homura_art.utilities as utilities


@click.command()
@click.option(
    "--acccess-key", default=lambda: os.environ.get("ACCCESS_KEY", ""), prompt=True
)
def sync(
    acccess_key,
):
    """Sync hydrus network database with homura-art"""
    utilities.sync(acccess_key)


if __name__ == "__main__":
    sync()
