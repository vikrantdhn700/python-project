# Mini Supply-Chain Risk Graph

A Python + Neo4j learning project for supplier-risk and dependency analysis.

## Business problem
A supply chain can contain Tier-1 and Tier-2 suppliers, components, products, plants, shipments and supplier countries. The important questions are often multi-hop: which products depend on a supplier, which plants depend on a component, how a Tier-2 supplier reaches a plant, and which products use components sourced from a particular country.

## Graph model
Nodes: Supplier, Component, Product, Plant, Shipment, Country.

Relationships:
- Supplier -> SUPPLIES -> Component
- Component -> USED_IN -> Product
- Product -> MANUFACTURED_AT -> Plant
- Supplier -> LOCATED_IN -> Country
- Shipment -> CONTAINS -> Component
- Shipment -> DESTINED_FOR -> Plant
- Supplier -> SUPPLIES_SUPPLIER -> Supplier (Tier-2)

## Project structure
- `app/main.py` runs the full demo.
- `app/graph_manager.py` contains Neo4j connection, graph creation and analysis methods.
- `cypher/01_constraints.cypher` contains constraints.
- `cypher/02_create_graph.cypher` contains the complete sample graph.
- `cypher/03_queries.cypher` contains the analysis queries.
- `.env.example` contains connection settings.
- `requirements.txt` contains Python dependencies.

## Run
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `.env` with your Neo4j AuraDB or local Neo4j credentials, then:

```powershell
python app/main.py
```

## Main traversal patterns

Supplier A -> Component -> Product answers product dependency.

Component X -> Product -> Plant answers potential plant impact.

Supplier B -> Supplier A -> Component -> Product -> Plant answers a Tier-2 dependency path.

Country -> Supplier -> Component -> Product answers country-based sourcing analysis.

## Sample expected results

Supplier A connects to Product Alpha, Product Beta and Product Gamma.

Component X can affect Plant Delhi, Plant Pune and Plant Chennai through Product Alpha and Product Beta.

Product Beta is connected to Supplier A, Supplier B and Supplier D.

Supplier B is a Tier-2 supplier to Supplier A.

Supplier B is located in China and supplies Component X and Component Z.

Component W has only one supplier in the sample data: Supplier C.

## Neo4j Browser visualization
After running the application, use:

```cypher
MATCH (n)-[r]->(m)
RETURN n,r,m
LIMIT 100;
```

The sample data is fictional and is intended for learning/demo purposes.
