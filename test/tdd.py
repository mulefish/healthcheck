import time

def timething():
    t = time.time()
    print("hello worrld {}".format(t))    
    print(time.localtime( time.time() )) 
    # print(time.asctime( time.localtime(time.time()) )
    
if __name__ == '__main__':
    timething()
