# AI-Powered Test Suite Optimization

This project uses machine learning to intelligently reorder test execution in CI/CD pipelines. It learns from test history (failure count and execution time) and prioritizes critical or flaky tests earlier in the pipeline—helping teams catch bugs faster and reduce CI wait time.

## Features

- Learns from test run history using SQLite
- Ranks tests using runtime and failure trends
- Executes tests in a smarter, adaptive order
- Compatible with Pytest and GitHub Actions

## Tech Stack

- Python 3.10
- Pytest
- SQLite
- scikit-learn
- GitHub Actions (CI)

## How It Works

1. Run tests and log outcomes in `test_history.db`
2. Use ML logic to assign priority to each test
3. Execute the test suite in optimized order

## Project Structure

- `ai_test_optimizer.py` – Ranking logic based on history
- `test_logger.py` – Logs test name, duration, pass/fail to DB
- `run_tests.py` – Runs tests in optimized order
- `tests/` – Folder for Pytest test cases
- `test_history.db` – SQLite file (auto-created)
- `requirements.txt` – Dependencies

## Usage


pip install -r requirements.txt
python test_logger.py        # Creates test_history.db
python ai_test_optimizer.py # Shows optimized order
python run_tests.py         # Runs tests with AI ordering

Example Output

Running tests in optimized order: ['test_example_fail', 'test_example', 'test_another']
Test 'test_example_fail' FAILED in 2.00 seconds.
Test 'test_example' PASSED in 1.00 seconds.
Test 'test_another' PASSED in 0.50 seconds.
