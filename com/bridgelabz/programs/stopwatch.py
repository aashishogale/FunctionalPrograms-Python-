import datetime

if __name__ == '__main__':
    inpustring = input("print enter to start")
    start = datetime.datetime.utcnow()
    print(start)
    inputstring = input("print enter to stop")
    stop = datetime.datetime.utcnow()
    print(stop)
    elapsedtime=(stop-start).microseconds
    print("elapsed time in microseconds",elapsedtime)

