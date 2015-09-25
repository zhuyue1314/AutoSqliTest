# coding=utf-8
#code by xi4okv QQ:48011203 
import threading
import time

from AutoSqli import AutoSqli

def test_Sqli(test_url):
    t = AutoSqli('http://127.0.0.1:8775',test_url)
    t.run() 
	
    	
def Auto_test(test_urls,n):
    try:       
        for t in range(1,n):
            if t%10 == 0:
                time.sleep(300)
            else:
                t = threading.Thread(target=test_Sqli,args=(test_urls[t],))
                t.start()
#            t.join()

    except:
        print "线程创建失败"

n = 1
test_urls={}
for test_url in open("result.lst","a+"):
    test_urls[n] = test_url
    n = n + 1

Auto_test(test_urls,n)
