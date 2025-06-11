import server
import sql

import dotenv
import threading

def main():
    dotenv.load_dotenv()

    conn, db = sql.initialise()
    s = server.initialise()

    try:
        while True:
            client, address = s.accept()

            threading.Thread(target=server.handle, args=(client, address, conn, db)).start()
            
    except KeyboardInterrupt:
        print("Exiting...")

    server.terminate(s)
    sql.terminate(conn, db)

if __name__ == "__main__":
    main()
