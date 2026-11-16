import time, uuid, datetime

random_string = str(uuid.uuid4())

while True:
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")
    print(f"{timestamp}: {random_string}", flush=True)
    time.sleep(5)