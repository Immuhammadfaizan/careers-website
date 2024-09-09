from sqlalchemy import create_engine, text
import os

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOSTNAME = '127.0.0.1'
DB_NAME = 'careersoncloud'

engine_URL = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/{DB_NAME}?charset=utf8mb4'

engine = create_engine(engine_URL)

def load_the_jobs():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    
    jobs = []
    for row in result.all():
      jobs.append(dict(row))
      
    return jobs
