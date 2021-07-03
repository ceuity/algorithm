from itertools import permutations

if __name__ == "__main__":
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    nums = sorted(nums)

    perm = list(permutations(nums, M))
    for i in perm:
        print(' '.join(map(str, i)))