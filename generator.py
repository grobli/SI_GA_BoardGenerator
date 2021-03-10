#!/bin/python3

from PIL import Image, ImageDraw
from typing import Tuple
import json
import sys

SCALE = 50
BORDER = 10
PATH_TRANSPARENCY = 'FF'  # transparency in hexadecimal format (00..FF)

COLOR_PALETTE_8 = [
    '#191970',  # midnightblue
    '#006400',  # darkgreen
    '#ff0000',  # red
    '#ffd700',  # gold
    '#00ff00',  # lime
    '#00ffff',  # aqua
    '#ff00ff',  # fuchsia
    '#ffb6c1',  # lightpink
]

COLOR_PALETTE_16 = [
    '#2f4f4f',  # darkslategray
    '#800000',  # maroon
    '#006400',  # darkgreen
    '#00008b',  # darkblue
    '#ff0000',  # red
    '#ffa500',  # orange
    '#ffff00',  # yellow
    '#00ff00',  # lime
    '#00fa9a',  # mediumspringgreen
    '#00ffff',  # aqua
    '#0000ff',  # blue
    '#ff00ff',  # fuchsia
    '#1e90ff',  # dodgerblue
    '#f0e68c',  # khaki
    '#ff1493',  # deeppink
    '#ffb6c1',  # lightpink
]


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


def create_board(solution: dict) -> Image:
    dim_x, dim_y = solution['board']
    im = create_plane(dim_x, dim_y)

    color_palette = COLOR_PALETTE_8 if len(
        solution['paths']) < 9 else COLOR_PALETTE_16

    for i, path in enumerate(solution['paths']):
        color = f'{color_palette[i % len(color_palette)]}{PATH_TRANSPARENCY}'
        draw_lines(im, path, color=color)

    for x, y in solution['points']:
        draw_point(im, x, y)

    return im


def main() -> int:
    def usage():
        print("usage: generate.py <input (*.json)> [<output> (*.png)]")
        return 1

    argv = sys.argv[1:]
    output_path = ''
    if argv:
        # first must be .json file
        if not (json_path := argv.pop(0)).lower().endswith('.json'):
            return usage()

        if argv:  # there are still more options
            output_path = argv.pop(0)

        if argv:  # there are still options - shouldn't happen :(
            return usage()
    else:
        return usage()

    with open(json_path, 'r') as file:
        im = create_board(json.load(file))

    if output_path:
        im.save(output_path)
    else:
        im.show()
    return 0


if __name__ == '__main__':
    main()
