from sqlalchemy import create_engine, text
import os

# Fetching environment variables
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

DB_HOSTNAME = os.environ.get('DB_HOSTNAME', '127.0.0.1')  # Default to 127.0.0.1
DB_NAME = os.environ.get('DB_NAME', 'careersoncloud')

if not DB_USERNAME or not DB_PASSWORD:
    raise ValueError("Database username or password is missing. Please check environment variables.")

engine_URL = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_NAME}?charset=utf8mb4'

engine = create_engine(engine_URL)

def load_the_jobs():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    
    jobs = [dict(row) for row in result.all()]
    return jobs
