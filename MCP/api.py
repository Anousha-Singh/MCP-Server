# api.py
from mcp.server.fastmcp import FastMCP
from db import (
    add_employee_to_db,
    get_employee_from_db,
    update_employee_role,
    delete_employee_from_db,
)

mcp = FastMCP("EmployeeManagement")

@mcp.tool()
def add_employee(emp_id: int, name: str, role: str) -> str:
    """Add a new employee"""
    if not add_employee_to_db(emp_id, name, role):
        return f"Employee with ID {emp_id} already exists."
    return f"Employee {name} added with ID {emp_id}."

@mcp.tool()
def get_employee(emp_id: int) -> str:
    """Get employee details"""
    emp = get_employee_from_db(emp_id)
    if not emp:
        return f"No employee found with ID {emp_id}"
    return f"Name: {emp['name']}, Role: {emp['role']}"

@mcp.tool()
def update_role(emp_id: int, new_role: str) -> str:
    """Update an employee's role"""
    success = update_employee_role(emp_id, new_role)
    if not success:
        return f"No employee found with ID {emp_id}"
    return f"Employee {emp_id} role updated to {new_role}"

@mcp.tool()
def delete_employee(emp_id: int) -> str:
    """Delete an employee"""
    success = delete_employee_from_db(emp_id)
    if not success:
        return f"No employee found with ID {emp_id}"
    return f"Employee with ID {emp_id} deleted."

