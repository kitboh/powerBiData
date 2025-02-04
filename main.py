import csv
import random
from datetime import datetime, timedelta

position_in_company = ['Manager', 'Assistant Manager', 'Supervisor', 'Team Leader', 'Senior Developer', 'Junior Developer', 'Intern']
department = ['HR', 'Finance', 'IT', 'Marketing', 'Sales', 'Customer Service', 'Production', 'Logistics', 'Research and Development', 'Acquisitions', 'Leadership', ]
salary = [60000, 55000, 52000, 22000, 24000, 50000, 40000, 30000, 20000, 10000, 8000, 5000]


# Function to generate a random name
def generate_name():
    first_names = ['John', 'Jane', 'Alex', 'Emily', 'Chris', 'Katie', 'Michael', 'Sarah', 'David', 'Laura', 'Fred', 'Deborah', 'Tom', 'Alice', 'Peter', 'Lucy', 'Paul', 'Hannah', 'Simon', 'Olivia', 'Roisin', 'Niamh', 'Derek', 'Eoin', 'Ciaran', 'Sean', 'Aoife', 'Orla', 'Catherine', 'Mary', 'Ella', 'Megan', 'Eva', 'Sophie', 'Ella', 'Grace', 'Lily', 'Ava', 'Ruby', 'Sophia', 'Isabella', 'Oliver', 'Jack', 'Harry', 'Jacob', 'Charlie', 'Thomas', 'George', 'Oscar', 'James', 'William', 'Henry', 'Ethan', 'Alexander', 'Daniel', 'Samuel', 'Joseph', 'Benjamin', 'Luke', 'Matthew', 'Leo', 'Dylan', 'Max', 'Adam', 'Ryan', 'Nathan', 'Isaac', 'Caleb', 'Cameron', 'Connor', 'Evan', 'Mason', 'Aiden', 'Liam', 'Noah', 'Lucas', 'Elijah', 'Michael', 'David', 'Joseph', 'James', 'William', 'Charles', 'Thomas', 'Richard', 'Daniel', 'Matthew', 'Anthony', 'Donald', 'Steven', 'Paul', 'Andrew', 'Kenneth', 'Joshua', 'Kevin', 'Brian', 'Edward', 'Ronald', 'Timothy', 'Jason', 'Jeffrey', 'Gary', 'Ryan', 'Nicholas', 'Eric', 'Stephen', 'Jacob', 'Larry', 'Frank', 'Scott', 'Justin', 'Brandon', 'Raymond', 'Gregory', 'Samuel', 'Benjamin', 'Patrick', 'Jack', 'Henry', 'Walter', 'Dennis', 'Jerry', 'Alexander', 'Peter', 'Tyler', 'Douglas', 'Harold', 'Aaron', 'Jose', 'Adam', 'Arthur', 'Carl', 'Albert', 'Kyle', 'Lawrence', 'Joe', 'Willie', 'Gerald', 'Roger', 'Keith', 'Jeremy', 'Terry', 'Harry', 'Ralph', 'Sean', 'Jesse', 'Roy', 'Louis', 'Billy', 'Austin', 'Bruce', 'Eugene', 'Christian', 'Bryan', 'Wayne', 'Russell', 'Howard', 'Fred', 'Ethan', 'Jordan', 'Philip', 'Alan', 'Juan', 'Randy', 'Vincent', 'Bobby', 'Dylan', 'Johnny', 'Philip']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Blahut', 'Gumpert', 'Higginbotham', 'Hutchins', 'Koehler', 'Krebs', 'Lindholm', 'Loyd', 'Majors', 'Mangum', 'Mcclellan', 'Mccollum', 'Mccracken', 'Mccreary', 'Mccurry', 'Mcgill', 'Mcginnis', 'Mckinley', 'Mcknight', 'Mclendon', 'Mcmillan', 'Mcmullen', 'Mcmurray', 'Mcnabb', 'Mcnulty', 'Mcphee', 'Mcvay', 'Mcvicker', 'Mcvay']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate a random date within the past 20 years
def generate_join_date(age):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365*20)
    join_date = start_date + (end_date - start_date) * random.random()
    # Ensure join date is more than age - 18 years ago
    min_join_date = end_date - timedelta(days=365*(age - 18))
    if join_date > min_join_date:
        join_date = min_join_date - timedelta(days=random.randint(0, 365))
    return join_date.strftime('%Y-%m-%d')

# Generate the CSV file
with open('employees.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['employee_number', 'name', 'position', 'join_date', 'department', 'salary', 'age'])

    for _ in range(10000):
        employee_number = random.randint(1000000, 9999999)
        name = generate_name()
        position = random.choice(position_in_company)
        department = random.choice(department)
        salary_value = random.choice(salary) + random.randint(1, 2500)
        age = random.randint(18, 60)
        join_date = generate_join_date(age)
        
        writer.writerow([employee_number, name, position, join_date, department, salary_value, age])