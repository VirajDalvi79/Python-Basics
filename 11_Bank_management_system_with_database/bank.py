from database import connection, cursor

class Bank:

    def create_account(self, account_number, name, balance):
     cursor.execute("INSERT INTO accounts VALUES (%s, %s, %s)",
                    (account_number, name, balance))
     connection.commit()

    def deposit_money(self, account_number, amount):
       cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_number = %s",
                      (amount, account_number)) 
       connection.commit()

    def withdraw_money(self, account_number, amount):
       cursor.execute("SELECT balance FROM accounts WHERE account_number = %s",
                                (account_number,))
       balance = cursor.fetchone()
       actual_balance = balance[0]
       if actual_balance >= amount:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_number = %s",
                      (amount, account_number))
        connection.commit()
