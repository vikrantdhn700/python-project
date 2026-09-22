CREATE TABLE users (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    email TEXT NOT NULL UNIQUE,
    full_name TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price NUMERIC(12, 2) NOT NULL,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT products_price_check
        CHECK (price >= 0),

    CONSTRAINT products_stock_quantity_check
        CHECK (stock_quantity >= 0)
);

CREATE TABLE orders (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL,
    total_amount NUMERIC(12, 2) NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending',
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT orders_user_fk
        FOREIGN KEY (user_id)
        REFERENCES users (id)
        ON DELETE RESTRICT,

    CONSTRAINT orders_status_check
        CHECK (
            status IN (
                'pending',
                'paid',
                'shipped',
                'completed',
                'cancelled'
            )
        )
);

CREATE TABLE order_items (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id BIGINT NOT NULL,
    product_id BIGINT NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(12, 2) NOT NULL,
    item_total NUMERIC(12, 2) NOT NULL,

    CONSTRAINT order_items_order_fk
        FOREIGN KEY (order_id)
        REFERENCES orders (id)
        ON DELETE CASCADE,

    CONSTRAINT order_items_product_fk
        FOREIGN KEY (product_id)
        REFERENCES products (id)
        ON DELETE RESTRICT,

    CONSTRAINT order_items_quantity_check
        CHECK (quantity > 0),

    CONSTRAINT order_items_unit_price_check
        CHECK (unit_price >= 0),

    CONSTRAINT order_items_order_product_unique
        UNIQUE (order_id, product_id)
);

CREATE INDEX orders_user_id_idx
    ON orders (user_id);

CREATE INDEX order_items_product_id_idx
    ON order_items (product_id);