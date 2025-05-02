import sqlite3
from datetime import datetime

# Database setup
DB_NAME = "test_history.db"

def setup_database():
    """Create the test history table if it doesn't exist."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS test_history (
                test_name TEXT PRIMARY KEY,
                avg_runtime REAL,
                failure_count INTEGER
            )
        """)
        conn.commit()

def log_test_result(test_name, duration, passed):
    """
    Log the result of a test.
    
    Args:
        test_name (str): The name of the test.
        duration (float): The runtime of the test in seconds.
        passed (bool): Whether the test passed or failed.
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        
        # Check if the test already exists in the database
        cursor.execute("SELECT avg_runtime, failure_count FROM test_history WHERE test_name = ?", (test_name,))
        row = cursor.fetchone()
        
        if row:
            # Update existing record
            avg_runtime, failure_count = row
            new_avg_runtime = (avg_runtime + duration) / 2
            new_failure_count = failure_count + (0 if passed else 1)
            cursor.execute("""
                UPDATE test_history
                SET avg_runtime = ?, failure_count = ?
                WHERE test_name = ?
            """, (new_avg_runtime, new_failure_count, test_name))
        else:
            # Insert new record
            failure_count = 0 if passed else 1
            cursor.execute("""
                INSERT INTO test_history (test_name, avg_runtime, failure_count)
                VALUES (?, ?, ?)
            """, (test_name, duration, failure_count))
        
        conn.commit()

# Example usage
if __name__ == "__main__":
    setup_database()
    log_test_result("test_example", 1.5, True)
    log_test_result("test_example", 2.0, False)
    log_test_result("test_another", 0.8, True)