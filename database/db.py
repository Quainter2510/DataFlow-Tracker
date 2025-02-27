import psycopg2 
from loader import config, logger
from grade_handler import Grade

class DataBase:
    def __init__(self):
        self.conn = psycopg2.connect(user=config.db.user,
                                     password=config.db.password,
                                     host=config.db.host,
                                     port=config.db.port,
                                     database=config.db.database)
        self.create_tables()
        
    def create_tables(self):
        with self.conn.cursor() as cursor:
            cursor.execute('''CREATE table IF NOT EXISTS Grade
                           (user_id TEXT NOT NULL,
                           oauth_consumer_key TEXT,
                           lis_result_sourcedid TEXT NOT NULL,
                           lis_outcome_service_url TEXT NOT NULL,
                           is_correct INT,
                           attempt_type TEXT NOT NULL,
                           created_at timestamp NOT NULL)''')
        self.conn.commit()

    def insert_data(self, grade: Grade):
        with self.conn.cursor() as cursor:
            cursor.execute('''INSERT INTO Grade 
                           VALUES (%s, %s, %s, %s, %s, %s, %s)
                           ''', (grade.user_id,
                           grade.oauth_consumer_key,
                           grade.lis_result_sourcedid,
                           grade.lis_outcome_service_url,
                           grade.is_correct,
                           grade.attempt_type,
                           grade.created_at))
        self.conn.commit()
        
    def get_runs_count_by_last_day(self):
        with self.conn.cursor() as cursor:
            cursor.execute('''SELECT COUNT(*)
                            FROM grade
                            WHERE created_at::date = (SELECT MAX(created_at::date) FROM grade) AND 
                            attempt_type = 'run'
                           ''')
            return cursor.fetchone()[0]
    
    def get_submit_count_by_last_day(self):
        with self.conn.cursor() as cursor:
            cursor.execute('''SELECT COUNT(*)
                            FROM grade
                            WHERE created_at::date = (SELECT MAX(created_at::date) FROM grade) AND 
                            attempt_type = 'commit'
                           ''')
            return cursor.fetchone()[0]
        
    def get_success_submit_count_by_last_day(self):
        with self.conn.cursor() as cursor:
            cursor.execute('''SELECT COUNT(*)
                            FROM grade
                            WHERE created_at::date = (SELECT MAX(created_at::date) FROM grade) AND 
                            attempt_type = 'commit' AND 
                            is_correct = 1
                           ''')
            return cursor.fetchone()[0]
        
    def get_percentage_correct_decisions_by_last_day(self):
        seccess = self.get_success_submit_count_by_last_day()
        all = self.get_submit_count_by_last_day()
        if all == 0:
            return 0 
        return seccess / all
    
    def get_unique_users_by_last_day(self):
        with self.conn.cursor() as cursor:
            cursor.execute('''SELECT COUNT(DISTINCT user_id)
                            FROM grade
                            WHERE created_at::date = (SELECT MAX(created_at::date) FROM grade)
                           ''')
            return cursor.fetchone()[0]
        
    def get_most_popular_task_by_last_day(self):
        with self.conn.cursor() as cursor:
            cursor.execute('''SELECT lis_result_sourcedid, COUNT(*) AS frequency
                            FROM your_table
                            WHERE created_at::date = (SELECT MAX(created_at::date) FROM grade)
                            GROUP BY lis_result_sourcedid 
                            ORDER BY frequency DESC
                            LIMIT 1
                           ''')
            return cursor.fetchone()[0]