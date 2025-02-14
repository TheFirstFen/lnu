class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def main(self):
        nums = [2, 7, 11, 15]
        target = 9

        print(self.twoSum(nums, target))

if __name__ == "__main__":
    Solution().main()