import click

@click.group()
def main():
    pass

# inverzní obraz
@main.command(help = "Color inversion")
def invert():
    pass

# převod do odstínů šedi
@main.command(help = "Color removal")
def greyscale():
    pass

# zesvětlení/ztmavení
@main.command(help = "Increase image brightness")
@click.option('--amount', default = 1, help = "Number of steps to apply")
def dodge(amount):
    pass

@main.command(help = "Decrease image brightness")
@click.option('--amount', default = 1, help = "Number of steps to apply")
def burn(amount):
    pass

# zvýraznění hran
@main.command(help = "Edge detection filter")
def edges():
    pass

if __name__ == '__main__':
    main()
