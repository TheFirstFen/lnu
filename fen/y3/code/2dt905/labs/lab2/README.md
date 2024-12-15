# 2DT905 : Lab 2 : [Samuel Berg](mailto:sb224sc@student.lnu.se)

## Compile & execution

- Compile Server

    Linux: `javac *.java`

    Windows: `javac Main.java`

- Run Server

    Linux: `java Main [port] [source_directory]`

    Windows: `java Main.class [port] [source_directory]`

- Example Execution

    `java Main 8888 public/`

- Test Server

    `python testa2u1.py` (Included test file)

    `python test.py` (Concurrency test file)

- Status codes

    To get a 302 Redirect go to localhost:{port}/redirect

## Report

### Request

#### HTML/HTM file

![html](./img/html.png)

![html server](./img/html_server.png)

#### Image file

![img](./img/img.png)

![img server](./img/img_server.png)

#### Directory

![dir](./img/dir.png)

![dir server](./img/dir_server.png)

### Response codes

#### 200 OK

![html](./img/html.png)

![html server](./img/html_server.png)

#### 302 Redirect

Tested by going to `/redirect`

![redirect server](./img/redirect.png)

#### 404 File Not Found

Tested by going to `/d`

![file not found](./img/FNF.png)

![file not found server](./img/FNF_server.png)

#### 500 Internal Server Error

Note: Not working as I expect it to. Did work as expected when trying to implement POST, unsure how to stimulate the same error now that I did not have time to implement POST properly so I removed it from code base.

Tested by going to `/error` which should "simulate 500 Internal Server Error"

![internal server error](./img/ISE_server.png)

### Exceptions

Handled exceptions are IOExceptions and General Exceptions.

Why?:

- General Exceptions: To catch any unexpected exceptions that might occur during execution of the run method.

- IOExceptions: IO operations such as reading and writing to a socket can fail due to several diffrent reasons for example network issues, closed connections or file access problems.
