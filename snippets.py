import logging
import argparse
import sys
import psycopg2

#set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)
logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect(database="snippets")

def main():
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    #subparser for the put command
    logging.debug("Constructing put subparser")
    logging.debug("Connecting to PostgreSQL")
    connection = psycopg2.connect(database="snippets")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    get_parser = subparsers.add_parser("get")
    get_parser.add_argument("keyword", help="the keyword of the row")
    
    
    arguments = parser.parse_args(sys.argv[1:])
    # convert parsed arguments from namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")
    
    if command == "put":
        name, snippet = put(**arguments)
        print("Stored {!r} as {!r}".format(snippet, name))
    elif command == "get":
        snippet = get(**arguments)
        print("Retrieved snippet: {!r}".format(snippet))
        
def put(name, snippet):
    """Store a snippet with an associated name."""
    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    #cursor = connection.cursor()
    try:
        with connection, connection.cursor() as cursor:
            cursor.execute("update snippets set message=%s where keyword=%s", (name, snippet))
        connection.commit()
    except psycopg2.IntegrityError as e:
        connection.rollback()
        command = "update snippets set message=%s where keyword=%s"
        cursor.execute(command, (snippet, name))
    connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet
    

def get(keyword):
    """
    
    Retrieve the snippet with a given name.
    
    If there is no such snippet return "no such snippet"
    
    Returns the snippet.
    """
    with connection, connection.cursor() as cursor:
        cursor.execute("select message from snippets where keyword=%s", (keyword,))
        row = cursor.fetchone()
    logging.error("no row matching the criteria")
    logging.debug("row retrieved successfully")
    return row
        
    
if __name__ == "__main__":
    main()


    

    

