CREATE CONSTRAINT supplier_name_unique IF NOT EXISTS FOR (n:Supplier) REQUIRE n.name IS UNIQUE;
CREATE CONSTRAINT component_name_unique IF NOT EXISTS FOR (n:Component) REQUIRE n.name IS UNIQUE;
CREATE CONSTRAINT product_name_unique IF NOT EXISTS FOR (n:Product) REQUIRE n.name IS UNIQUE;
CREATE CONSTRAINT plant_name_unique IF NOT EXISTS FOR (n:Plant) REQUIRE n.name IS UNIQUE;
CREATE CONSTRAINT country_name_unique IF NOT EXISTS FOR (n:Country) REQUIRE n.name IS UNIQUE;
CREATE CONSTRAINT shipment_id_unique IF NOT EXISTS FOR (n:Shipment) REQUIRE n.id IS UNIQUE;
