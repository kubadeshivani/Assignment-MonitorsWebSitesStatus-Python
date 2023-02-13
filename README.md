# Monitors web sites for web site administrators for detecting problems on their sites in Python

 A simple program that monitors web sites and reports their availability. This tool is intended as a monitoring tool for web site administrators for detecting problems on their sites.

-Features
* Reads a list of web pages (HTTP URLs) from a YAML file.
* Periodically makes an HTTP request to each URL.
* Measures the time it took for the web server to complete the whole request.
* Verifies the connectivity (online/offline) using 'HEAD' request to given web url
* Writes a log file that shows the progress of the periodic checks.

## Dependencies 

python version required : python 3

## Run options for the Project
Run the application with below commands :

python3 -m connectivitychecker [options] [URLS_File.yaml]

* [options] connectivitychecker provides the following options:
 `--urls` takes one or more URLs and checks if they're online.
 `--url-file` takes a file containing a list of URLs to check.
* <URL_File.yaml> is a mandatory path parameter when using url-file option. See `input/urls.yaml` for a sample configuration file.

## Example Run Configurations: 
python3 -m connectivitychecker --url-file input/urls.yaml
python3 -m connectivitychecker --urls http://www.wikipedia.org/ http://stackoverflow.com/ http://invalidurl.fi

## Notes :
<b>URL redirects</b> : In current application redirects are not considered as errors and only response status is logged in the log file

## Improvement areas : TODO List

Current application only checks the connectivity of given URL based on 'HEAD' request succes and logs the response status in log file with required duration.

I will be able to make folllowing improvements in the real applications :

* Use regular expression patterns as input in configuration URL file and then use those to match response content received from 'GET' request
* Better logging of the status of the website with actual result with pattern matched/not matched
* Provide an option to Handle URL redirects as error or success
* Add validations of the user input and better exception handling
* Will not use print statements instead use console logger

