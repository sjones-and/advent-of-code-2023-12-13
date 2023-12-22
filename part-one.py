#!/usr/bin/env python3

import os
from time import perf_counter_ns
from itertools import chain

def fuzzy_equal(a, b):
    return int.bit_count(a ^ b) <= 1

def answer(input_file):
    start = perf_counter_ns()
    with open(input_file, 'r') as input:
        puzzles = input.read().replace('.','0').replace('#','1').split('\n\n')

    answer = 0
    for puzzle in puzzles:
        puzzle_rows = puzzle.split('\n')
        rows = {k:v for k,v in enumerate((
            int(puzzle_rows[iy],2)
            for iy in range(len(puzzle_rows))
        ))}
        cols = {k:v for k,v in enumerate((
            int(''.join([puzzle_rows[iy][ix] for iy in range(len(puzzle_rows))]),2)
            for ix in range(len(puzzle_rows[0]))
        ))}

        mirror_axis = next(chain((
            (i + 1) * 100
            for i in range(len(rows) - 1)
            if rows[i] == rows[i + 1] 
            if all([rows[i - j] == rows[i + j + 1] for j in range(1, min(len(rows) - i - 2, i) + 1)])
        ), (
            i + 1 
            for i in range(len(cols) - 1)
            if cols[i] == cols[i + 1] 
            if all([cols[i - j] == cols[i + j + 1] for j in range(1, min(len(cols) - i - 2, i) + 1)])
        )), None)

        answer += mirror_axis

    end = perf_counter_ns()

    print(f'The answer is: {answer}')
    print(f'{((end-start)/1000000):.2f} milliseconds')

input_file = os.path.join(os.path.dirname(__file__), 'input')
answer(input_file)
