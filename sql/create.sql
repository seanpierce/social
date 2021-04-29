-- run this file into sqlite3:
-- sqlite3 db.sqlite3 < ./sql/create.sql

-- posts
CREATE TABLE IF NOT EXISTS posts (
	id integer PRIMARY KEY,
   	content text NOT NULL,
	user_id integer NOT NULL,
    created_at timestamp DEFAULT (datetime('now','localtime')),
    
	FOREIGN KEY (user_id)
        REFERENCES auth_user (id)
        ON DELETE CASCADE
);