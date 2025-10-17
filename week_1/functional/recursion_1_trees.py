class Node(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.value = name
        self.children = children or []

    def __repr__(self):
        return f"Node({self.value}, {self.children})"

def total_n_nodes(node: Node):
    """
    Calculate the total number of nodes in a tree.

    Parameters:
        node (Node): Tree.
    
    Returns:
        total_n (int): Total number of nodes in the tree.
    """

    return 1 + sum([total_n_nodes(child_node) for child_node in node.children])

def calc_expr(node: Node):
    """
    Evaluate the expression represented by the tree and return the result.

    Parameters:
        node (Node): Tree representing an expression.

    Returns:
        result: The result of the evaluated expression.
    """

    # If value is numeric, return the value itself
    try:
        return float(node.value)
    except ValueError:
        pass
    
    # If value is not a binary operator, throw error
    assert node.value in ["+", "-", "*", "/"], "Value is not a number nor a binary operator"
    # If incorrect number of children, throw error
    assert len(node.children) == 2, "Invalid number of children for binary operator"

    # Calculate result depending on the operator
    match node.value:
        case "+":
            return calc_expr(node.children[0]) + calc_expr(node.children[1])
        case "-":
            return calc_expr(node.children[0]) - calc_expr(node.children[1])
        case "*":
            return calc_expr(node.children[0]) * calc_expr(node.children[1])
        case "/":
            return calc_expr(node.children[0]) / calc_expr(node.children[1])

#    +
#   / \
#  1  *
#    / \
#   2   3
t = Node('+', [Node('1'),
               Node('*', [Node('2'),
                          Node('3')])])


print(total_n_nodes(t))
print(calc_expr(t))