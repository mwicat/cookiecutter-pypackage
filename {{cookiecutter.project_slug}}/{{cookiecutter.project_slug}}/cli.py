# -*- coding: utf-8 -*-

"""Console script for {{cookiecutter.project_slug}}."""

import logging
import sys

import click


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.option('-l', '--loglevel', help='Logging level')
@click.pass_context
def cli(ctx, debug, loglevel):
    ctx.obj['DEBUG'] = debug
    if loglevel is not None:
        loglevel = getattr(logging, loglevel.upper(), None)
    else:
        loglevel = logging.INFO
    logging.basicConfig(level=loglevel)


@cli.command()
@click.pass_context
@click.argument('liveset_path')
@click.option('--dest-dir', '-d',
              help='Destination directory',
              default='./livesetutil_samples')
@click.option('--include-groups/--exclude_groups',
              help='Include or exclude tracks from matching groups',
              default=True)
@click.option('--filter',
              help='Regular expression to filter by')
@click.option('--prefix', '-p',
              help='Prefix to prepend to extracted filenames')
@click.option('--dry-run', '-n',
              help='Do not nothing, just print what it would do',
              is_flag=True)
def subcommand(ctx, liveset_path, dest_dir, include_groups, filter, prefix, dry_run):
    return 0


def main():
    sys.exit(cli(obj={}))


if __name__ == '__main__':
    main()
