import psycopg2
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):

    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def connect_to_db(query):

    # initialize a connection variable
    conn = None

    try:
        # read connection parameters
        params = config()

        print("Connecting to the Redshift...")
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        print("Querying DB...")
        cur.execute(query)

        print("Fetching data...")
        data = cur.fetchall()
        
        print("Closing DB connection...")
        cur.close()

        return data

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')