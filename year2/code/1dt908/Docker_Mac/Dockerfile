# Use an official MySQL runtime as a parent image
FROM mysql:8.0.36-bullseye

# Set the root password for MySQL (change it to a secure password)
ENV MYSQL_ROOT_PASSWORD=toor

# Create a database and user (change these values as needed)
# ENV MYSQL_DATABASE=test
# ENV MYSQL_USER=hotel2
# ENV MYSQL_PASSWORD=hotel2

# Expose the MySQL port
EXPOSE 33060

# Copy custom configuration file (if needed)
# COPY my.cnf /etc/mysql/my.cnf

# Uncomment the line below if you want to initialize the database with a SQL script
COPY init.sql /docker-entrypoint-initdb.d/

# CMD instruction provides default command to run when the container starts
CMD ["mysqld"]

# Healthcheck (uncomment if needed)
HEALTHCHECK --interval=30s --timeout=3s CMD mysqladmin ping -u root -p$MYSQL_ROOT_PASSWORD || exit 1
