import sys
import os
import time
import logging
import argparse

def prep_vars():
    global user
    global domain

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", default="", help="the User of the deployment account. Default: ''")
    parser.add_argument("-d", "--domain", default="", help="the domain of the deployment account. Default: ''")
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help="verbose execution")
    args = parser.parse_args()

    if (args.verbose):
        log_level=logging.DEBUG
    else:
        log_level=logging.INFO
    
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=log_level,
        datefmt='%Y-%m-%d %H:%M:%S')

    logging.debug("argumant user: %s" % args.user)
    logging.debug("argument domain: %s" % args.domain)


    if (args.user):
        user = args.user
    else:
        user = os.environ.get('USER', "")
    
    if (args.domain):
        domain = args.domain
    else:
        domain = os.environ.get('DOMAIN', "")

    if (user == ""):
         logging.error("User was not provided - define user before submission.")
         sys.exit(1)

    if (domain == ""):
         logging.error("Domain was not provided - define domain before submission.")
         sys.exit(1)

    logging.debug("user: %s" % user)
    logging.debug("domain: %s" % domain)

    return()

def gen_templates(u, d):
    global user
    global domain

    # nginx template
    nginx_template = "/user/"+user+"/sites/"+domain+"/deploy_tools/nginx.template.conf"
    nginx_prod_file = "/etc/nginx/sites-available/"+domain

    try:
        fp = open(nginx_template)
        line = fp.readline()
        fout = open(nginx_prod_file, "+w")
        while(line):
            line = line.replace('USER', user)
            line = line.replace('DOMAIN', domain)
            fout.write(line)
            line = fp.readline()
    finally:
        fp.close()
    
    return()

def start_services():
    return()

def main():
    global user
    global domain
    user=""
    domain=""
 
    prep_vars()    
    gen_templates(user, domain)
    start_services()

if __name__ == '__main__':
    main()
