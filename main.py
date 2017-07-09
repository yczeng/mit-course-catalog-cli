import click

@click.command()
@click.option('--search', default='', help="search for subject with course number")

def cli(course):
	if course:
		click.echo("Searching for course...")