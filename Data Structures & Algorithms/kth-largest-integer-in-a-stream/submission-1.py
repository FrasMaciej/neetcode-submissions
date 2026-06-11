class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        nums = list(self.nums)
        print(nums)
        max_n = 0
        for i in range(self.k):
            max_n = max(nums)
            nums.remove(max_n)
        return max_n
