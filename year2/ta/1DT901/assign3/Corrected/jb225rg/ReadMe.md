Pretty recursive print - Den ör likadan som "recursive_print.py" förutm att jag använde mig av
                         av en til variaben "depth" som hjälpte med att få den fina utskrifen.
                         Jag satte den flrst so 0 och varje gång jag gick in i en dy mapp så kallade
                         jag funktionen igen men med 'depth' + 1. Vid varje utskrift tog jag 'depth' gånger "   " 
                         (tre mellanslag) innan namnet, då jag könde att det gjore finast utskrift.

Lines of python - I start in the cwd and then scan it to get each entry in it and go check each of them. If the 
                  entry is another diretory the functun is called again but for the found diectory. If the entry
                  is a file I check if the file-name ends in '.py'. If it doesn't nothing happens, bur if it does
                  then i go throuch each row of the text. If the length of the row is > 1 then it is non-empty.
                  (len(1) counts all the empty ones to so it has to be longer than it). TIn the beginning i created
                  a variable to count the lines and nof for every row, if the row is non-empty it increases by 1.

Letter count - I use a lot of my 'life_of_brian' code. I ude the code for getting the lines of it and also the individual
               words. For the lines I make a finction the simply go thwough all the lines of the text anf or each line I make if smaller case before adding it to a list thet the function then retuens. With the words i make a function and in that I make a list of the allowed sumbols - and '. I check if the letter har the correct ascii number to not be a-z, after that i check if it is not in the allowed sumbols. If it is the wrong ascii and not in the allowed symbols i replace it with " ". After that i split the strings into individual words and add them to a list thet the function returns.
               For the individual letters i go throuch each letter of the words and add them to a dictionary. If the letter
               is not already in the dictionary it creates a key for the letter with the value 0. If the letter exests the value for said letter increases by one. That function then returns that dictionary.
               I created a variable for the total amount of letters and got that by adding all the values together. I also sorted the dictionary t be in alfabethical order in order to make the print pretty. I decided on making each star in the histogram represent 100 occurances since i found that with other numbers you could actuall se the realy low counts, but the ones with a lot took up the entire screen. 

               (i believe thet making a string of all allowed symbols including a-z and just checking if the letter exists in that might be faster than checking the ascii number and a list)