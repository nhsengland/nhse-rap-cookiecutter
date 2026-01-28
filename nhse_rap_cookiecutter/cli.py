"""Command-line interface for NHS RAP Cookiecutter Template."""

import sys

import click
from cookiecutter.main import cookiecutter

# GitHub repository URL for the template
TEMPLATE_REPO = "gh:nhsengland/nhse-rap-cookiecutter"


@click.command()
@click.argument("template", default=TEMPLATE_REPO)
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
@click.option(
    "--debug",
    is_flag=True,
    help="Show full traceback on error",
)
def main(template, checkout, no_input, config_file, output_dir, debug):
    """Generate a new NHS RAP project from the cookiecutter template.

    TEMPLATE is the path or URL to the template. Defaults to the NHS RAP
    cookiecutter template from GitHub.
    """
    try:
        cookiecutter(
            template,
            checkout=checkout,
            no_input=no_input,
            extra_context=None,
            replay=False,
            overwrite_if_exists=False,
            output_dir=output_dir,
            config_file=config_file,
        )
    except Exception as e:
        import traceback

        click.echo(f"Error: {e}", err=True)
        if debug:
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
