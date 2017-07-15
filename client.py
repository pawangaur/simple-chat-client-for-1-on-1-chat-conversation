import socket
import select
import sys
import thread

def outgoing():
    while True:
        message = sys.stdin.readline()
        server.send(message)
def incoming():
    while True:
        try:
            message=server.recv(2048)
            if message:
                print message
            else:
                print "Server closed connection"
                thread.interrupt_main()
                break
        except:
              #Process terminates
            print "Server closed connection"
            thread.interrupt_main()
            break
        
        

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if len(sys.argv) != 3:
        print "Correct usage: script, IP address, port number"
        exit()
    IP_address = str(sys.argv[1])
    Port = int(sys.argv[2])
    server.connect((IP_address, Port))
    thread.start_new_thread(outgoing,())
    thread.start_new_thread(incoming,())

    try:
        while 1:
            continue
    except:
        print "Client program quits...."
        server.close()     