import sqlite3

# Database setup
DB_NAME = "test_history.db"

def fetch_test_data():
    """
    Fetch test data from the SQLite database.
    
    Returns:
        list of tuples: Each tuple contains (test_name, avg_runtime, failure_count).
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT test_name, avg_runtime, failure_count FROM test_history")
        return cursor.fetchall()

def normalize_data(data, key_index):
    """
    Normalize a specific column of the data to a 0-1 range.
    
    Args:
        data (list of tuples): The test data.
        key_index (int): The index of the column to normalize.
    
    Returns:
        list of floats: Normalized values for the specified column.
    """
    values = [row[key_index] for row in data]
    min_val, max_val = min(values), max(values)
    if min_val == max_val:  # Avoid division by zero
        return [1.0] * len(values)
    return [(val - min_val) / (max_val - min_val) for val in values]

def compute_priority(data):
    """
    Compute a priority score for each test based on normalized runtime and failure count.
    
    Args:
        data (list of tuples): The test data.
    
    Returns:
        list of tuples: Each tuple contains (test_name, priority_score).
    """
    normalized_runtime = normalize_data(data, 1)  # Normalize avg_runtime
    normalized_failures = normalize_data(data, 2)  # Normalize failure_count
    
    priority_scores = []
    for i, row in enumerate(data):
        test_name = row[0]
        # Higher failure count increases priority, slower runtime decreases priority
        priority_score = (1 - normalized_runtime[i]) + normalized_failures[i]
        priority_scores.append((test_name, priority_score))
    
    return sorted(priority_scores, key=lambda x: x[1], reverse=True)

def get_optimized_test_order():
    """
    Get an optimized test execution order based on priority scores.
    
    Returns:
        list of str: Sorted test names based on priority.
    """
    test_data = fetch_test_data()
    if not test_data:
        return []
    
    priority_scores = compute_priority(test_data)
    return [test_name for test_name, _ in priority_scores]

# Example usage
if __name__ == "__main__":
    optimized_order = get_optimized_test_order()
    print("Optimized Test Execution Order:")
    for test_name in optimized_order:
        print(test_name)