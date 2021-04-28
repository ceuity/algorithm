import sys
from collections import defaultdict


def preorder(node, graph, visited):
    if node == '.':
        return
    else:
        visited.append(node)
        preorder(graph[node][0], graph, visited)
        preorder(graph[node][1], graph, visited)
        return visited


def inorder(node, graph, visited):
    if node == '.':
        return
    else:
        inorder(graph[node][0], graph, visited)
        visited.append(node)
        inorder(graph[node][1], graph, visited)
        return visited


def postorder(node, graph, visited):
    if node == '.':
        return
    else:
        postorder(graph[node][0], graph, visited)
        postorder(graph[node][1], graph, visited)
        visited.append(node)
        return visited


def solution():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n):
        node, left, right = map(str, sys.stdin.readline().strip().split())
        graph[node] = [left, right]
    print(''.join(preorder('A', graph, [])))
    print(''.join(inorder('A', graph, [])))
    print(''.join(postorder('A', graph, [])))


if __name__ == "__main__":
    solution()