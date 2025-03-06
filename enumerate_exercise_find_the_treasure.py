grid = """
.............
.........X...
...X..o......
.............
...........X.
""".strip()
print(grid)

rows = grid.split("\n")
print(rows)
for row, line in enumerate(rows, start=-(len(rows) // 2)):
    for col, char in enumerate(line, start=-(len(line) // 2)):
        if char == "X":
            print(f"Treasure found at ({row}, {col})")
