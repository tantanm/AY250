import argparse
import re
import urllib2
from urllib2 import urlopen

def main():
    parser = argparse.ArgumentParser(description='Sample Application')
    parser.add_argument('-s', action='store', dest='inp',help='Your Input')
    results = parser.parse_args()
    calcalc(results.inp)


def calcalc(inp):
    try:
        evalresult=eval(inp)
        float(evalresult)
        print evalresult
    except (RuntimeError, TypeError, NameError, ValueError): 
        inp= inp.replace (" ", "%20")
        url= 'http://api.wolframalpha.com/v2/query?input='+inp+'&appid=KUL4AR-P9LQ3L6RLA'
        response= urllib2.urlopen(url)
        html=response.read()
        result= re.findall('<plaintext>(.*?)</plaintext>', html)
        print result
def test():
    assert(calcalc('3*4'))==12

def test():
    assert(calcalc('5+2'))==7
    
if __name__=="__main__":
    main()

