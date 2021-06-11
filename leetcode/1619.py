class Solution:
    def trimMean(self, arr: List[int]) -> float:
        divided = int(len(arr) * 0.05)
        arr.sort()
        new_arr = arr[divided:-divided]
        return (sum(new_arr) / len(new_arr))