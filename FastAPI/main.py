from fastapi import FastAPI
from pydantic import BaseModel

# 1. Create an instance of the FastAPI application
app = FastAPI()

members = ["Rajat", "Kunal"]

# 2. Define a "route" or "endpoint"
@app.get("/")
def read_root():
    # 3. Return the response
    return {"Hello": "World"}

@app.get("/rajat")
def read_rajat():
    return {
        "Hello": "Rajat"
    }

@app.get("/api/members")
def get_members():
    return {
        "members": members
    }

@app.post("/api/add_member/{name}")
def add_member(name: str):
    members.append(name)
    return {
        "message": f"Member {name} added successfully!",
        "members": members
    }

class Members(BaseModel):
    names: list[str]

@app.post("/api/add_members")
def add_members(members_list: Members):
    # Extract the list of names from the request body
    new_names = members_list.names
    # Add the new names to the existing members list
    members.extend(new_names)
    return {
        "message": f"{len(new_names)} members added successfully!",
        "members": members
    }

@app.get("/api/search_members")
def search_members(query: str):
    # 'query' is query parameters because that is NOT in the path string "/api/search_members"
    # Search for members that contain the query string (case-insensitive)
    results = [member for member in members if query.lower() in member.lower()]
    return {"results": results}
