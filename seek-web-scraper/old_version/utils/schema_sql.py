query_create_website_provider_table = ''' 
CREATE TABLE IF NOT EXISTS website_provider (
	website_provider_id INTEGER PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   	name TEXT NOT NULL UNIQUE
);
'''

query_create_advertiser_table = ''' 
CREATE TABLE IF NOT EXISTS advertiser (
	advertiser_id INTEGER PRIMARY KEY,
   	name TEXT NOT NULL UNIQUE
);
'''

query_create_website_provider_advertiser_table = ''' 
CREATE TABLE IF NOT EXISTS website_provider_advertiser (
    website_provider_id INTEGER,
    advertiser_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (website_provider_id, advertiser_id),
    FOREIGN KEY (website_provider_id) 
        REFERENCES website_provider (website_provider_id) 
        ON DELETE CASCADE 
        ON UPDATE NO ACTION,
    FOREIGN KEY (advertiser_id) 
        REFERENCES advertiser (advertiser_id) 
        ON DELETE CASCADE 
        ON UPDATE NO ACTION
);
'''

query_create_job_table = ''' 
CREATE TABLE IF NOT EXISTS job (
	job_id INTEGER PRIMARY KEY,
	advertiser_id INTEGER NOT NULL,
   	title TEXT NOT NULL,
   	link TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (advertiser_id) 
      REFERENCES advertiser (advertiser_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);
'''

query_create_tech_stack_table = ''' 
CREATE TABLE IF NOT EXISTS tech_stack (
	tech_stack_id INTEGER PRIMARY KEY,
   	category TEXT NOT NULL,
   	subcategory TEXT NOT NULL,
   	stack TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

query_create_job_tech_stack_table = ''' 
CREATE TABLE IF NOT EXISTS job_tech_stack (
    job_id INTEGER,
    tech_stack_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (job_id, tech_stack_id),
    FOREIGN KEY (job_id) 
        REFERENCES job (job_id) 
        ON DELETE CASCADE 
        ON UPDATE NO ACTION,
    FOREIGN KEY (tech_stack_id) 
        REFERENCES tech_stack (tech_stack_id) 
        ON DELETE CASCADE 
        ON UPDATE NO ACTION
);
'''

query_insert_website_provider_table = "INSERT OR IGNORE INTO website_provider (name) VALUES (?);"
query_insert_advertiser_table = "INSERT OR IGNORE INTO advertiser (name) VALUES (?);"
query_insert_website_provider_advertiser_table = "INSERT OR IGNORE INTO website_provider_advertiser (website_provider_id, advertiser_id) VALUES (?, ?);"
query_insert_job_table = "INSERT INTO job (advertiser_id, title, link) VALUES (?, ?, ?);"
query_insert_tech_stack_table = "INSERT OR IGNORE INTO tech_stack (category, subcategory, stack) VALUES (?, ?, ?);"
query_insert_job_tech_stack_table = "INSERT OR IGNORE INTO job_tech_stack (job_id, tech_stack_id) VALUES (?, ?);"

query_select_get_tech_stack_id = "SELECT tech_stack_id FROM tech_stack WHERE category=? AND subcategory=? AND stack=?"
query_select_get_website_provider_id = "SELECT website_provider_id FROM website_provider WHERE name = ?"
query_select_get_advertiser_id = "SELECT advertiser_id FROM advertiser WHERE name = ?"
