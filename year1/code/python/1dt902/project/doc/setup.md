# Setup - The software

## List of technologies used

1. Sensor (Micropython)
    - urequests
2. Database (MariaDB)
3. Backend (Rust)
    - Hyper
    - Tokio
    - Serde
    - MySql
4. Website (JavaScript)
    - React
    - Bootstrap
    - ChartJS
5. Hosting
    - NGINX
    - Linux
    - Cloudflare DNS
    - Certbot (SSL)

## Further description

### Sensor

[MicroPython](https://micropython.org/) have been a central part throughout the course. We therefore felt that it was only natural to keep using it in the sensor. It uses the library urequests to communicate with the server.

### Database

Thereafter we quickly noticed that we need to store data measured by our device. The industry standard for dealing with data is MySQL. This is a database which uses the SQL-language, which we thought were suitable for this cause. More specifically we used the community implementation of it called [MariaDB](https://mariadb.org/).

### Backend

In order to order to communicate with the database we needed some middle man. This was because neither micropython nor js in web browser have the capability to directly communicate with an SQL-database. That initiated the development of the project which got the name _dummy_sql_. This server also came in handy when a log-in system was needed. [Rust](https://www.rust-lang.org/) was chosen since it is fast, performant, modern and forces the programmer to think of every time the thread might crash. This means that it becomes much easier to write code which handles errors and exception which might occur, and therefore better code.

To create the webserver the external library [Hyper](https://crates.io/crates/hyper) was used, which allows the creation of a webserver without much friction. Async is and has been a part of Rust for a long time, however creating the main async function can be tedious, which is the reason for the [Tokio](https://crates.io/crates/tokio) dependency. It is wildly used in the Rust community, for the reason that it makes creating the async main function really easy. In order to easily deserialize and parse JSON the (de)serializing library [serde](https://crates.io/crates/serde) was used, in conjunction with [serde_json](https://crates.io/crates/serde_json), which makes parsing JSON to structs very easy. To communicate with MariaDB, the library [MySQL](https://crates.io/crates/mysql) was used. It provides an easy to use way of communicating with MySQL-like databases, which was used in order to read and insert data into the database.

### Website

To create the website without much hassle, and also make it responsive and realtime, [react](https://reactjs.org/) was used. It is one of the industry standards to create fast, pretty, and responsive websites in JavaScript.
To show the data that the sensor collected we realized that a self written website would be the most suitable method. To help with the process of displaying the data we used the library [chartjs](https://www.chartjs.org/), which is a library for creating beautiful and responsible charts. To quickly build the website with beautiful elements, [bootstrap](https://getbootstrap.com/) was used. This is essentially a collection of CSS stylesheets, that are widly used in this context.

### Hosting

In order to have a "URL" [cloudflare dns](https://www.cloudflare.com/) is used. There an A-record pointing to Love's network is defined.

To host the website, server and database a _Raspberry Pi 4 4GB_ was used.It runs the Linux distribution [Raspbian](https://www.raspbian.org/), which among with most other linux-based operating systems is power efficient, performant and stable. This makes linux based operating-systems the firsthand choice for all top 500 supercomputers in the world, nearly all webservers, and a great choice for small computers, where speed and efficiency are dire. For this very reason, it is also used for this project.

To serve the website, encrypt traffic with SSL and manage connections the webserver [NGINX](https://www.nginx.com/) was used. The domain _billenius.com_ which is located at _Cloudflare DNS_ contain a subdomain with an A-record which points to the network, where the _Raspberry Pi 4_ is located. In NGINX a serverblock is defined that accepts traffic coming from this subdomain, and thereafter serves the webpage if no destination is specified. If however _/sql_ is passed, then it proxypasses onto the rustserver. Since NGINX supports SSL encryption, that is also used. Since we use proxypass, it also encrypts traffic to the rustserver.

In order to acquire and renew SSL certificates EFF's [certbot](https://certbot.eff.org/) is used. It uses [LetsEncrypt's](https://letsencrypt.org/) certificates which is a free to use and secure SSL provider.  Certbot provides an excellent way of handling their certificates and offers great integration with NGINX. To automatically renew the certificates it is ran each month as a cronjob with the renew flag.
