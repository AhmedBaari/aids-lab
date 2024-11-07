/*
How to run
==========
save the file as rmi.java (filename can be anything)
Command Prompt 1 (go to the location the file is saved)
javac *.java
start rmiregistry
java Server

Command Prompt 2 (go to the location the file is saved)
java Client localhost

Note: If version error occurs, Compile following way:
javac --release 8 *.java
*/

import java.net.*;
import java.rmi.*;
import java.rmi.server.*;

interface MyServerIntf extends Remote{	
	String add(double a, double b) throws RemoteException;
}

class MyServerImpl extends UnicastRemoteObject implements MyServerIntf{
	MyServerImpl()throws RemoteException{}
	public String add(double a, double b)throws RemoteException{
		return a+" + "+b+" = "+(a+b);
	}	
}

class Client{
	public static void main(String[] arg){
		try{
			String name;
			if(arg.length == 0)
				name = "rmi://localhost/RMServer";
			else
				name = "rmi://"+arg[0]+"/RMServer";
			MyServerIntf asif = (MyServerIntf)Naming.lookup(name);
			System.out.println("Addition: "+asif.add(1200,1300));
		}catch(Exception e){System.out.println("Exception: "+e);}
	}
}


class Server{
	public static void main(String[] arg){
		try 	{
			MyServerImpl asi = new MyServerImpl();
			Naming.rebind("RMServer",asi);
			System.out.println("Server Started...");
		}
		catch(Exception e){System.out.println("Exception: "+e);}
	}
}
