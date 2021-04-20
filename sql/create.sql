-- posts
CREATE TABLE IF NOT EXISTS posts (
	id integer PRIMARY KEY,
   	content text NOT NULL,
	user_id integer NOT NULL,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP,
    
	FOREIGN KEY (user_id)
        REFERENCES auth_user (id)
        ON DELETE CASCADE 
        ON UPDATE NO ACTION
) WITHOUT ROWID;