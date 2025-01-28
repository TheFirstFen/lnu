class init_hash:
    def hash(input):
        tot_sum = 0
        for i,letter in enumerate(input):
            aski = ord(letter)
            tot_sum += aski * (i+1)
        return tot_sum % 256


        