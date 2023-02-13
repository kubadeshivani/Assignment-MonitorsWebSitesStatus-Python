import pathlib
import yaml
import sys
import logging
import time
from connectivitychecker.webchecker import site_is_available
from connectivitychecker.argumentparser import log_connection_result, read_user_arguments

logger = logging.getLogger(__name__)


def main():    
    configure_logging()
    user_args = read_user_arguments()
    urls = get_websites_urls(user_args)
    if not urls:
        print(".. No URLs Provided..", file=sys.stderr)
        sys.exit(1)

    run_connectivity_check(urls)

def configure_logging(): 

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
  
    configure_file_logging(root_logger, logging.DEBUG, 'http_connectivity_checker.log')

def configure_file_logging(logger, level, log_path):
    """ Makes specified logger print information to the file """
   
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler = logging.FileHandler(log_path)
    handler.setLevel(level)
    handler.setFormatter(formatter)

    logger.addHandler(handler)    

# Get Website Urls from the user configuration file
def get_websites_urls(user_args):
    urls = user_args.urls
    if user_args.input_file:
        urls = read_urls_from_configuration_file(user_args.input_file)
    return urls


def read_urls_from_configuration_file(file):
    file_path = pathlib.Path(file)
    result_urls =[]
    if file_path.is_file():     
        # Open the file and load the file     
        with open(file,'r', encoding='utf-8') as url_configuration_file:            
            input_urls = yaml.safe_load(url_configuration_file)
            url_settings = {}                  
            url_settings['urls'] = input_urls['urls']            
            for url_config in url_settings['urls']:                
                if url_config['url']:                    
                    result_urls.append(url_config['url'])                                 

    else:
        print("Error: input configuration file not found", file=sys.stderr)

    return result_urls

def connectivity_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_available(url,3)
        except Exception as e:
            result = False
            error = str(e)
        log_connection_result(result, url, error)


def run_connectivity_check(urls):
        
        probe_int= 10        
        logger.info("Starting connectivity checker in an infinite loop. Use Ctrl+C to stop.\n")

        probe_index = 0
        try:
            while True:
                logger.debug("Starting probe %d", probe_index + 1)
                connectivity_check(urls)
                time.sleep(probe_int)

        except KeyboardInterrupt:
            logger.info("Keyboard Interrupt")

            sys.exit(0)


if __name__ == "__main__":
    main()
