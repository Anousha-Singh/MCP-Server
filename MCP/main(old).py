from mcp.server.fastmcp import FastMCP

# Create an MCP server instance
mcp = FastMCP("EmployeeManagement")

# In-memory database
employee_db = {2002: {"name": "Jane Smith", "role": "Intern"}}

# Add an employee
@mcp.tool()
def add_employee(emp_id: int, name: str, role: str) -> str:
    """Add a new employee"""
    if emp_id in employee_db:
        return f"Employee with ID {emp_id} already exists."
    employee_db[emp_id] = {"name": name, "role": role}
    return f"Employee {name} added with ID {emp_id}."

# Get employee details
@mcp.tool()
def get_employee(emp_id: int) -> str:
    """Get employee details"""
    emp = employee_db.get(emp_id)
    if not emp:
        return f"No employee found with ID {emp_id}"
    return f"Name: {emp['name']}, Role: {emp['role']}"


# Update employee role
@mcp.tool()
def update_role(emp_id: int, new_role: str) -> str:
    """Update an employee's role"""
    if emp_id not in employee_db:
        return f"No employee found with ID {emp_id}"
    employee_db[emp_id]["role"] = new_role
    return f"Employee {emp_id} role updated to {new_role}"

# Delete an employee
@mcp.tool()
def delete_employee(emp_id: int) -> str:
    """Delete an employee"""
    if emp_id not in employee_db:
        return f"No employee found with ID {emp_id}"
    del employee_db[emp_id]
    return f"Employee with ID {emp_id} deleted."

if __name__ == "__main__":
    mcp.run()



