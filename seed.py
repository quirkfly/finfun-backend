import sqlite3
import random
from datetime import datetime, timedelta

DB_PATH = 'instance/db.sqlite3'

def seed_client():
    """
    Insert a sample client if it doesn't exist.
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Check if client exists
    c.execute("SELECT id FROM clients WHERE email = ?", ('john@example.com',))
    client = c.fetchone()

    if client:
        client_id = client[0]
        print(f"Client already exists with ID: {client_id}")
    else:
        created_at = datetime.today().strftime('%Y-%m-%d')
        c.execute('''
            INSERT INTO clients (name, email, created_at)
            VALUES (?, ?, ?)
        ''', ('John Doe', 'john@example.com', created_at))
        client_id = c.lastrowid
        print(f"Inserted new client with ID: {client_id}")

    conn.commit()
    conn.close()
    return client_id

def seed_transactions(client_id=1, days=180, daily_probability=0.5):
    """
    Insert synthetic transactions for the given client.
    """
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    today = datetime.today()
    categories = ['Transport', 'Dining', 'Groceries', 'Entertainment', 'Utilities']

    transactions = []
    for i in range(days):
        date = today - timedelta(days=i)
        if random.random() < daily_probability:
            amount = round(random.uniform(5, 50), 2)
            category = random.choice(categories)
            description = f"{category} expense"
            transactions.append((
                amount,
                category,
                date.strftime('%Y-%m-%d'),
                description,
                client_id
            ))

    if transactions:
        c.executemany('''
            INSERT INTO transactions (amount, category, date, description, client_id)
            VALUES (?, ?, ?, ?, ?)
        ''', transactions)
        print(f"Seeded {len(transactions)} transactions.")
    else:
        print("No transactions generated.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    client_id = seed_client()
    seed_transactions(client_id)
