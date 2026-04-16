import random
import math

print("Program started...")

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(leaves):
    nodes = [Node(value=v) for v in leaves]
    while len(nodes) > 1:
        temp = []
        for i in range(0, len(nodes), 2):
            temp.append(Node(left=nodes[i], right=nodes[i+1]))
        nodes = temp
    return nodes[0]

def minimax(node, is_max, counter):
    if node.left is None:
        counter[0] += 1
        return node.value

    if is_max:
        return max(minimax(node.left, False, counter),
                   minimax(node.right, False, counter))
    else:
        return min(minimax(node.left, True, counter),
                   minimax(node.right, True, counter))

def alpha_beta(node, alpha, beta, is_max, counter, pruned):
    if node.left is None:
        counter[0] += 1
        return node.value

    if is_max:
        value = -math.inf
        for child in [node.left, node.right]:
            value = max(value, alpha_beta(child, alpha, beta, False, counter, pruned))
            alpha = max(alpha, value)
            if beta <= alpha:
                pruned[0] += 1
                break
        return value
    else:
        value = math.inf
        for child in [node.left, node.right]:
            value = min(value, alpha_beta(child, alpha, beta, True, counter, pruned))
            beta = min(beta, value)
            if beta <= alpha:
                pruned[0] += 1
                break
        return value

def run_case(case_num):
    leaves = [random.randint(1, 25) for _ in range(8)]
    root = build_tree(leaves)

    print(f"\nCase#{case_num} Output:")
    print("Generated Leaf Nodes:", leaves)

    mini_counter = [0]
    optimal = minimax(root, True, mini_counter)

    print("Minimax:")
    print(" Nodes Evaluated:", mini_counter[0])
    print(" Optimal Value:", optimal)

    ab_counter = [0]
    pruned = [0]

    ab_value = alpha_beta(root, -math.inf, math.inf, True, ab_counter, pruned)

    print("Alpha-Beta Pruning:")
    print(" Nodes Evaluated:", ab_counter[0])
    print(" Nodes Pruned:", pruned[0])
    print(" Optimal Value:", ab_value)

    improvement = ((mini_counter[0] - ab_counter[0]) / mini_counter[0]) * 100
    print(f"Efficiency Improvement: {improvement:.2f}%")

if __name__ == "__main__":
    run_case(1)
    run_case(2)