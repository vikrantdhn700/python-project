# Neo4j Graph Traversal - Supply Chain Risk

## Objective
Focus specifically on graph traversal using the supply-chain graph from the earlier task. This project contains 15 Cypher examples covering single-hop, multi-hop, property filtering, relationship direction, reverse traversal, aggregation/counting, path queries, and variable-length traversal.

## Core traversal
```text
Supplier
   ↓ SUPPLIES
Component
   ↓ USED_IN
Product
   ↓ MANUFACTURED_AT
Plant
```

## Graph model
Nodes: Supplier, Component, Product, Plant, Country, Shipment.

Relationships:
```text
(Supplier)-[:SUPPLIES]->(Component)
(Component)-[:USED_IN]->(Product)
(Product)-[:MANUFACTURED_AT]->(Plant)
(Supplier)-[:LOCATED_IN]->(Country)
(Shipment)-[:CONTAINS]->(Component)
(Shipment)-[:DESTINED_FOR]->(Plant)
(Supplier)-[:SUPPLIES_SUPPLIER]->(Supplier)
```

## Sample data
Countries: India, China, Germany.
Suppliers: A, B, C, D.
Components: X, Y, Z, W.
Products: Alpha, Beta, Gamma.
Plants: Delhi, Pune, Chennai.

Important dependencies:
- A supplies X and Y.
- B supplies X and Z.
- C supplies Y and W.
- D supplies Z.
- X is used in Alpha and Beta.
- Y is used in Alpha and Gamma.
- Z is used in Beta and Gamma.
- W is used in Gamma.
- Alpha is manufactured at Delhi and Pune.
- Beta is manufactured at Pune and Chennai.
- Gamma is manufactured at Chennai.
- B supplies A as a Tier-2 relationship.

## Setup
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks activation:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Copy `.env.example` to `.env` and set your Neo4j credentials.

## Run
Use module mode from the project root:
```powershell
python -m app.main
```

`app/main.py` intentionally uses:
```python
from .graph_manager import SupplyChainGraph
```
so the package import works correctly with `python -m app.main`.

## Query file
Open `traversal_queries.cypher` in Neo4j Browser to run the queries individually.

## Traversal examples

### 1. Single-hop
```cypher
MATCH (s:Supplier)-[:SUPPLIES]->(c:Component {name: 'Component X'})
RETURN s.name AS supplier;
```

### 2. Multi-hop
```cypher
MATCH (s:Supplier {name: 'Supplier A'})-[:SUPPLIES]->(:Component)-[:USED_IN]->(p:Product)
RETURN DISTINCT p.name AS product;
```

### 3. Supplier -> Component -> Product -> Plant
```cypher
MATCH (s:Supplier {name: 'Supplier A'})-[:SUPPLIES]->(:Component)-[:USED_IN]->(p:Product)-[:MANUFACTURED_AT]->(pl:Plant)
RETURN DISTINCT p.name AS product, pl.name AS plant;
```

### 4. Property filtering
```cypher
MATCH (s:Supplier)-[:SUPPLIES]->(c:Component {criticality: 'High'})
RETURN s.name AS supplier, c.name AS component;
```

### 5. Direction / reverse direction
```cypher
MATCH (s:Supplier)-[:LOCATED_IN]->(country:Country {name: 'China'})
RETURN s.name AS supplier;

MATCH (p:Product)<-[:USED_IN]-(c:Component {name: 'Component Z'})
RETURN p.name AS product;
```

### 6. Aggregation
```cypher
MATCH (s:Supplier)-[:SUPPLIES]->(:Component)-[:USED_IN]->(p:Product)
RETURN s.name AS supplier, count(DISTINCT p) AS product_count;
```

### 7. Path query
```cypher
MATCH path = (s:Supplier {name: 'Supplier B'})-[:SUPPLIES]->(:Component)-[:USED_IN]->(:Product)-[:MANUFACTURED_AT]->(pl:Plant {name: 'Chennai Plant'})
RETURN [n IN nodes(path) | coalesce(n.name, toString(n.id))] AS path, length(path) AS hops;
```

### 8. Variable-length traversal
```cypher
MATCH path = (s:Supplier {name: 'Supplier B'})-[:SUPPLIES_SUPPLIER*1..3]->(target:Supplier)
RETURN [n IN nodes(path) | n.name] AS supplier_chain, length(path) AS hops;
```

## Why graph traversal feels different from tables

In a relational design, a connected question is often expressed as a sequence of joins across relationship tables. The developer has to think about foreign keys, join conditions, intermediate tables, duplicate rows, and the order of joins.

In a graph, the relationships are first-class elements of the model. A question such as "Which plants depend on Supplier A?" can be written directly as the connected pattern:

```text
Supplier -> Component -> Product -> Plant
```

The important difference is the mental model: instead of starting with tables and deciding how to join them, graph traversal starts with the entities and the relationship path connecting them. This is particularly useful for dependency analysis, supply-chain risk, network analysis, recommendations, and other connected-data questions.

## Assignment checklist
- [x] At least 10 Cypher queries
- [x] Single-hop relationships
- [x] Multi-hop relationships
- [x] Property filtering
- [x] Relationship-direction queries
- [x] Aggregation/counting
- [x] Path queries
- [x] Variable-length traversal
- [x] Supplier -> Component -> Product -> Plant traversal
- [x] Business explanation
- [x] Graph vs. table/join explanation
