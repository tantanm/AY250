
def calcalc(inp):
   try:
        evalresult=eval(inp)
        float(evalresult)
        return evalresult
   except (RuntimeError, TypeError, NameError, ValueError): 
        inp= inp.replace (" ", "%20")
        url= 'http://api.wolframalpha.com/v2/query?input='+inp+'&appid=KUL4AR-P9LQ3L6RLA'
        response= urllib2.urlopen(url)
        html=response.read()
        result= re.findall('<plaintext>(.*?)</plaintext>', html)
        return result[0][1]
        
