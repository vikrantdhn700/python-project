// Products depending on Supplier A
MATCH (s:Supplier {name:'Supplier A'})-[:SUPPLIES]->(c:Component)-[:USED_IN]->(p:Product)
RETURN DISTINCT s.name AS supplier,c.name AS component,p.name AS product ORDER BY product,component;

// Plants affected if Component X is unavailable
MATCH (c:Component {name:'Component X'})-[:USED_IN]->(p:Product)-[:MANUFACTURED_AT]->(plant:Plant)
RETURN DISTINCT c.name AS component,p.name AS product,plant.name AS affected_plant ORDER BY affected_plant,product;

// Suppliers connected to Product Beta
MATCH (s:Supplier)-[:SUPPLIES]->(c:Component)-[:USED_IN]->(p:Product {name:'Product Beta'})
RETURN DISTINCT s.name AS supplier,c.name AS component,p.name AS product ORDER BY supplier,component;

// Tier-2 Supplier B to plant
MATCH (s:Supplier {name:'Supplier B'})-[:SUPPLIES_SUPPLIER]->(tier1:Supplier)-[:SUPPLIES]->(c:Component)-[:USED_IN]->(p:Product)-[:MANUFACTURED_AT]->(plant:Plant)
RETURN s.name AS tier2_supplier,tier1.name AS tier1_supplier,c.name AS component,p.name AS product,plant.name AS plant ORDER BY plant,product,component;

// Components supplied by suppliers from China and their products
MATCH (s:Supplier)-[:LOCATED_IN]->(country:Country {name:'China'}),(s)-[:SUPPLIES]->(c:Component)-[:USED_IN]->(p:Product)
RETURN DISTINCT country.name AS country,s.name AS supplier,c.name AS component,p.name AS product ORDER BY supplier,component,product;

// Components with multiple suppliers
MATCH (s:Supplier)-[:SUPPLIES]->(c:Component)
WITH c,count(DISTINCT s) AS supplier_count WHERE supplier_count > 1
RETURN c.name AS component,supplier_count ORDER BY supplier_count DESC,component;

// Single-supplier components
MATCH (s:Supplier)-[:SUPPLIES]->(c:Component)
WITH c,collect(DISTINCT s.name) AS suppliers WHERE size(suppliers)=1
RETURN c.name AS component,suppliers ORDER BY component;

// Shipment destinations
MATCH (shipment:Shipment)-[:CONTAINS]->(component:Component),(shipment)-[:DESTINED_FOR]->(plant:Plant)
RETURN shipment.id AS shipment,component.name AS component,plant.name AS destination ORDER BY shipment;

// Shortest path from Tier-2 Supplier B to Plant Chennai
MATCH (s:Supplier {name:'Supplier B'}),(plant:Plant {name:'Plant Chennai'})
MATCH path=shortestPath((s)-[*]-(plant)) RETURN path;

// Visualize complete graph
MATCH (n)-[r]->(m) RETURN n,r,m LIMIT 100;
