#!/bin/python3

from PIL import Image, ImageDraw
from typing import Tuple
from random import randint
import json

SCALE = 40
BORDER = 5


def create_plane(width: int, height: int) -> Image:
    im_dim = ((width - 1) * SCALE + 2 * BORDER,
              (height - 1) * SCALE + 2 * BORDER)
    im = Image.new('RGB', im_dim)
    draw = ImageDraw.Draw(im)
    draw.rectangle([(0, 0), im_dim], outline=(
        3, 3, 3), fill=(84, 84, 84), width=BORDER)

    for x in range(width):
        for y in range(height):
            draw.rectangle(
                ((x * SCALE + BORDER - 1, y * SCALE + BORDER - 1),
                 (x * SCALE + BORDER + 1, y * SCALE + BORDER + 1)),
                fill=(120, 120, 120))
    return im


def draw_point(im: Image, x: int, y: int):
    draw = ImageDraw.Draw(im)
    draw.ellipse(((x * SCALE + BORDER - SCALE//4, y * SCALE + BORDER - SCALE//4),
                  (x * SCALE + BORDER + SCALE//4, y * SCALE + BORDER + SCALE//4)),
                 fill=(255, 255, 255), outline=(0, 0, 0))


def draw_lines(im: Image, lines: Tuple[Tuple[int, int], ...], color=(255, 255, 255, 125)):
    draw = ImageDraw.Draw(im, 'RGBA')
    line_seq = tuple(((x * SCALE + BORDER, y * SCALE + BORDER)
                      for x, y in lines))
    draw.line(line_seq, width=SCALE//4, joint="curve", fill=color)


if __name__ == '__main__':
    filepath = input("Enter solution (*.json) file path: ")
    output_file = input(
        "Enter output image name (image will be saved as <name>.png): ")
    with open(filepath, 'r') as file:
        solution = json.load(file)

    dim_x, dim_y = solution['Board']
    im = create_plane(dim_x, dim_y)

    for i, path in enumerate(solution['Paths']):
        color = [randint(0, 255) for _ in range(3)]
        color.append(min(125 + i * 10, 255))
        color = tuple(color)
        draw_lines(im, path, color=color)

    for x, y in solution['Points']:
        draw_point(im, x, y)

    im.save(f'{output_file}.png')
    im.show()
