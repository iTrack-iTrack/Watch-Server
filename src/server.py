import sql

import datetime
import json
import os
import requests
import socket
import threading

def initialise():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    port = 8081

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((host,port))
    server.listen(5)

    return server

def handle(client, address, conn, db):
    try:
        while client:
            message = client.recv(1024)

            if not message:
                continue

            date_time = datetime.datetime.now()
            with open("{}/{}".format(os.getenv("PAYLOAD_FOLDER"), date_time), "wb") as f:
                f.write(message)

            msg = message.decode().rstrip()
            try:
                js = json.loads(msg)
                js["date_time"] = date_time

                arr = ["user_id", "step", "fall", "temperature", "latitude", "longitude", "bpm", "blood_oxygen"]

                insert = "date_time"
                values = "?"
                tuples = (date_time,)

                for item in arr:
                    if not item in js:
                        continue

                    insert += ", {}".format(item)
                    values += ", ?"
                    tuples += (js[item],)

                query = "INSERT INTO sensor_data ({}) VALUES ({});".format(insert, values)
                db.execute(query, tuples)
                conn.commit()

                r = requests.post("http://itrackandi.watch:8082/{}/live".format(js["user_id"]), json=js, timeout=5)
                r.raise_for_status()

            except Exception as e:
                print("Exception Ignored at Client {}:{} - {}".format(address[0], address[1], e));

    except socket.timeout:
        pass
    except Exception as e:
        print("Exception Caught at Client {}:{} - {}".format(address[0], address[1], e));
    finally:
        client.close()

def terminate(server):
    server.close()
