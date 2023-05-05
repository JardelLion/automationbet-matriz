#get access on the site of the statics
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError


def access(url):
    try:
        request_access = Request(url,
                      headers= {"User-Agent": 'Mozilla/5.0'})
        access = urlopen(request_access)
    except URLError:
        return 'URL Invalid, Please check you URL'
    
    except ValueError:
        return "You pass an invalid value"
    
    except HTTPError:
        return "This page doesn't exists"
    else:
        return access


