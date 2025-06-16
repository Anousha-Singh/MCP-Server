from pymongo import MongoClient
from pydantic import BaseModel

class Employee(BaseModel):
    emp_id: int
    name: str
    role: str

client = MongoClient("mongodb://localhost:27017/")  # Replace with your URI if needed
db = client["EmployeeManagementDB"]
collection = db["employees"]


def add_employee(emp: Employee):
    if collection.find_one({"emp_id": emp.emp_id}):
        return {"error": "Employee already exists"}
    collection.insert_one(emp.dict())
    return {"message": "Employee added successfully"}

def get_employee(emp_id: int):
    emp = collection.find_one({"emp_id": emp_id}, {"_id": 0})
    if emp:
        return emp
    return {"error": "Employee not found"}

def update_employee(emp_id: int, emp: Employee):
    result = collection.update_one({"emp_id": emp_id}, {"$set": emp.dict()})
    if result.modified_count:
        return {"message": "Employee updated successfully"}
    return {"error": "Employee not found or data unchanged"}

def delete_employee(emp_id: int):
    result = collection.delete_one({"emp_id": emp_id})
    if result.deleted_count:
        return {"message": "Employee deleted successfully"}
    return {"error": "Employee not found"}
