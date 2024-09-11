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

def show_the_jobs(id):
    try:
        with engine.connect() as conn:
            result = conn.execute(text(f'SELECT * FROM jobs WHERE id = {id}'))
            rows = result.fetchall()
            if len(rows) == 0:
                return None
            else:
                return dict(rows[0]._asdict())
    except Exception as e:
        print(f"Error: {e}")
        raise
    
def final_data(job_id, apply_data):
    try:
        with engine.connect() as conn:
            # for the beginning the transaction
            trans = conn.begin()
            query = text("""
                INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience) 
                VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience)
            """)
            print ("Applying data:", apply_data)
            
            # Execute the query with a dictionary of parameters
            conn.execute(query, {
                'job_id': job_id,
                'full_name': apply_data.get('full_name'),
                'email': apply_data.get('email'),
                'linkedin_url': apply_data.get('linkedin'),  # Ensure this key matches the column name
                'education': apply_data.get('education'),
                'work_experience': apply_data.get('work_experience')
            })
            trans.commit()  # Commit the transaction
            print("Data inserted and committed successfully")
        
    except Exception as e:
        trans.rollback()  # Rollback in case of an error
        print(f"Error during database insertion: {e}")
        raise