"""Command-line interface for NHS RAP Cookiecutter Template."""

import sys
from pathlib import Path

import click
from cookiecutter.main import cookiecutter


@click.command()
@click.option(
    "-c",
    "--checkout",
    default=None,
    help="Branch, tag, or commit to checkout after git clone",
)
@click.option(
    "--no-input",
    is_flag=True,
    help="Do not prompt for parameters and only use cookiecutter.json defaults",
)
@click.option(
    "--config-file",
    type=click.Path(exists=True),
    help="User configuration file",
)
@click.option(
    "-o",
    "--output-dir",
    default=".",
    type=click.Path(),
    help="Where to output the generated project dir",
)
def main(checkout, no_input, config_file, output_dir):
    """Generate a new NHS RAP project from the cookiecutter template."""
    # Get the template directory (parent of this package)
    template_dir = Path(__file__).parent.parent

    try:
        cookiecutter(
            str(template_dir),
            checkout=checkout,
            no_input=no_input,
            extra_context=None,
            replay=False,
            overwrite_if_exists=False,
            output_dir=output_dir,
            config_file=config_file,
        )
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
