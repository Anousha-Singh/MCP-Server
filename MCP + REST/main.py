from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from db import Employee
from db import add_employee, get_employee, update_employee, delete_employee

app = FastAPI()

@app.post("/employee/", operation_id="create_employee")
def create_employee(emp: Employee):
    return add_employee(emp)

@app.get("/employee/{emp_id}", operation_id="read_employee")
def read_employee(emp_id: int):
    return get_employee(emp_id)

@app.put("/employee/{emp_id}", operation_id="update_employee")
def modify_employee(emp_id: int, emp: Employee):
    return update_employee(emp_id, emp)

@app.delete("/employee/{emp_id}", operation_id="delete_employee")
def remove_employee(emp_id: int):
    return delete_employee(emp_id)

if __name__ == "__main__":
    # Mount the MCP to the FastAPI app
    
    mcp = FastApiMCP(app, include_operations=["create_employee", "read_employee", "update_employee", "delete_employee"])
    mcp.mount()
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    