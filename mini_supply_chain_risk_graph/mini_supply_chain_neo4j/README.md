# Mini Supply-Chain Risk Graph

A small Python + Neo4j project that models supplier dependencies and performs supply-chain risk analysis.

## Business Problem

A company may depend on multiple suppliers, components, products, manufacturing plants, and shipments.

The difficult questions are usually multi-hop questions:

- Which products depend on Supplier A?
- Which plants could be affected if Component X becomes unavailable?
- Which suppliers are connected to Product Beta?
- How is a Tier-2 supplier connected to a manufacturing plant?
- Which components supplied by suppliers from China are used in which products?
- Which components have multiple suppliers?
- Which components have only one supplier?

Neo4j is a good fit because these questions require relationship traversal.

## Graph Model

### Nodes

- Supplier
- Component
- Product
- Plant
- Shipment
- Country

### Relationships

```text
(Supplier)-[:SUPPLIES]->(Component)
(Component)-[:USED_IN]->(Product)
(Product)-[:MANUFACTURED_AT]->(Plant)
(Supplier)-[:LOCATED_IN]->(Country)
(Shipment)-[:CONTAINS]->(Component)
(Shipment)-[:DESTINED_FOR]->(Plant)
(Supplier)-[:SUPPLIES_SUPPLIER]->(Supplier)
```

The last relationship represents the Tier-2 supplier relationship.

Example:

```text
Supplier B
    |
    | SUPPLIES_SUPPLIER
    v
Supplier A
    |
    | SUPPLIES
    v
Component X
    |
    | USED_IN
    v
Product Alpha
    |
    | MANUFACTURED_AT
    v
Plant Delhi
```

## Project Structure

```text
mini_supply_chain_neo4j/
|
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── graph_manager.py
|
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10+
- Neo4j AuraDB or local Neo4j
- Internet connection if using Neo4j AuraDB

## 1. Create a Virtual Environment

Windows PowerShell:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

Alternative without changing PowerShell policy:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

## 3. Configure Neo4j

Copy:

```text
.env.example
```

to:

```text
.env
```

PowerShell:

```powershell
Copy-Item .env.example .env
```

Then edit `.env`.

For Neo4j AuraDB:

```env
NEO4J_URI=neo4j+s://YOUR_INSTANCE.databases.neo4j.io
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=YOUR_PASSWORD
NEO4J_DATABASE=neo4j
```

For local Neo4j:

```env
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=YOUR_PASSWORD
NEO4J_DATABASE=neo4j
```

Do not commit `.env` to GitHub.

## 4. Run the Project

From the project root:

```powershell
python app/main.py
```

You should see sections such as:

```text
======================================================================
1. Creating constraints
======================================================================
Constraints created.

======================================================================
2. Creating supply-chain graph
======================================================================
Sample graph created.
```

Then the program executes the supply-chain queries.

## 5. Main Queries

### Products depending on Supplier A

```cypher
MATCH (s:Supplier {name: "Supplier A"})
      -[:SUPPLIES]->(c:Component)
      -[:USED_IN]->(p:Product)
RETURN DISTINCT
    s.name AS supplier,
    c.name AS component,
    p.name AS product;
```

### Plants affected by Component X

```cypher
MATCH (c:Component {name: "Component X"})
      -[:USED_IN]->(p:Product)
      -[:MANUFACTURED_AT]->(plant:Plant)
RETURN DISTINCT
    c.name AS component,
    p.name AS product,
    plant.name AS affected_plant;
```

### Suppliers connected to Product Beta

```cypher
MATCH (s:Supplier)
      -[:SUPPLIES]->(c:Component)
      -[:USED_IN]->(p:Product {name: "Product Beta"})
RETURN DISTINCT
    s.name AS supplier,
    c.name AS component,
    p.name AS product;
```

### Tier-2 supplier to plant

```cypher
MATCH (s:Supplier {name: "Supplier B"})
      -[:SUPPLIES_SUPPLIER]->(tier1:Supplier)
      -[:SUPPLIES]->(c:Component)
      -[:USED_IN]->(p:Product)
      -[:MANUFACTURED_AT]->(plant:Plant)
RETURN
    s.name AS tier2_supplier,
    tier1.name AS tier1_supplier,
    c.name AS component,
    p.name AS product,
    plant.name AS plant;
```

### Components from a particular country

```cypher
MATCH (s:Supplier)-[:LOCATED_IN]->(country:Country {name: "China"}),
      (s)-[:SUPPLIES]->(c:Component)
      -[:USED_IN]->(p:Product)
RETURN DISTINCT
    country.name AS country,
    s.name AS supplier,
    c.name AS component,
    p.name AS product;
```

## Expected Sample Data

### Suppliers

```text
Supplier A -> India
Supplier B -> China
Supplier C -> Germany
Supplier D -> India
```

### Supplier components

```text
Supplier A -> Component X
Supplier A -> Component Y

Supplier B -> Component X
Supplier B -> Component Z

Supplier C -> Component Y
Supplier C -> Component W

Supplier D -> Component Z
```

### Component products

```text
Component X -> Product Alpha
Component X -> Product Beta

Component Y -> Product Alpha
Component Y -> Product Gamma

Component Z -> Product Beta
Component Z -> Product Gamma

Component W -> Product Gamma
```

### Products and plants

```text
Product Alpha -> Plant Delhi
Product Alpha -> Plant Pune

Product Beta -> Plant Pune
Product Beta -> Plant Chennai

Product Gamma -> Plant Chennai
```

### Tier-2 dependency

```text
Supplier B
    |
    | SUPPLIES_SUPPLIER
    v
Supplier A
```

## Expected Analysis

### Supplier A

Supplier A supplies:

```text
Component X
Component Y
```

These components are used in:

```text
Product Alpha
Product Beta
Product Gamma
```

Therefore Supplier A has downstream connections to:

```text
Plant Delhi
Plant Pune
Plant Chennai
```

### Component X outage

Component X is used by:

```text
Product Alpha
Product Beta
```

Those products are manufactured at:

```text
Plant Delhi
Plant Pune
Plant Chennai
```

Therefore all three plants have a potential dependency on Component X.

### Supplier B

Supplier B is located in China and supplies:

```text
Component X
Component Z
```

These are used in:

```text
Product Alpha
Product Beta
Product Gamma
```

Supplier B also supplies Supplier A, creating a Tier-2 relationship.

## Neo4j Browser Visualization

After running the Python program, open Neo4j Browser and run:

```cypher
MATCH (n)-[r]->(m)
RETURN n, r, m
LIMIT 100;
```

This displays the graph visually.

You can also inspect Supplier B's downstream dependency:

```cypher
MATCH path =
(s:Supplier {name: "Supplier B"})
-[:SUPPLIES_SUPPLIER]->
(tier1:Supplier)
-[:SUPPLIES]->
(c:Component)
-[:USED_IN]->
(p:Product)
-[:MANUFACTURED_AT]->
(plant:Plant)
RETURN path;
```

## Important Note

The sample graph is synthetic and is intended for learning Neo4j graph modeling, traversal, and supply-chain risk analysis. It does not represent a real company's supply chain.

## Learning Outcomes

This project demonstrates:

- Neo4j connection from Python
- Graph creation using Cypher
- Nodes and relationships
- Relationship direction
- Parameterized Cypher
- Multi-hop traversal
- Tier-2 supplier relationships
- Supply-chain dependency analysis
- Impact analysis
- Shortest-path traversal
- Aggregation with `count`
- Filtering with `WHERE`
- `DISTINCT`
- Graph visualization in Neo4j Browser
