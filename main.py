#!/usr/bin/env python3

from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import click

def image_command(func):
    """
        A decorator for Click options common to all image commands.
    """
    options = [
            click.option('--in-place', is_flag = True, default = False, help = "Apply the modifier in-place"),
            click.option('-o', '--output', type = click.Path()),
            click.argument('filename'),
            ]

    for option in reversed(options):
        func = option(func)

    return func

def save_image(image, filename, in_place, output):
    """
        Saves image in OUTPUT, if it's not None. Otherwise, if IN_PLACE
        is True, it saves the image in FILENAME.
    """
    if output:
        image.save(output)
    elif in_place:
        image.save(filename)
    else:
        click.echo("Output file not specified!")
        click.echo("If you want to edit the file in-place, use --in-place flag.")

@click.group()
def main():
    """
        Function stub that acts as a group for all image commands the
        application supports.
    """
    pass

# inverzní obraz
@main.command(help = "Color inversion")
@image_command
def invert(filename, in_place, output):
    """
        Click command that inverts the colors of image at FILENAME.
    """
    image = ImageOps.invert(Image.open(filename))
    save_image(image, filename, in_place, output)

# převod do odstínů šedi
@main.command(help = "Color removal")
@image_command
def greyscale(filename, in_place, output):
    """
        Click command that removes the colors from image at FILENAME.
    """
    image = ImageOps.grayscale(Image.open(filename))
    save_image(image, filename, in_place, output)

# zesvětlení/ztmavení
@main.command(help = "Increase / decrease image brightness")
@image_command
@click.option('--value', type = float, default = 1.0, help = "Brightness multiplication coefficient")
def brightness(filename, in_place, output, value):
    """
        Click command that modifies the brightness of image at FILENAME.
    """
    image = Image.open(filename)
    image = ImageEnhance.Brightness(image).enhance(value)
    save_image(image, filename, in_place, output)

# zvýraznění hran
@main.command(help = "Edge detection filter")
@image_command
def edges(filename, in_place, output):
    """
        Click command that increases edge contrast in image at FILENAME.
    """
    image = Image.open(filename).filter(ImageFilter.EDGE_ENHANCE)
    save_image(image, filename, in_place, output)

if __name__ == '__main__':
    main()
