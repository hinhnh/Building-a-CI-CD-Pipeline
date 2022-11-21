import click

@click.command(help="This is just a hello app. It does nothing.")
@click.option("--name", prompt="I need your name", help="Need name")
@click.option("--color", prompt="I need your color", help="This is your color")
@click.option("--year", prompt="I need your year", help="This is your year")
def hello(name, color, year):
    if name == "Thor":
        click.echo("Thor, you are always red.")
        click.echo(click.style(f"Hello {name}!", fg="red"))
        click.echo("Thor war born in" + year)
    else:
        click.echo(click.style(f"Hello world!{name}", fg=color))

if __name__ == "__main__":
    hello()