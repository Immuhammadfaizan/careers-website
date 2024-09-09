from sqlalchemy import create_engine, text
import os

# Fetching environment variables
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

DB_HOSTNAME = os.environ.get('DB_HOSTNAME')  # Default to 127.0.0.1
DB_NAME = os.environ.get('DB_NAME', 'careersoncloud')

if not DB_USERNAME or not DB_PASSWORD:
    raise ValueError("Database username or password is missing. Please check environment variables.")

engine_URL = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_NAME}?charset=utf8mb4'

engine = create_engine(engine_URL)

def load_the_jobs():
    try:
        with engine.connect() as conn:
            # Execute the query
            result = conn.execute(text('SELECT * FROM jobs'))
            rows = result.fetchall()
            jobs = [dict(row._asdict()) for row in rows]
            return jobs
        
    except Exception as e:
        print(f"Error: {e}")
        raise
