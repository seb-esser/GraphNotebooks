
def load_credentials(filename: str = "Neo4j-aacfd399-Created-2024-10-18.txt") -> dict: 
    """
    Loads the neo4j credentials if stated as a file"""

    try: 
        with open(filename) as f: 
            raw = f.readlines()
    except: 
        raise FileNotFoundError("Credentials File has not been found. ")

    URI = raw[1].split("=")[1][:-1]
    USERNAME = raw[2].split("=")[1][:-1]
    PASSWPORD = raw[3].split("=")[1][:-1]
    INSTANCE_ID = raw[4].split("=")[1][:-1]
    INSTANCE_NAME = raw[5].split("=")[1][:-1]
    credentials = {
        "URI": URI, 
        "USERNAME": USERNAME, 
        "PASSWORD": PASSWPORD, 
        "INSTANCE_ID": INSTANCE_ID, 
        "INSTANCE_NAME": INSTANCE_NAME
    }

    return credentials


if __name__ == "__main__": 
    creds = load_credentials()
    print(creds)
