from collections import defaultdict

if __name__ == "__main__":
    T = int(input())
    nums = [i for i in range(2, 5082)]
    primes = []
    gold_bach = defaultdict(list)
    while nums:
        num = nums.pop(0)
        nums = list(filter(lambda x: x % num != 0, nums))
        primes.append(num)

    for i in primes:
        for j in primes:
            if i <= j:
                gold_bach[i+j].append([str(i), str(j)])

    for _ in range(T):
        n = int(input())
        print(' '.join(gold_bach[n][-1]))