class Solution:
    def romanToInt(self, s:str) -> int:
        roman = (
            ('I', 1), ('V', 5), ('X', 10), ('L', 50),
            ('C', 100), ('D', 500), ('M', 1000)
        )
        result = 0
        prev = 0
        for i in s[::-1]:
            for r, v in roman:
                if i == r:
                    if v < prev:
                        result -= v
                    else:
                        result += v
                    prev = v
        return result
    
    def main(self):
        s = 'III'
        
        print(self.romanToInt(s))

if __name__ == "__main__":
    Solution().main()
