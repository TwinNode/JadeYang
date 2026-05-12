"""
* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""
import re
def domain_name(url):  
    new = url.replace("http://", "").replace("https://", "").replace("www.", "")
    return re.sub(r"(?=\.).*", "", new)


#best practice
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

#clever
import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
