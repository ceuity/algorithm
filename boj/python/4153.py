if __name__ == "__main__":
    def check_triangle(a, b, c):
        if c**2 == a**2 + b**2:
            return 'right'
        else:
            return 'wrong'

    while True:
        nums = list(map(int, input().split()))
        if sum(nums) == 0:
            break
        nums.sort()
        print(check_triangle(nums[0], nums[1], nums[2]))