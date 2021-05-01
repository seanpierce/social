CREATE TABLE IF NOT EXISTS posts (
	id SERIAL PRIMARY KEY,
   	content text NOT NULL,
	user_id integer NOT NULL,
    created_at timestamp WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
	FOREIGN KEY (user_id)
        REFERENCES auth_user (id)
        ON DELETE CASCADE
);