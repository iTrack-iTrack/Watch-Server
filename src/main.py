import server
import sql

import dotenv

def main():
    dotenv.load_dotenv()

    conn, db = sql.initialise()
    s = server.initialise()

    try:
        while True:
            msg = server.receive(s)
            if msg == None:
                continue

            print(msg)

            for row in db.execute("SELECT * FROM sensor_readings"):
                print(row)
    except KeyboardInterrupt:
        print("Exiting...")

    server.terminate(s)
    sql.terminate(conn, db)

if __name__ == "__main__":
    main()
