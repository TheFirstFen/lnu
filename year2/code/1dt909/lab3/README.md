# Assignment 3

<!--TODO: Rewrie -->

## Instructions

To run Problem 1:

In terminal 1:

```bash
go run srv.go
```

In terminal 2:

```bash
go run p1.go
```

To run Problem 2:

In terminal 1:

```bash
cd p2_srv/
go run .
```

In terminal 2:

```bash
go run p2.go
```

If you don't get p2 to work check with `init.sql` file that the db tables are correct.

## Problems

### Problem 2

#### Overview

The provided code consists of two main components: a client-side application (`p2.go`) and a server-side application (`p2_srv.go`). The server-side application interacts with a MySQL database to perform CRUD operations on student records, while the client-side application facilitates user interaction via a command-line interface.

##### Client-side Application (`p2.go`)

1. It provides a command-line interface (CLI) for users to interact with student records stored in the database.
2. Users can perform operations such as creating, retrieving, updating, and deleting student records.
3. Each operation sends HTTP requests to the server-side application (`p2_srv.go`) to perform the corresponding database operation.
4. It uses the `http` package in Go to make HTTP requests to the server.

##### Server-side Application (`p2_srv.go`)

1. It uses the Gorilla Mux router to define routes for handling HTTP requests.
2. It connects to a MySQL database and initializes it with a `students_db` schema and a `students` table using the provided `init.sql` script.
3. It defines HTTP handler functions for handling CRUD operations on student records.
4. It uses SQL queries to interact with the MySQL database (`INSERT`, `SELECT`, `UPDATE`, `DELETE`).

##### Concurrency Handling

Concurrency in web applications typically involves handling multiple requests simultaneously without data corruption or inconsistency. Here's how you can handle concurrency in this scenario:

1. **Database Connection Pooling**: Ensure that your server application uses a connection pool to manage database connections efficiently. This allows multiple requests to share and reuse database connections, reducing overhead and improving performance.

2. **Transaction Management**: Wrap related database operations (e.g., create, update, delete) within transactions to maintain data consistency. Begin transactions before executing database operations and commit or rollback transactions based on the success or failure of those operations.

3. **Isolation Levels**: Choose appropriate isolation levels for transactions to control the visibility of data changes across concurrent transactions. For example, using the `READ COMMITTED` isolation level ensures that each transaction sees only committed data, preventing dirty reads.

4. **Concurrency Control Mechanisms**: Implement concurrency control mechanisms such as locking to prevent concurrent access to the same data by multiple transactions. Use row-level or table-level locks judiciously to balance concurrency and performance.

5. **Error Handling**: Implement robust error handling and recovery mechanisms to handle database errors gracefully. Retry failed database operations where appropriate, with backoff strategies to mitigate contention and avoid overwhelming the database.

6. **Testing and Benchmarking**: Thoroughly test your application under simulated load and concurrency to identify and address potential bottlenecks or race conditions. Use tools like Apache Bench or wrk to benchmark your application's performance and concurrency handling capabilities.

By incorporating these concurrency handling strategies into your application design and implementation, you can ensure robustness, reliability, and scalability in handling concurrent requests and database accesses.
