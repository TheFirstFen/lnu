# Assignment 2

## Emil Ulvagården (eu222dq@student.lnu.se)

### Problem 1

No file or directory given so automatically uses index.html

![No given file or directory](./Pic/Main.png)

Input directory a, presents /a/index.html

![Directory a](./Pic/a.png)

Input index.html, presents /index.html

![Index.html](./Pic/Index.png)

Input fun.htm, presents fun.htm

![fun.html](./Pic/fun.png)

Input clown.png, presenst clown.png

![clown.png](./Pic/clown.png)

Input directory s, presents 404 file not found

![Invalid directory or file](./Pic/s.png)

Input test500, presents server error

![Test code 500](./Pic/test500.png)

### Problem 2

Redirect is made if the input is: redirect and it takes the user to /a/b/c/c.html .This is to test the redirect of status code 302

![Rediret](./Pic/redirect.png)

To show 404 Not found. If any path that is not in the public directory the server shows a File Not Found page and prints 404: File Not Found.

![404](./Pic/404.png)

To test the status code 500 type in test500 as the input to throw a runtimeException to simulate a server error.

![Simulated 500](./Pic/simulated500.png)
