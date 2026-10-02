// Supply-chain graph traversal assignment: 12+ queries

// Q1 Single-hop
MATCH (s:Supplier)-[:SUPPLIES]->(c:Component {name: 'Component X'})
RETURN s.name AS supplier;

// Q2 Single-hop
MATCH (s:Supplier {name: 'Supplier A'})-[:SUPPLIES]->(c:Component)
RETURN c.name AS component;

// Q3 Multi-hop
MATCH (s:Supplier {name: 'Supplier A'})-[:SUPPLIES]->(:Component)-[:USED_IN]->(p:Product)
RETURN DISTINCT p.name AS product ORDER BY product;

// Q4 Supplier -> Component -> Product -> Plant
MATCH (s:Supplier {name: 'Supplier A'})-[:SUPPLIES]->(:Component)-[:USED_IN]->(p:Product)-[:MANUFACTURED_AT]->(pl:Plant)
RETURN DISTINCT p.name AS product, pl.name AS plant ORDER BY product, plant;

// Q5 Property filtering
MATCH (s:Supplier)-[:SUPPLIES]->(c:Component {criticality: 'High'})
RETURN s.name AS supplier, c.name AS component;

// Q6 Relationship direction
MATCH (s:Supplier)-[:LOCATED_IN]->(country:Country {name: 'China'})
RETURN s.name AS supplier, country.name AS country;

// Q7 Reverse direction
MATCH (p:Product)<-[:USED_IN]-(c:Component {name: 'Component Z'})
RETURN p.name AS product;

// Q8 Aggregation/counting
MATCH (s:Supplier)-[:SUPPLIES]->(:Component)-[:USED_IN]->(p:Product)
RETURN s.name AS supplier, count(DISTINCT p) AS product_count
ORDER BY product_count DESC, supplier;

// Q9 Aggregation by country
MATCH (s:Supplier)-[:LOCATED_IN]->(country:Country), (s)-[:SUPPLIES]->(c:Component)
RETURN country.name AS country, count(DISTINCT c) AS component_count
ORDER BY component_count DESC;

// Q10 Path query
MATCH path = (s:Supplier {name: 'Supplier B'})-[:SUPPLIES]->(:Component)-[:USED_IN]->(:Product)-[:MANUFACTURED_AT]->(pl:Plant {name: 'Chennai Plant'})
RETURN [n IN nodes(path) | coalesce(n.name, toString(n.id))] AS path, length(path) AS hops;

// Q11 Variable-length Tier-2 traversal
MATCH path = (s:Supplier {name: 'Supplier B'})-[:SUPPLIES_SUPPLIER*1..3]->(target:Supplier)
RETURN [n IN nodes(path) | n.name] AS supplier_chain, length(path) AS hops;

// Q12 Variable-length dependency traversal
MATCH path = (s:Supplier {name: 'Supplier B'})-[:SUPPLIES|SUPPLIES_SUPPLIER|USED_IN|MANUFACTURED_AT*1..6]->(target:Plant)
RETURN DISTINCT target.name AS plant, length(path) AS hops
ORDER BY hops, plant;

// Q13 Components with multiple suppliers
MATCH (c:Component)<-[:SUPPLIES]-(s:Supplier)
WITH c, count(DISTINCT s) AS supplier_count
WHERE supplier_count > 1
RETURN c.name AS component, supplier_count;

// Q14 Supplier -> Component -> Product dependency details
MATCH (s:Supplier {name: 'Supplier B'})-[:SUPPLIES]->(c:Component)-[:USED_IN]->(p:Product)
RETURN DISTINCT s.name AS supplier, c.name AS component, p.name AS product;

// Q15 Component -> Product -> Plant
MATCH (c:Component {name: 'Component X'})-[:USED_IN]->(p:Product)-[:MANUFACTURED_AT]->(pl:Plant)
RETURN DISTINCT c.name AS component, p.name AS product, pl.name AS plant;
