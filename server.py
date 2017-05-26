def init(): # 
      
      import socket, _thread, sys;

      global socket, _thread, sys;

      global HOST, PORT, SOCKET;

      NAME = socket.gethostbyname(socket.gethostname());

      HOST, PORT = " ", 5555;

      SOCKET = socket.socket();

      print("Localhost %s listening on port %s \n" % (NAME, PORT));

#



def listen(): #

      SOCKET.bind((HOST, PORT));

      SOCKET.listen(5);

      global connection, address;

      connection, address = SOCKET.accept();

#



def client(connection, address): #

      while (True): #
      
            _input = connection.recv(1024).decode("utf-8");
            
            print("%s  ->  %s" % (address, _input));
            
            _output = str.encode("Hello %s, thanks for using our server (^_^)" % (address));
            
            connection.send(_output);

#

def main(): #

      init();

      while (True): #

            listen();
        
            _thread.start_new_thread(client, (connection, address));    
            
      #
      
#



main();
