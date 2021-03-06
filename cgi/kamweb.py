#!/usr/bin/python

import os
import cgi

def santise_env(env, cgipath="/cgi-bin/404"):
    env["PATH_INFO"] = env.get("PATH_INFO", env.get("REDIRECT_URL", ""))
    env["DOCUMENT_ROOT"] = env.get("DOCUMENT_ROOT", "/srv/Websites/iotoy.org/docs")
    env["PATH_TRANSLATED"] = env.get("PATH_TRANSLATED",  env["DOCUMENT_ROOT"]+env["PATH_INFO"])

    env["here"] = here = os.path.realpath(os.getcwd())
    env["appbase"] = here[:here.rfind("/")]

    if env.get("REDIRECT_REQUEST_METHOD", None):
        env["REQUEST_METHOD"] = env.get("REQUEST_METHOD", env["REDIRECT_REQUEST_METHOD"])
        del env["REDIRECT_REQUEST_METHOD"]
        del env["REDIRECT_URL"]
        del env["REDIRECT_STATUS"]

    if env.get("REDIRECT_QUERY_STRING", None):
        env["QUERY_STRING"] = env["REDIRECT_QUERY_STRING"]
        del env["REDIRECT_QUERY_STRING"]

    if env["REQUEST_URI"].startswith(cgipath):
        env["ZPREFIX"] = cgipath
        env["REQUEST_URI"] = env["REQUEST_URI"][(len(cgipath)):]
    else:
        env["ZPREFIX"] = ""

def debug_dump(env):
    print "Content-Type: text/html"
    print "Pragma: no-cache"
    print "Cache-Control: no-cache"
    print
    print "<html>"
    print "<body>"
    print "<h1> 404 Handler </h1>"
    print "<ul>"
    keys = env.keys()
    keys.sort()
    for key in keys:
        print "<li><b>%s</b> - <pre>%s</pre>" % (cgi.escape(key) ,cgi.escape(repr(env[key])))

    print "</ul>"
    print "</body>"
    print "</html>"

def serve_file(filetoserve, status=200):
    f = open(filetoserve) # No point doing this if the file doesn't open!
    import mimetypes
    mimetypes.init()
    mimetype, encoding = mimetypes.guess_type(filetoserve)

    if mimetype:
        print "Content-Type:", mimetype

    if encoding:
        print "Content-Encoding:", encoding
            
    import sys
    print "Status:", str(status)
    print
    data = f.read(327680)
    while data:
        sys.stdout.write(data)
        data = f.read(327680)

    f.close()

def scrub_filename(filename):
    while True:
        if filename[0] == "/":
            filename = filename[1:]
        else:
            break
    filename = filename.replace("../","") # Remove all of these inside the filename
    if filename[-2:] == "..":
       filename = filename[:-2]
    return filename

if __name__ == "__main__":
    pass
