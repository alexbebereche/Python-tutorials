import time

while True:
    try:
        print("printing")
        time.sleep(.1)
    # except:  # keyboard interrupt is still an exception
    #     print("some exception happened")  
    except Exception:
        print("some exception happened")