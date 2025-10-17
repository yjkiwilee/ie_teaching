import numpy as np

def attach_names(data: np.array, names: list[str]):
    assert len(data) == len(names)

    return [
        {
            'name': name,
            'data': row
        } for row, name in zip(data, names)
    ]

data = np.array([[1., 2., 3.],
                 [4., 5., 6.]])

output = attach_names(data, ['Alice', 'Bob', 'Charlie'])
print(output)