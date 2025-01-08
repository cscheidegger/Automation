import random
import string

# Test data for Practice Form
PRACTICE_FORM_DATA = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "mobile": "1234567890",
    "address": "123 Main St, Springfield",
    "date_of_birth": "06 Jan 1990",  # Static date for testing
    "gender": "Male",  # Options: Male, Female, Other
    "hobbies": ["Sports"],  # Options: Sports, Reading, Music
    "subjects": ["Maths"],  # Dynamic subject inputs
    "state": "NCR",  # State dropdown values
    "city": "Delhi",  # City dropdown based on state
}

def generate_random_string(length, chars=string.ascii_letters):
    """Generate a random string of specified length."""
    return ''.join(random.choices(chars, k=length))

def generate_random_number(length):
    """Generate a random numeric string of specified length."""
    return ''.join(random.choices(string.digits, k=length))

def generate_practice_form_data():
    """Generate random data for the Practice Form."""
    return {
        "first_name": generate_random_string(8),
        "last_name": generate_random_string(10),
        "email": f"{generate_random_string(5)}@example.com",
        "mobile": generate_random_number(10),
        "address": generate_random_string(20, string.ascii_letters + string.digits + " "),
        "date_of_birth": f"{random.randint(1, 28)} {random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])} {random.randint(1980, 2000)}",
        "gender": random.choice(["Male", "Female", "Other"]),
        "hobbies": random.sample(["Sports", "Reading", "Music"], k=random.randint(1, 3)),
        "subjects": random.sample(["Maths", "Physics", "Chemistry", "Biology", "English"], k=random.randint(1, 3)),
        "state": random.choice(["NCR", "Uttar Pradesh", "Haryana"]),
        "city": random.choice(["Delhi", "Lucknow", "Agra"]),
    }

# Test data for Web Tables
WEB_TABLES_RECORD = {
    "first_name": "Jane",
    "last_name": "Smith",
    "age": "29",
    "email": "janesmith@example.com",
    "salary": "50000",
    "department": "Engineering",
}

def generate_web_tables_record():
    """Generate random data for a Web Tables record."""
    return {
        "first_name": generate_random_string(8),
        "last_name": generate_random_string(10),
        "age": str(random.randint(18, 65)),
        "email": f"{generate_random_string(5)}@example.com",
        "salary": str(random.randint(30000, 150000)),
        "department": random.choice(["Engineering", "HR", "Sales", "Marketing"]),
    }
