import sys
sys.setrecursionlimit(10000)


def solution():
    n = int(input())
    inorder = list(map(int, sys.stdin.readline().strip().split()))
    postorder = list(map(int, sys.stdin.readline().strip().split()))
    preorder = []

    def conversion_tree(inorder, postorder):
        if inorder and postorder:
            preorder.append(postorder[-1])
            index = inorder.index(postorder.pop())

            left = len(inorder[:index])
            right = len(inorder[index+1:])

            conversion_tree(inorder[:index], postorder[:left])
            conversion_tree(inorder[index+1:], postorder[-right:])
        else:
            return

    conversion_tree(inorder, postorder)
    print(' '.join(map(str, preorder)))


if __name__ == "__main__":
    solution()