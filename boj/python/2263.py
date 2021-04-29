import sys
sys.setrecursionlimit(1000000)


def solution():
    n = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))
    preorder = []
    pos = [0] * (n+1)
    for i in range(n):
        pos[inorder[i]] = i

    def conversion_tree(in_start, in_end, post_start, post_end):
        if (in_start > in_end) or (post_start > post_end):
            return
        parents = postorder[post_end]
        preorder.append(parents)

        left = pos[parents] - in_start
        right = in_end - pos[parents]

        conversion_tree(in_start, in_start+left-1, post_start, post_start+left-1)
        conversion_tree(in_end-right+1, in_end, post_end-right, post_end-1)

    conversion_tree(0, n-1, 0, n-1)
    print(' '.join(map(str, preorder)))


if __name__ == "__main__":
    solution()
