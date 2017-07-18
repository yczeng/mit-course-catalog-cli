import click
import script as s

@click.command()
@click.option('--menu', is_flag=True, help="Displays list of courses.")
@click.option('--search', default='', help="Search by subject number or name.")

def cli(menu, search):
	if menu:
		click.echo(s.getMenu())
	if search:
		click.echo(s.getSubject(format(search)))