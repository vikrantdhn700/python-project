# Learning Platform Graph with Neo4j

A Python + Neo4j project that models a learning platform using a graph database.

The graph represents relationships between **Students, Courses, Mentors, Skills, Projects, and Companies**.

The project demonstrates:

- Creating nodes
- Creating relationships
- Reading graph data
- Searching/filtering graph data
- Updating node properties
- Deleting relationships
- Deleting nodes
- Using Cypher parameters
- Connecting Python to Neo4j
- Visualizing the resulting graph in Neo4j Browser

---

## 1. Project Structure

```text
learning-platform-neo4j/
│
├── app/
│   ├── __init__.py
│   └── graph.py
│
├── docs/
│   ├── GRAPH_EXPLANATION.md
│   └── EXPECTED_OUTPUT.md
│
├── .env.example
├── .gitignore
├── cypher_queries.cypher
├── main.py
├── README.md
└── requirements.txt
```

---

# 2. Technologies Used

- Python 3.10+
- Neo4j
- Cypher Query Language
- Neo4j Python Driver
- python-dotenv

---

# 3. Graph Model

The learning platform contains six types of nodes.

```text
Student
Course
Mentor
Skill
Project
Company
```

The relationships are:

```text
(Student)-[:ENROLLED_IN]->(Course)

(Mentor)-[:TEACHES]->(Course)

(Course)-[:TEACHES_SKILL]->(Skill)

(Student)-[:BUILT]->(Project)

(Project)-[:USES]->(Skill)

(Student)-[:INTERESTED_IN]->(Company)
```

---

# 4. Nodes

## Student

Represents a learner on the platform.

Example:

```text
Student
{
    id: "S1",
    name: "Aarav",
    city: "Delhi"
}
```

---

## Course

Represents a course available on the learning platform.

Example:

```text
Course
{
    id: "C1",
    title: "Python Backend"
}
```

---

## Mentor

Represents a mentor who teaches courses.

Example:

```text
Mentor
{
    id: "M1",
    name: "Anita Sharma"
}
```

---

## Skill

Represents a technical skill.

Example:

```text
Skill
{
    id: "SK1",
    name: "Python"
}
```

---

## Project

Represents a project built by a student.

Example:

```text
Project
{
    id: "P1",
    name: "Support Ticket API"
}
```

---

## Company

Represents a company that a student is interested in.

Example:

```text
Company
{
    id: "CO1",
    name: "TechNova"
}
```

---

# 5. Relationships

## Student → Course

```cypher
(Student)-[:ENROLLED_IN]->(Course)
```

Represents the courses in which a student is enrolled.

Example:

```text
Aarav ──ENROLLED_IN──> Python Backend
```

---

## Mentor → Course

```cypher
(Mentor)-[:TEACHES]->(Course)
```

Represents the courses taught by a mentor.

Example:

```text
Anita Sharma ──TEACHES──> Python Backend
```

---

## Course → Skill

```cypher
(Course)-[:TEACHES_SKILL]->(Skill)
```

Represents the skills taught by a course.

Example:

```text
Python Backend ──TEACHES_SKILL──> Python
```

---

## Student → Project

```cypher
(Student)-[:BUILT]->(Project)
```

Represents projects created by students.

Example:

```text
Aarav ──BUILT──> Support Ticket API
```

---

## Project → Skill

```cypher
(Project)-[:USES]->(Skill)
```

Represents skills or technologies used by a project.

Example:

```text
Support Ticket API ──USES──> FastAPI
```

---

## Student → Company

```cypher
(Student)-[:INTERESTED_IN]->(Company)
```

Represents companies in which students are interested.

Example:

```text
Aarav ──INTERESTED_IN──> TechNova
```

---

# 6. Graph Size

The seed data creates more than the required minimum.

```text
Students   : 4
Courses    : 4
Mentors    : 3
Skills     : 5
Projects   : 3
Companies  : 2
--------------------------------
Total Nodes: 21
```

Relationships:

```text
ENROLLED_IN       : 8
TEACHES           : 4
TEACHES_SKILL     : 7
BUILT             : 4
USES              : 8
INTERESTED_IN     : 4
--------------------------------
Total Relationships: 35
```

Therefore, the project satisfies the requirement of:

```text
At least 20 nodes
At least 25 relationships
```

---

# 7. Prerequisites

Install the following:

- Python 3.10 or newer
- Neo4j Desktop, Neo4j Server, or Neo4j Aura

Check Python:

```bash
python --version
```

---

# 8. Create Python Virtual Environment

Windows:

```powershell
python -m venv venv
```

Activate:

```powershell
.\venv\Scripts\activate
```

---

# 9. Install Dependencies

Run:

```powershell
pip install -r requirements.txt
```

The project uses:

```text
neo4j
python-dotenv
```

---

# 10. Configure Neo4j

Copy:

```text
.env.example
```

to:

```text
.env
```

Example:

```env
NEO4J_URI=neo4j://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=your_password
NEO4J_DATABASE=neo4j
```

Replace:

```text
your_password
```

with your actual Neo4j password.

### Important

Do not commit `.env` to GitHub.

The `.gitignore` file already contains:

```text
.env
```

---

# 11. Run the Project

Start Neo4j first.

Then run:

```powershell
python main.py
```

The program will:

1. Connect to Neo4j
2. Remove previous demo data
3. Create nodes
4. Create relationships
5. Read graph data
6. Update a student
7. Delete a relationship
8. Delete a project
9. Display the final graph

---

# 12. CRUD Operations

## CREATE

The Python application creates nodes using Cypher.

Example:

```python
query = f"""
CREATE (n:{label} $props)
"""
```

Properties are passed separately as parameters.

Relationships are created using:

```cypher
MATCH (a {id: $start_id, demo: true})
MATCH (b {id: $end_id, demo: true})
CREATE (a)-[:ENROLLED_IN]->(b)
```

---

# 13. READ

The project reads all relationships:

```cypher
MATCH (a)-[r]->(b)
WHERE a.demo = true
  AND b.demo = true
RETURN a, r, b
```

It also demonstrates specific searches.

Example:

```cypher
MATCH (s:Student)
      -[:ENROLLED_IN]->
      (c:Course)
      -[:TEACHES_SKILL]->
      (skill:Skill)

WHERE skill.name = "Python"

RETURN s, c, skill;
```

This finds students who are enrolled in courses that teach Python.

---

# 14. UPDATE

The project updates a student's city.

```cypher
MATCH (s:Student {
    id: $student_id
})

SET s.city = $city

RETURN s;
```

Python passes the values separately:

```python
session.run(
    query,
    student_id="S1",
    city="Hyderabad"
)
```

---

# 15. DELETE Relationship

The project demonstrates deleting a relationship without deleting either node.

```cypher
MATCH (
    s:Student {
        id: $student_id
    }
)-[r:INTERESTED_IN]->(
    c:Company {
        id: $company_id
    })

DELETE r;
```

The Student and Company remain in the graph.

Only their relationship is removed.

---

# 16. DELETE Node

The project also demonstrates deleting a node.

```cypher
MATCH (p:Project {
    id: $project_id
})

DETACH DELETE p;
```

`DETACH DELETE` removes the node and its connected relationships.

---

# 17. Cypher Parameters

The project uses parameters instead of directly inserting values into Cypher queries.

Example:

```cypher
MATCH (s:Student {
    id: $student_id
})

SET s.city = $city

RETURN s;
```

Python:

```python
session.run(
    query,
    student_id="S1",
    city="Hyderabad"
)
```

This keeps query structure separate from data values.

---

# 18. Graph Visualization

After running the Python program, open **Neo4j Browser**.

Run:

```cypher
MATCH (n)-[r]->(m)
WHERE n.demo = true
  AND m.demo = true
RETURN n, r, m;
```

Neo4j Browser will display the graph visually.

You will see nodes such as:

```text
Student
Course
Mentor
Skill
Project
Company
```

and relationships such as:

```text
ENROLLED_IN
TEACHES
TEACHES_SKILL
BUILT
USES
INTERESTED_IN
```

---

# 19. Example Graph

The conceptual graph looks like:

```text
                         ┌─────────────┐
                         │   Mentor    │
                         └──────┬──────┘
                                │
                             TEACHES
                                │
                                ▼
┌──────────┐             ┌─────────────┐
│ Student  │────────────►│   Course    │
└────┬─────┘ ENROLLED_IN └──────┬──────┘
     │                          │
     │ BUILT                    │
     │                          │ TEACHES_SKILL
     ▼                          ▼
┌──────────┐                ┌─────────┐
│ Project  │──────USES─────►│  Skill  │
└──────────┘                └─────────┘
     │
     │
     │
     ▼
 Student ─────INTERESTED_IN────► Company
```

---

# 20. Useful Cypher Queries

## Show all students

```cypher
MATCH (s:Student)
RETURN s;
```

## Show all courses

```cypher
MATCH (c:Course)
RETURN c;
```

## Show student enrollments

```cypher
MATCH (s:Student)-[r:ENROLLED_IN]->(c:Course)
RETURN s, r, c;
```

## Show mentors and courses

```cypher
MATCH (m:Mentor)-[r:TEACHES]->(c:Course)
RETURN m, r, c;
```

## Show courses and skills

```cypher
MATCH (c:Course)-[r:TEACHES_SKILL]->(s:Skill)
RETURN c, r, s;
```

## Show projects and skills

```cypher
MATCH (p:Project)-[r:USES]->(s:Skill)
RETURN p, r, s;
```

## Show students and companies

```cypher
MATCH (s:Student)-[r:INTERESTED_IN]->(c:Company)
RETURN s, r, c;
```

## Count nodes

```cypher
MATCH (n)
WHERE n.demo = true
RETURN count(n) AS total_nodes;
```

## Count relationships

```cypher
MATCH (a)-[r]->(b)
WHERE a.demo = true
  AND b.demo = true
RETURN count(r) AS total_relationships;
```

---

# 21. Learning Outcomes

After completing this project, you should understand:

- What a graph database is
- What a Neo4j node is
- What labels are
- What node properties are
- What relationships are
- How relationship direction works
- How Cypher works
- How to create nodes using Python
- How to create relationships using Python
- How to read graph data
- How to filter graph data
- How to update graph data
- How to delete relationships
- How to delete nodes
- How to use Cypher parameters
- How to visualize a graph in Neo4j Browser

---

# 22. Assignment Requirements Checklist

| Requirement               | Status           |
| ------------------------- | ---------------- |
| Create Student nodes      | Done             |
| Create Course nodes       | Done             |
| Create Mentor nodes       | Done             |
| Create Skill nodes        | Done             |
| Create Project nodes      | Done             |
| Create Company nodes      | Done             |
| Student → Course          | Done             |
| Mentor → Course           | Done             |
| Course → Skill            | Done             |
| Student → Project         | Done             |
| Project → Skill           | Done             |
| Student → Company         | Done             |
| At least 20 nodes         | 21 nodes         |
| At least 25 relationships | 35 relationships |
| Create operation          | Done             |
| Read operation            | Done             |
| Update operation          | Done             |
| Delete relationship       | Done             |
| Delete node               | Done             |
| Parameterized Cypher      | Done             |
| Graph visualization       | Done             |
| Node explanation          | Done             |
| Label explanation         | Done             |
| Property explanation      | Done             |
| Relationship explanation  | Done             |
| Direction explanation     | Done             |

---

# 23. Git Commands

Initialize Git:

```powershell
git init
```

Add files:

```powershell
git add .
```

Commit:

```powershell
git commit -m "Create Neo4j learning platform graph"
```

Add remote:

```powershell
git remote add origin YOUR_GITHUB_REPOSITORY_URL
```

Push:

```powershell
git branch -M main
git push -u origin main
```

Make sure `.env` is not included in the repository.

---

# 24. Project Summary

This project demonstrates how a learning platform can be represented as a graph.

Instead of storing only isolated records, Neo4j stores meaningful connections between learners, courses, mentors, skills, projects, and companies.

For example:

```text
Student
   ↓
ENROLLED_IN
   ↓
Course
   ↓
TEACHES_SKILL
   ↓
Skill
```

and:

```text
Student
   ↓
BUILT
   ↓
Project
   ↓
USES
   ↓
Skill
```

These relationships make it possible to answer graph-oriented questions such as:

- Which courses teach Python?
- Which students are learning Python?
- Which projects use Neo4j?
- Which mentor teaches a particular course?
- Which companies are students interested in?
- Which skills are connected to a student's projects?

This demonstrates the core concepts of **Neo4j, graph modeling, Cypher, relationships, and Python integration**.
