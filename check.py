import urllib.request
import urllib.parse
import json
import os
trans = input('Please type in what you want to be checked:')
params = urllib.parse.urlencode({'a': 'getWordMean', 'c': 'search', 'word': trans})
url = "http://www.iciba.com/index.php?%s" % params
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
results = json.loads(html)
check=results['baesInfo']
check_result='suggest' in check.keys()
if check_result == True:         
    corword=results['baesInfo']['suggest'][0]['key']
    print( 0)
else:
    print( 1)


    
