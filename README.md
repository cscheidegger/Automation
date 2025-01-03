**QA Automation Exercise
**
Welcome to my QA automation exercise ! The purpose of this project is to practice QA automation using best practices and simple tools, such as cucumber using BDD for Python. 

This repository is designed to demonstrate automated testing capabilities for both API and frontend scenarios. The project is split into two parts:

1. API Automation: Validates the functionality of a book management API.
2. Frontend Automation: Simulates user interactions with a web interface for the same API.

**Project Purpose**
The purpose of this project is to automate testing workflows for an API and its frontend counterpart, ensuring that key operations such as user creation, authentication, and book management work seamlessly.

**Key Objectives**
# Automate end-to-end testing of the API.
# Simulate user interactions with the web application.
# Ensure compatibility and alignment between backend and frontend functionalities.
# Demonstrate clean, scalable, and reusable code.

**How to Run the Project**
Prerequisites
Ensure the following are installed on your system:

Python 3.10+
pip (Python package installer)
Google Chrome (for frontend automation)
ChromeDriver (compatible with your Chrome version)

 Setup Instructions
# 1. Clone the Repository
git clone <repository-url>
cd qa_automation

# 2. Set Up a Virtual Environment 
python -m venv venv

# 3. Activate the Virtual Environment
Windows
.\venv\Scripts\activate
Mac/Linux:
source venv/bin/activate

# 4. Install Dependencies 
pip install -r requirements.txt

# 5. Verify Installation 
Ensure all dependencies are installed and the environment is ready: 
pip list

**Running Tests**
# Part 1: API Automation
To validate the API's functionality:
1. Navigate to the api_automation directory:
```python
cd api_automation
```
2. Run Behave Tests: 
```python
behave features
```
**Important Notes for API Tests
A unique username must be generated for each test run to ensure successful validation.
The test suite automatically generates a random username (8 alphanumeric characters) and uses a secure password.

If you encounter issues, verify that:

The API server is accessible.
The generated username is unique.
The API meets all requirements outlined in the Swagger documentation.

**
# Part 2: Frontend Automation
To test the web interface:

1. Navigate to the frontend_automation directory:
cd frontend_automation
2. Run the frontend automation script:
python -m unittest discover -s tests -p "test_*.py"

# Important Notes for Frontend Tests
Ensure Google Chrome and ChromeDriver are installed and compatible.
The frontend tests simulate user interactions for book management, aligned with the API operations.

# Project Structure # 
qa_automation/
├── api_automation/           # API Automation Tests
│   ├── api_client.py         # API Client for interacting with backend endpoints
│   ├── features/             # Behave feature files and step definitions
│   │   ├── api_test.feature  # Gherkin feature file for API tests
│   │   ├── steps/            # Step definitions for Behave tests
│   │       ├── api_steps.py  # Implementation of test steps
│   │       ├── __init__.py   # Package initialization (optional, can be empty)
│   ├── requirements.txt      # API automation dependencies
│
├── frontend_automation/      # Frontend Automation Tests
│   ├── tests/                # Test scripts for frontend automation
│   │   ├── test_demoqa.py    # Test cases for the web interface
│   ├── requirements.txt      # Frontend automation dependencies
│
├── README.md                 # Project documentation

# Best Practices
1. Generating Unique Users
For API automation, a unique username is generated automatically before each test run to avoid conflicts.
The username follows an 8-character alphanumeric format, ensuring uniqueness.
Password might need to be adapted, to meet common security requirements

2. Debugging Errors
API Errors:
Ensure the API server is accessible.
Test the endpoints manually using tools like Postman.
Check the logs generated during test execution for detailed error messages.
Frontend Errors:
Verify that the ChromeDriver version matches your Google Chrome installation.
Check browser logs and screenshots (if implemented) for test failures.

# Dependencies # 
API Automation
behave: For BDD (Behavior-Driven Development) testing.
requests: For making API calls.

Frontend Automation 
selenium: For browser-based UI testing.
unittest: For structuring test cases.

Common 
install all dependencies using : 
pip install -r requirements.txt

# Contribution # 
If you'd like to improve or extend this project:

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with detailed explanations of your changes.

# Contact # 
For questions or support, feel free to reach out: 
Caio Scheidegger
cscheidegger@gmail.com
linkedin - caioscheidegger