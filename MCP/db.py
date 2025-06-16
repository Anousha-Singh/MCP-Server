# db.py
from pymongo import MongoClient

# Connect to MongoDB 
client = MongoClient("mongodb://localhost:27017/")

db = client["EmployeeManagementDB"]
employee_collection = db["employees"]

employee_collection.insert_one({"emp_id": 2001, "name": "John Doe", "role": "Software Engineer"})

# Default entries
def initialize_db():
    if employee_collection.count_documents({"emp_id": 2002}) == 0:
        employee_collection.insert_one({"emp_id": 2002, "name": "Jane Smith", "role": "Intern"})

# Utility functions
def add_employee_to_db(emp_id, name, role):
    if employee_collection.find_one({"emp_id": emp_id}):
        return False
    employee_collection.insert_one({"emp_id": emp_id, "name": name, "role": role})
    return True

def get_employee_from_db(emp_id):
    return employee_collection.find_one({"emp_id": emp_id}, {"_id": 0})

def update_employee_role(emp_id, new_role):
    result = employee_collection.update_one({"emp_id": emp_id}, {"$set": {"role": new_role}})
    return result.modified_count > 0

def delete_employee_from_db(emp_id):
    result = employee_collection.delete_one({"emp_id": emp_id})
    return result.deleted_count > 0
