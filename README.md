## PCB Board Picture Generator for visualizing GA solutions (AI Lab)

<div align="center">
  <img src="https://github.com/m-LoKi-g/SI_GA_BoardGenerator/blob/master/board.png?raw=true">
</div>

### Dependencies

- Python 3.8 (or newer)
- [Pillow](https://python-pillow.org)

### Installation

To install **Pillow** use following command in your terminal (assuming you have **Pip** installed):

```
pip install Pillow
```

### Usage

#### 1. Solution JSON file

First you need to generate yourself a solution JSON file in the format just like following example (contents of `example.json`):

```
{
  "board": [6, 6],
  "generation": 1,
  "fitness": 21.37,
  "points": [
    [1, 3],
    [5, 3],
    [3, 1],
    [3, 3]
  ],
  "paths": [
    [
      [1, 3],
      [1, 4],
      [5, 4],
      [5, 3]
    ],
    [
      [3, 1],
      [3, 3]
    ]
  ]
}
```

Where:

- `board` represents dimensions of PCB board `[x, y]` which means width and height respectively.
- `generation` is a number of generation the solution represents (optional)
- `fitness` is solution's fitness value (optional)
- `points` is a list of _points_ that need to be connected on the PCB. Each point is represented by a _list_ of coordinates `[x, y]`.
- `paths` is a list of paths between _points_. Each sublist like:

  ```
      [
          [3, 1],
          [3, 3]
      ]
  ```

  represents one complete path between two points. Each sublist of path list represents a point which is a part of given path.

#### 2. Run script

Interface: `generate.py <input (*.json)> [<output (*.png)>]`

Options:

- `<input (*.json)>` - solution file in JSON format, i.e. `example.json` (obligatory).
- `[<output (*.png)>]` - path of the saved result file, i.e. `board.png` (optional - if not given then script will only show the result in the window without saving it).

##### Usage examples

```
>> python generator.py example.json board.png    ### result is saved to file named board.png

>> python generator.py example.json    ### result is only displayed in system window
```

### Extras

You can change the scale of generated image by modifying `SCALE` constant in `generator.py`.
