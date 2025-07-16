#!/usr/bin/env python3
"""
Test database connection and creation
"""
import os
import sqlite3
from pathlib import Path

def test_database():
    """Test database creation and connection"""
    print("Testing database setup...")
    
    # Create data directory
    data_dir = Path("data")
    data_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Data directory: {data_dir.absolute()}")
    print(f"Directory exists: {data_dir.exists()}")
    print(f"Directory writable: {os.access(data_dir, os.W_OK)}")
    
    # Test SQLite connection
    db_path = data_dir / "test.db"
    try:
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY)")
        cursor.execute("INSERT INTO test (id) VALUES (1)")
        conn.commit()
        
        cursor.execute("SELECT * FROM test")
        result = cursor.fetchall()
        print(f"Database test successful: {result}")
        
        conn.close()
        
        # Clean up test file
        if db_path.exists():
            db_path.unlink()
            
        return True
    except Exception as e:
        print(f"Database test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_database()
    if not success:
        exit(1)
    print("Database test completed successfully!")
