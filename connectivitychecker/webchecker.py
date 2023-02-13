import time
import logging
from http.client import HTTPConnection
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

def site_is_available(url, timeout=3):
    start_time   = None
    end_time     = None    
    error = Exception("unknown error")

    parsed_url = urlparse(url)
    host = parsed_url.netloc or parsed_url.path.split("/")[0]    

    for port in (80, 443):

        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        start_time = time.time()
        
        try:                    
            connection.request("HEAD", "/")            
            response = connection.getresponse()
            logger.info(" 'Response Status': '%s' received for URL '%s'", response.status,url)                           
            return True         
            
        except Exception as e:
            error = e   
                     
        finally:
            end_time = time.time()
            request_duration = end_time - start_time
            logger.info("Request Duration for connectivity with website %s is %f ", url,request_duration)
            connection.close()
    
    raise error


