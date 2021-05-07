from collections import defaultdict


def solution(gems):
    answer = []
    gems_count = defaultdict(int)
    find_gem = len(set(gems))
    start = left = 0
    end = -1
    for right, gem in enumerate(gems):
        if gems_count[gem] == 0:
            find_gem -= 1
        gems_count[gem] += 1

        if find_gem == 0:
            while left < right and gems_count[gems[left]] > 0:
                gems_count[gems[left]] -= 1
                if gems_count[gems[left]] == 0:
                    find_gem += 1
                left += 1
            if end == -1 or end - start > right - left:
                start, end = left, right

    return [start+1, end+1]


if __name__ == "__main__":
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    print(solution(gems))