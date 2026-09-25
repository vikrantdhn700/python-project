# Python + Neo4j CRUD Project

This project demonstrates Python-to-Neo4j connectivity and all required graph operations using Neo4j AuraDB.

The graph is created and modified programmatically. No manual graph creation through the Neo4j UI is required.

## Operations

1. Create Node
2. Create Relationship
3. Read Nodes
4. Search / Filter
5. Update Properties
6. Delete Relationship
7. Delete Node

## Project Structure

```text
python-neo4j-crud-project/
├── app/
│   ├── __init__.py
│   ├── database.py
│   └── main.py
├── .env.example
├── .gitignore
├── README.md
├── SETUP.md
└── requirements.txt
```

## Setup

Create and activate the virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install packages:

```powershell
python -m pip install -r requirements.txt
```

Create `.env` from `.env.example` and add the Neo4j Aura credentials.

Example:

```env
NEO4J_URI=neo4j+s://your-instance.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your-password
NEO4J_DATABASE=neo4j
```

Never commit `.env`.

## Run

```powershell
python -m app.main
```

Expected successful ending:

```text
Neo4j connection successful!
...
All Neo4j operations completed successfully.
```

## Parameterized Cypher

The project uses parameters instead of string concatenation.

Example:

```python
query = """
CREATE (s:Student {
    name: $name,
    age: $age,
    city: $city
})
RETURN s
"""

records, _, _ = driver.execute_query(
    query,
    name=name,
    age=age,
    city=city,
    database_=self.database,
)
```

## Cypher Operations

### Create Node

```cypher
CREATE (s:Student {
    name: $name,
    age: $age,
    city: $city
})
RETURN s
```

### Create Relationship

```cypher
MATCH (s1:Student {name: $student1_name})
MATCH (s2:Student {name: $student2_name})
CREATE (s1)-[r:FRIEND_OF]->(s2)
RETURN s1, r, s2
```

### Read Nodes

```cypher
MATCH (s:Student)
RETURN s
ORDER BY s.name
```

### Search / Filter

```cypher
MATCH (s:Student)
WHERE ($city IS NULL OR s.city = $city)
  AND ($min_age IS NULL OR s.age >= $min_age)
RETURN s
```

### Update Properties

```cypher
MATCH (s:Student {name: $name})
SET s.age = coalesce($age, s.age),
    s.city = coalesce($city, s.city)
RETURN s
```

### Delete Relationship

```cypher
MATCH (s1:Student {name: $student1_name})
      -[r:FRIEND_OF]->
      (s2:Student {name: $student2_name})
DELETE r
RETURN count(r)
```

### Delete Node

```cypher
MATCH (s:Student {name: $name})
DETACH DELETE s
RETURN count(s)
```

## Execution Results

A successful execution will show:

```text
Neo4j connection successful!

1. CREATE NODES
...

2. CREATE RELATIONSHIPS
...

3. READ ALL STUDENTS
...

4. SEARCH / FILTER
...

5. UPDATE STUDENT
...

6. DELETE RELATIONSHIP
Deleted relationships: 1

7. DELETE NODE
Deleted nodes: 1

All Neo4j operations completed successfully.
```

The exact Neo4j element IDs may differ between executions.

## GitHub Submission

```powershell
git init
git add .
git commit -m "Implement Python Neo4j CRUD operations"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/python-neo4j-crud-project.git
git push -u origin main
```

Before pushing, verify that `.env` and `venv/` are not included.

## Security

Never commit:

- `.env`
- `venv/`
- Neo4j passwords
- API keys
- other secrets
