from psycopg2 import connect, extensions, sql


def create_data(Data_name):
    conn = connect(
        database="postgres",
        user="postgres",
        password="1",
        host="127.0.0.1",
        port="5432"
    )

    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    conn.set_isolation_level(autocommit)
    cursor = conn.cursor()

    try:
        cursor.execute("CREATE USER user1 WITH password '1111'")
    except:
        pass

    try:
        cursor.execute(sql.SQL("CREATE DATABASE {} OWNER user1").format(sql.Identifier(Data_name)))
        cursor.execute(sql.SQL("GRANT ALL privileges ON DATABASE {} TO user1").format(sql.Identifier(Data_name)))
    except:
        cursor.close()
        conn.close()
        return 1

    cursor.close()
    conn.close()

    return 0


def delete_data(Data_name):
    conn = connect(
        database="postgres",
        user="postgres",
        password="1",
        host="127.0.0.1",
        port="5432"
    )

    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    conn.set_isolation_level(autocommit)
    cursor = conn.cursor()

    try:
        cursor = conn.cursor()
        cursor.execute(sql.SQL("DROP DATABASE {}").format(sql.Identifier(Data_name)))
    except:
        cursor.close()
        conn.close()
        return 1

    cursor.close()
    conn.close()
    return 0


def new_user(Data_name):
    conn = connect(
        database=Data_name,
        user="user1",
        password="1111",
        host="127.0.0.1",
        port="5432"
    )

    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    conn.set_isolation_level(autocommit)
    return conn


def tables_and_procedures(cursor):
    # создание таблицы
    cursor.execute("CREATE TABLE product (\"id product\" serial PRIMARY KEY, name varchar(80) , prise int)")
    cursor.execute("CREATE TABLE sale (\"id sale\" serial PRIMARY KEY, \"id product\" int, "
                   "\"number of sold\" int)")
    cursor.execute("CREATE TABLE records (\"id record\" serial PRIMARY KEY, quantity int)")

    # триггер

    cursor.execute("CREATE OR REPLACE FUNCTION add_trigger() RETURNS VOID AS \
    $$ \
    INSERT INTO records (quantity) VALUES (0); \
    $$ LANGUAGE sql;")

    cursor.execute("SELECT add_trigger()")

    cursor.execute("CREATE OR REPLACE FUNCTION n_records() RETURNS TRIGGER AS \
    $$ \
    BEGIN \
        UPDATE records SET quantity = quantity + 1 \
        WHERE records.\"id record\" in (1);\
        RETURN NEW; \
    END \
    $$ LANGUAGE plpgsql;")

    cursor.execute("CREATE TRIGGER update_n_records \
    AFTER INSERT ON sale EXECUTE PROCEDURE n_records();")

    # индекс
    cursor.execute("CREATE INDEX order_to ON product (name);")

    # процедуры

    # все продукты
    cursor.execute("CREATE OR REPLACE FUNCTION get_all_product() RETURNS SETOF product AS \
    $$ \
    SELECT * FROM product \
    $$ LANGUAGE sql;")

    # все продажи
    cursor.execute("CREATE OR REPLACE FUNCTION get_all_sale() RETURNS SETOF sale AS \
    $$ \
    SELECT * FROM sale \
    $$ LANGUAGE sql;")

    cursor.execute("CREATE OR REPLACE FUNCTION get_trigger() RETURNS SETOF records AS \
        $$ \
        SELECT * FROM records \
        $$ LANGUAGE sql;")

    # добавить записи
    cursor.execute("CREATE OR REPLACE FUNCTION add_product(name_product varchar(50), pr int) RETURNS VOID AS \
        $$ \
        INSERT INTO product (name, prise) VALUES (name_product, pr); \
        $$ LANGUAGE sql;")

    cursor.execute("CREATE OR REPLACE FUNCTION add_sale(prod int, num int) RETURNS VOID AS \
        $$ \
        INSERT INTO sale (\"id product\", \"number of sold\") VALUES (prod, num); \
        $$ LANGUAGE sql;")

    # поиск
    cursor.execute("CREATE OR REPLACE FUNCTION find_product(name_prod varchar(80)) RETURNS SETOF product AS \
        $$ \
        SELECT * FROM product \
        WHERE product.name in (name_prod);\
        $$ LANGUAGE sql;")

    # удаление

    cursor.execute("CREATE OR REPLACE FUNCTION delete_product(nm varchar(50)) RETURNS VOID AS \
        $$ \
        DELETE FROM product WHERE name = nm;\
        $$ LANGUAGE sql;")

    cursor.execute("CREATE OR REPLACE FUNCTION delete_sale(_id int) RETURNS VOID AS \
        $$ \
        DELETE FROM sale WHERE \"id sale\" = _id;\
        $$ LANGUAGE sql;")

