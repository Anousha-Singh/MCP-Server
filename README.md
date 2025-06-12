# Employee Management MCP Server

This project is an AI-integrated backend server built using **MCP (Model Context Protocol)** and the `fastmcp` library. It allows tools like **Claude** to interact with your employee database through structured tool calls.

## 📌 Features
- Add new employees
- Fetch employee details
- Update employee roles
- Delete employee records
- Integrated with Claude via MCP

## 🚀 Setup Instructions

```bash
pip install uv
uv add mcp[cli]
uv run mcp install main.py
```


## 💬 Usage with Claude

1. Open Claude Desktop App → Settings → Enable Developer Mode  
2. Use prompts like:

```
Call add_employee with emp_id=1001, name="Alice", and role="Engineer"
```

Claude will call your backend tool and return the result.

## 🧰 Available Tools

- `add_employee`: Adds a new employee  
- `get_employee`: Gets employee details by ID  
- `update_role`: Updates an employee’s role  
- `delete_employee`: Deletes an employee by ID

## 🔧 Tech Stack

- Python 3.10+
- `fastmcp` via `mcp[cli]`
- Claude (AI client using MCP integration)


