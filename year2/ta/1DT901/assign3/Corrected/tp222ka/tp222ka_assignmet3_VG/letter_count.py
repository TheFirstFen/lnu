import os


def count_letter(path, file_name):
    # full path to the file
    full_path = path + file_name
    # Dict
    char_dict = {}

    with open(full_path, "r", encoding="utf-8") as file:
        for line in file:
            # Step 1: Convert to lowercase
            line = line.lower()
            for char in line:
                # If char is alphabet
                # Remove ".","!","?",":", number etc
                if char.isalpha():
                    # Add to the current char
                    if char in char_dict:
                        # If char in dict add 1 to it
                        char_dict[char] += 1
                    else:
                        # Add to the dict
                        char_dict[char] = 1
        # Sort dictionary based on keys
        letter_sorted = sorted(char_dict.items(), key=lambda tpl: tpl[0])
    return letter_sorted


def main():
    # file path
    path = os.getcwd()
    txt_file = "\\assignment-03\\brian_13393_words.txt"

    # Call count_letter
    result = count_letter(path, txt_file)

    scaling_factor = 220
    # print
    print(f"Histogram (where each star represents {scaling_factor}", end=" ")
    print("occurrences of the given letters)")
    for i in range(len(result)):
        print(result[i][0], "|", "*" * int(result[i][1]/scaling_factor))


# run the program
main()
