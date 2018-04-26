a, b, c, d, e, f, g, h = range(8)
N = [
    {b, c, d, e, f},  # a
    {c, e},  # b
    {d},  # c
    {e},  # d
    {f},  # e
    {c, g, h},  # f
    {f, h},  # g
    {f, g}  # h
]

N1 = [
    [b, c, d, e, f],
    [c, e],
    [d],
    [e],  # d
    [f],  # e
    [c, g, h],  # f
    [f, h],  # g
    [f, g]  # h
]

N2 = [
    {b: 2, c: 1, d: 3, e: 9, f: 4},  # a
    {c: 4, e: 3},  # b
    {d: 8},  # c
    {e: 7},  # d
    {f: 5},  # e
    {c: 2, g: 2, h: 2},  # f
    {f: 1, h: 6},  # g
    {f: 9, g: 8}  # h
]
