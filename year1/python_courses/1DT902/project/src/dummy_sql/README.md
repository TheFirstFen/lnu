# dummy_sql

Since Raspberry Pi Pico's are not powerful and also doesn't have that much memory
getting a mysql client working isn't feasable. That's the reason to this server.
It listens for http-requests on port *8579* and if password match with the
database's password, it will enter the query into the sql server.

## Headers

|Key|Value|
|:--:|:--:|
|x-celsius|float|
|x-humidity|float|
|x-password|String|
