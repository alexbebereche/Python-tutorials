import traceback

try:
    raise Exception("exception message")
except Exception as e: # sometimes the message is not helpful
    print(e)
    print("print traceback")
    print()
    traceback.print_exc()
    print(traceback.format_exc())