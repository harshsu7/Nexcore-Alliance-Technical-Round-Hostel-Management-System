import sqlite3

def login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    with sqlite3.connect("hostel.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM admin WHERE username=? AND password=?", (username, password))
        if cur.fetchone():
            print("Login successful.\n")
            return True
        else:
            print("Invalid credentials.")
            return False

def check_available_beds():
    with sqlite3.connect("hostel.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT bed_id FROM beds WHERE status='available'")
        beds = cur.fetchall()
        return [bed[0] for bed in beds]

def allot_bed():
    available_beds = check_available_beds()
    if not available_beds:
        print("No beds available.")
        return

    name = input("Enter user name: ")
    bed_id = available_beds[0]  # Allocating the first available bed

    with sqlite3.connect("hostel.db") as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, bed_id) VALUES (?, ?)", (name, bed_id))
        cur.execute("UPDATE beds SET status='occupied' WHERE bed_id=?", (bed_id,))
        conn.commit()
        print(f"Bed {bed_id} allotted to {name}.")

def main():
    print("Welcome to Hostel Management System\n")
    if not login():
        return

    while True:
        print("\n--- MENU ---")
        print("1. Check available beds")
        print("2. Allot bed to user")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            beds = check_available_beds()
            print(f"Available beds: {beds}" if beds else "No beds available.")
        elif choice == '2':
            allot_bed()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()