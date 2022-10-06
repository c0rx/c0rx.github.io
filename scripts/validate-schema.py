#!/usr/bin/env python3
import jsonschema
import os
import sys
import yaml

def parse_yaml(path):
    with open(path) as fs:
        text = fs.read()
        return yaml.load_all(text, Loader=yaml.SafeLoader)

def build_schema():
    function_names = next(parse_yaml('_data/functions.yml')).keys()
    return {
        "definitions": {
            'examples': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'description': {'type': 'string'},
                        'code': {'type': 'string'},
                        'image': "iVBORw0KGgoAAAANSUhEUgAAAZAAAAGQCAYAAACAvzbMAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAASdAAAEnQB3mYfeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAfGSURBVHic7dzNUSNZAkbRlxOE5ASGqGdF+QDlx5QhNX6g8gFW0xhSTohN9n5ioHsu1flIOCdC6/cp9XMhF1rGGOsAgP/TP2YPAGCfBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIrjY86+cY42nD8+hOY4zrjc76sdE5H9XtRuf4/O7Hlp/fsW70OG/1hHiz+7Hd+4K32ep1ut/qCfFm57HR+8ItLAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEguZo9gHfp9zHGMnsEf8mPjc75faNz2Jl1o8d5qycE8Imdx0bf625hAZAICACJgACQCAgAiYAAkAgIAImAAJAICACJgACQCAgAiYAAkAgIAIlf4/2kHg+Hu3VZ7mfveMWPL5fL3ewR78HD8XgeY9zO3vGSZV2/3jw/+7HUT8h/IAAkAgJAIiAAJAICQCIgACQCAkAiIAAkAgJAIiAAJAICQCIgACQCAkAiIAAkAgJAIiAAJAICQCIgACQCAkAiIAAkAgJAIiAAJAICQCIgACQCAkAiIAAkAgJAIiAAJAICQCIgACQCAkAiIAAkAgJAIiAAJAICQCIgACQCAkAiIAAkAgJAIiAAJAICQCIgACQCAkAiIAAkAgJAIiAAJFezB+zd4+FwN3tDsiyn2RNeta7Xu722v9i6rtdjWWbPeNmynB4Ph9krkpvn5/PsDXsmIG+0Lsv97A0f0rKc1jFc2x1Yx/j2rgP3ut0Ofw/cwgIgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAkqvZAz6AH7MHJOt6PZblNHvGK36OMZ5mj3gnTmOM69kjXrSuT2NZfs6ewfYE5I2+XC53szcUj4fD3TrG/ewdr3ja67X91R6Ox/MY43b2jpcsY3y/uVzOs3ewPbewAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASK5mD9i7h+PxPHtDsa7r9ewNf+K012v7NzjNHvCadYxvD8fj19k7ii+Xy93sDXsmIG93O3tAsiyzF/yZ67HXa/vZLMu7Dhx/H7ewAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIDkavaAvVvW9evsDcmynNYxvs2e8aJ1fVrG+D57xnuwjvFtLMtp9o6XLGN8H+v6NHsH2xOQN7p5fj7P3lA8Hg5jLMvsGS9blp83l8sur+2v9nA8vu8/Utb1aa+fA97GLSwAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQALJ1o8d5qycE8Imdx0bf6/4DASAREAASAQEgERAAEgEBIBEQABIBASAREAASAQEgERAAEgEBIBEQAJKr2QN4l/41xvjnRmfdbXTOR7XVj5T+Z4zx743OYicEhP/ltzHG7ewR/CVbvU7rEBD+i1tYACQCAkAiIAAkAgJAIiAAJAICQCIgACQCAkAiIAAkAgJAIiAAJAICQCIgACQCAkAiIAAkAgJAIiAAJAICQCIgACQCAkAiIAAkAgJAIiAAJAICQCIgACQCAkAiIAAkAgJAIiAAJAICQCIgACQCAkAiIAAkAgJAIiAAJAICQCIgACQCAkByteFZpzHGecPz6E4bnuU9sQ+/Da/VXmz2+V3GGOtWhwHwcbiFBUAiIAAkAgJAIiAAJAICQCIgACQCAkAiIAAkAgJAIiAAJAICQCIgACQCAkAiIAAkAgJAIiAAJAICQCIgACQCAkAiIAAkAgJAIiAAJAICQCIgACQCAkDyB2jsRJS05rjiAAAAAElFTkSuQmCC"
                    },
                    'required': ['code'],
                    'additionalProperties': True
                },
                'minimum': 1
            }
        },
        'type': 'object',
        'properties': {
            'description': {'type': 'string'},
            'functions': {
                'type': 'object',
                "patternProperties": {
                    '^({})$'.format('|'.join(function_names)): {'$ref': '#/definitions/examples'}
                },
                'additionalProperties': True
            },
        },
        'required': ['functions'],
        'additionalProperties': True
    }

def validate_directory(root):
    schema = build_schema()
    root, _, files = next(os.walk(root))
    for name in files:
        if not name.endswith('.md'):
            continue
        path = os.path.join(root, name)
        data = parse_yaml(path)
        try:
            jsonschema.validate(next(data), schema)
        except jsonschema.exceptions.ValidationError as err:
            print('{}: {}'.format(name, err))
            sys.exit(1)

if __name__ == '__main__':
    validate_directory("_gtfobins/")
