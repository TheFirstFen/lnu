-- creates the table with content for sivans table
CREATE TABLE IF NOT EXISTS sivans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    length INTEGER NOT NULL
);
