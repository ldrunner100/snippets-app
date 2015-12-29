import logging
import argparse
import sys
import psycopg2

#set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)


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
    """
<<<<<<< HEAD
    Store a snippet with an associated name.
=======

    Store a snippet with an associated name.

>>>>>>> 5371c63ed048dbbf3801d394eb201e0905f6bcf2
    Returns the name and the snippet
    """
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    logging.info("Storing snippet {!r: {!r}".format(name, snippet))
    cursor = connection.cursor()
    command = "insert into snippets values (%s, %s)"
    cursor.execute(command, (name, snippet))
    connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet
    

def get(keyword):
    """
    
    Retrieve the snippet with a given name.
    
    If there is no such snippet return "no such snippet"
    
    Returns the snippet.
    """
    try:
        command = "insert into snippets values (%s, %s)"
        cursor.execute(command, (name, snippet))
    except psycopg2.IntegrityError as e:
        connection.rollback()
        command = "update snippets set message=%s where keyword=%s"
        cursor.execute(command, (snippet, name))
    return row
        
    
if __name__ == "__main__":
    main()


    

    

