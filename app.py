from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='food_delivery_db'
    )

@app.route('/')
def dashboard():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Total Orders
    cursor.execute("SELECT COUNT(*) AS total_orders FROM orders")
    total_orders = cursor.fetchone()['total_orders']

    # Total Revenue
    cursor.execute("""
        SELECT SUM(o.quantity * f.price) AS total_revenue
        FROM orders o JOIN foods f ON o.food_id = f.food_id
    """)
    total_revenue = cursor.fetchone()['total_revenue']

    # Top Selling Foods
    cursor.execute("""
        SELECT f.food_name, SUM(o.quantity) AS total_sold
        FROM orders o JOIN foods f ON o.food_id = f.food_id
        GROUP BY f.food_name
        ORDER BY total_sold DESC
        LIMIT 5
    """)
    top_foods = cursor.fetchall()

    # Orders by City
    cursor.execute("""
        SELECT c.city, COUNT(o.order_id) AS orders_count
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        GROUP BY c.city
    """)
    orders_by_city = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html',
                           total_orders=total_orders,
                           total_revenue=total_revenue,
                           top_foods=top_foods,
                           orders_by_city=orders_by_city)

if __name__ == '__main__':
    app.run(debug=True)
