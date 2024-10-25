# Proggramering Lab 3

## 1dt909 Parallellprogrammering

### Emil Ulvagården

#### Run the program

For the first problem run srv.go and then for the second problem run srv2.go

```Powershell

go run srv.go

go run srv2.go

```

For the first problem run Prob1.go and then for the second problem run Prob2.go

```Powershell


go run Prob1.go

go run Prob2.go

```

To run Problem one run the server in on terminal and the program in another terminal. The same thing should also be done for the second problem.

To run the server in the second problem change the constants in srv2.go to give the server access to the database.

#### Problem 2

Problem two consists of two components that are the server srv2.go and the application Prob2.go. First one needs to have MySQL and set up the database mydb by runing the program Database_Schema
.sql. When the database is setup correctly the server srv2.go can be run and then with the application Prob2.go the user can interact with the using CRUD.

The server is connected to the database mydb with the schemas student and the schema is provided in DataBase_Schema.sql. The server handles http operations where Create, Read, Update and Deleate are the available functions. The server uses SQL queries to make the CRUD interactions with the database. The server uses gorilla/mux to handle http requests.

The application is an interface for the terminal that a user can interact with the stored information of students in the database. The different operations are CRUD and the operations are sent by http requests to the server srv2.go.
