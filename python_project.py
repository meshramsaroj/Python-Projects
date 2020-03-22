import sqlite3 as lite

# functionality goes here


class DatabaseManage(object):
  def __init__(self):
        global DBconnection
        try:
            DBconnection = lite.connect('courses.db')
            with DBconnection:
                cur = DBconnection.cursor()
                # it will execute sql statement
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, description TEXT, price TEXT,is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create a DB!")

  # create data into DB


  def insert_data(self, data):
    try:
        with DBconnection:
            cur = DBconnection.cursor()
            cur.execute(
                "INSERT INTO course(name,description,price,is_private)VALUES(?,?,?,?)", data
            )
            return True
    except Exception:
        return False


  # Read data for DB
  def fetch_data(self):
    try:
        with DBconnection:
            cur = DBconnection.cursor()
            cur.execute("SELECT * FROM course")
            return cur.fetchall()  # it will return or read all data
    except Exception:
        return False


  # Delete data from DB
  def delete_data(self, id):
    try:
        with DBconnection:
            cur = DBconnection.cursor()
            sql = "DELETE FROM course WHERE id =?"
            cur.execute(sql, [id])
            return True
    except Exception:
        return False


# todo interface here
def main():
    print("\t")
    print("*"*40)
    print("\n\t :: COURSE MANAGEMENT ::\n")
    print("*"*40)
    print("\n\t")

    db = DatabaseManage()
    print("#"*40)
    print("\n\t :: USER MANUAL :: \n")
    print("#"*40)
    print("\n\t1. Insert a new Couserses")
    print("\n\t2. Show all Couserse")
    print("\n\t3. Delete a course form Couserses \n")
    print("#"*40)
    print("\n\t")
    choice = input("\n Enter a choice: ")
    if choice == "1":
        name = input("\n Enter course name: ")
        description = input("\n Enter course description: ")
        price = input("\n Eneter course price: ")
        is_private = input("\n Eneter course private(0/1): ")
        if db.insert_data([name, description, price, is_private]):
            print("Course was inserted successfully !")
        else:
            print("OOPS Something goes wrong!!!")

    elif choice == "2":
        print("\n :: Course List ::")

        for index, item in enumerate(db.fetch_data()):
            print("\n Srl no: " + str(index + 1))
            print("\n Course Id: " + str(item[0]))
            print("\n Course name: " + str(item[1]))
            print("\n Course description: " + str(item[2]))
            print("\n Course price: " + str(item[3]))
            private = 'Yes' if item[4] else 'No'
            print(" Is Private: " + private)
            print("\n")

    elif choice == "3":
        record_id = input("\n Enter the COurse id: ")

        if db.delete_data(record_id):
            print("\n Course was deleted with a success")
        else:
            print("\n OOPS SOmething went wrong")

    else:
        print("\n Wrong choice ! Please enter valid choice(1/2/3): ")

#  have to call main method
if __name__ == '__main__':
    main()
