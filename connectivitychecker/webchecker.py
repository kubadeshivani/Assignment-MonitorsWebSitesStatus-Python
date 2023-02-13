import time
import logging
import http.client
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
            
            if response.status == http.client.OK: 
                content_type    = response.getheader('Content-Type')
                if '=' in content_type:
                    response_encoding = content_type.split('=')[1]                       

                logger.debug("Get result with 'status': '%s'; 'Content-Type': '%s'; Detected charset: '%s' ", response.status,content_type,response_encoding)
                page_content = response.read().decode(response_encoding)
                return True  
            else:
                logger.debug("Get result with 'status': '%s'", response.status)

            
        except Exception as e:
            error = e   
                     
        finally:
            end_time = time.time()
            request_duration = end_time - start_time
            logger.info("Request Duration for connectivity with website %s is %f ", url,request_duration)
            connection.close()
    
    raise error


