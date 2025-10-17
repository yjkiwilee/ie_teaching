import numpy as np

def step(grid):
    rows, cols = grid.shape
    new_grid = np.empty((rows, cols))

    for i in range(rows):
        for j in range(cols):
            neighbours = get_neighbours(grid, i, j)
            count = sum(neighbours)            
            # cells are unaffected unless they:
            # - die of under- or overpopulation, or
            # - become alive if they have exactly three neighbours
            if count < 2 or count > 3:
                new_grid[i, j] = 0
            elif count == 3:
                new_grid[i, j] = 1
            else:
                new_grid[i, j] = grid[i, j]
    
    return new_grid
                 
def get_neighbours(grid, i, j):
    rows, cols = grid.shape
    indices = np.array([(i-1, j-1), (i-1, j), (i-1, j+1),
                        (i, j-1),             (i, j+1),
                        (i+1, j-1), (i+1, j), (i+1, j+1)])
    valid_indices = (indices[:, 0] >= 0) & (indices[:, 0] < rows) & \
                    (indices[:, 1] >= 0) & (indices[:, 1] < cols)
    return grid[indices[valid_indices][:, 0], indices[valid_indices][:, 1]]

# Test
grid = np.array([[0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0],
                 [0, 1, 1, 1, 0],
                 [0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0]], dtype=np.int8)
grid = step(grid)
print(grid)

# our grid should show a square pattern, but doesn't
expected_grid = np.array([[0, 0, 0, 0, 0],
                          [0, 1, 1, 1, 0],
                          [0, 1, 0, 1, 0],
                          [0, 1, 1, 1, 0],
                          [0, 0, 0, 0, 0]], dtype=np.int8)
assert np.array_equal(grid, expected_grid)