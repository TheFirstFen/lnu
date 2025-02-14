class Solution:
    def isPalindrome(self, x:int) -> bool:
        return str(x) == str(x)[::-1]

    def main(self):
        x = -121

        print(self.isPalindrome(x))
    
if __name__ == "__main__":
    Solution().main()