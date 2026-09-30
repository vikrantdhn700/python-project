CREATE (:Country {name:'India'}), (:Country {name:'China'}), (:Country {name:'Germany'});
CREATE (:Supplier {name:'Supplier A'}), (:Supplier {name:'Supplier B'}), (:Supplier {name:'Supplier C'}), (:Supplier {name:'Supplier D'});
CREATE (:Component {name:'Component X'}), (:Component {name:'Component Y'}), (:Component {name:'Component Z'}), (:Component {name:'Component W'});
CREATE (:Product {name:'Product Alpha'}), (:Product {name:'Product Beta'}), (:Product {name:'Product Gamma'});
CREATE (:Plant {name:'Plant Delhi'}), (:Plant {name:'Plant Pune'}), (:Plant {name:'Plant Chennai'});
CREATE (:Shipment {id:'Shipment 101'}), (:Shipment {id:'Shipment 102'}), (:Shipment {id:'Shipment 103'});

MATCH (a:Supplier {name:'Supplier A'}),(b:Supplier {name:'Supplier B'}),(c:Supplier {name:'Supplier C'}),(d:Supplier {name:'Supplier D'}),
      (india:Country {name:'India'}),(china:Country {name:'China'}),(germany:Country {name:'Germany'})
CREATE (a)-[:LOCATED_IN]->(india),(b)-[:LOCATED_IN]->(china),(c)-[:LOCATED_IN]->(germany),(d)-[:LOCATED_IN]->(india);

MATCH (a:Supplier {name:'Supplier A'}),(b:Supplier {name:'Supplier B'}),(c:Supplier {name:'Supplier C'}),(d:Supplier {name:'Supplier D'}),
      (x:Component {name:'Component X'}),(y:Component {name:'Component Y'}),(z:Component {name:'Component Z'}),(w:Component {name:'Component W'})
CREATE (a)-[:SUPPLIES]->(x),(a)-[:SUPPLIES]->(y),(b)-[:SUPPLIES]->(x),(b)-[:SUPPLIES]->(z),(c)-[:SUPPLIES]->(y),(c)-[:SUPPLIES]->(w),(d)-[:SUPPLIES]->(z);

MATCH (x:Component {name:'Component X'}),(y:Component {name:'Component Y'}),(z:Component {name:'Component Z'}),(w:Component {name:'Component W'}),
      (a:Product {name:'Product Alpha'}),(b:Product {name:'Product Beta'}),(g:Product {name:'Product Gamma'})
CREATE (x)-[:USED_IN]->(a),(x)-[:USED_IN]->(b),(y)-[:USED_IN]->(a),(y)-[:USED_IN]->(g),(z)-[:USED_IN]->(b),(z)-[:USED_IN]->(g),(w)-[:USED_IN]->(g);

MATCH (a:Product {name:'Product Alpha'}),(b:Product {name:'Product Beta'}),(g:Product {name:'Product Gamma'}),
      (delhi:Plant {name:'Plant Delhi'}),(pune:Plant {name:'Plant Pune'}),(chennai:Plant {name:'Plant Chennai'})
CREATE (a)-[:MANUFACTURED_AT]->(delhi),(a)-[:MANUFACTURED_AT]->(pune),(b)-[:MANUFACTURED_AT]->(pune),(b)-[:MANUFACTURED_AT]->(chennai),(g)-[:MANUFACTURED_AT]->(chennai);

MATCH (s1:Shipment {id:'Shipment 101'}),(s2:Shipment {id:'Shipment 102'}),(s3:Shipment {id:'Shipment 103'}),
      (x:Component {name:'Component X'}),(y:Component {name:'Component Y'}),(z:Component {name:'Component Z'}),
      (delhi:Plant {name:'Plant Delhi'}),(pune:Plant {name:'Plant Pune'}),(chennai:Plant {name:'Plant Chennai'})
CREATE (s1)-[:CONTAINS]->(x),(s1)-[:DESTINED_FOR]->(delhi),(s2)-[:CONTAINS]->(y),(s2)-[:DESTINED_FOR]->(pune),(s3)-[:CONTAINS]->(z),(s3)-[:DESTINED_FOR]->(chennai);

MATCH (b:Supplier {name:'Supplier B'}),(a:Supplier {name:'Supplier A'})
CREATE (b)-[:SUPPLIES_SUPPLIER]->(a);
