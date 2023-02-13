import argparse
import logging

logger = logging.getLogger(__name__)

def read_user_arguments():   
    
    print("............. Starting Website connectivity checker in continous loop. Use Ctrl+C to stop. .........")
    parser = argparse.ArgumentParser(
        prog="connectivitychecker", description="check the availability of websites"
    )
    parser.add_argument(
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Enter one or more website URLs",
    )
    parser.add_argument(
        "--url-file",        
        metavar="FILE",
        type=str,
        default="",
        help="Read URLs from Yaml file",
    )

    return parser.parse_args()

def log_connection_result(result, url, error=""):    
    print(f'The status of "{url}" is:', end=" ")
    if result:
        print('"Online!"')
        logger.info('The status of webpage %s is : "Online!"',url)
    else:
        logger.info('The status of webpage %s is : "Offline?"  with Error %s :',url,error)
        print(f'"Offline?"  \n  Error: "{error}"')
