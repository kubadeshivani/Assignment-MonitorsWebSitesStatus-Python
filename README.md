# Monitors web sites for web site administrators for detecting problems on their sites in Python

 A simple program that monitors web sites and reports their availability. This tool is intended as a monitoring tool for web site administrators for detecting problems on their sites.

-Features
* Reads a list of web pages (HTTP URLs) from a YAML file.
* Periodically makes an HTTP request to each page.
* Measures the time it took for the web server to complete the whole request.
* Verifies that the page content received from the server matches the content requirements.
* Writes a log file that shows the progress of the periodic checks.

## Dependencies
python 3
python -m pip install aiohttp

## Run the Project
It's a console application and takes just a few arguments:
python3 -m connectivitychecker [options] <Requirement_File.yaml>

* <Requirement_File.yaml> is a mandatory path to a file listing URLs and their requirements. See `input/urls.yaml` for a sample configuration file.
* [options] connectivitychecker provides the following options:
 `-u` or `--urls` takes one or more URLs and checks if they're online.
 `-f` or `--input-file` takes a file containing a list of URLs to check.

## TODOList
* Will use new logger file for console to print information to consol
* Will do some probability checks like "MATCH", "NOTMATCH","ERRORS",etc. to assert the page content coming from web sites 

