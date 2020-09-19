from kata import *
import click


@click.group()
@click.option('--debug/--no-debug', default=False, help='Enable/Disable debug-mode.')
@click.pass_context
def cli(ctx, debug):
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug


@cli.command()
@click.pass_context
@click.option('-a', '--all', default=False, is_flag=True,
              help='Full sync with generating projects and tests without rewriting.')
@click.option('-p', '--project-files', default=False, is_flag=True, help='Generate project files.')
@click.option('-r', '--readme', default=False, is_flag=True, help='Generate readme.')
@click.option('-t', '--tests', default=False, is_flag=True, help='Generate project tests.')
@click.argument('sync', nargs=-1, type=str)
def sync(ctx, all, project_files, readme, tests, sync):
    """ Sync kata state from codewars to repo. """
    click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))
    if all:
        sync_kata()
        generate_readme(KATA_DATA)
        generate_project_files()
    else:
        sync_kata(set(sync))


if __name__ == '__main__':
    cli(obj={})

