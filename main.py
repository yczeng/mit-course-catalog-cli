import click
import script as s

@click.command()
@click.option('--menu', is_flag=True, help="displays list of courses")
@click.option('--subject', default='', help="get subject by course number")

def cli(menu, subject):
	if menu:
		click.echo(s.getMenu())
	if subject:
		click.echo(s.getSubject(format(subject)))