/*
How to run
==========
save the file as chat.java (filename can be anything)
Command Prompt 1 (go to the location the file is saved)
javac *.java
java Server

Command Prompt 2 (go to the location the file is saved)
java Client
*/

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;

class Client extends JFrame{
    JTextField jt;
    JButton send;
    JLabel lbl;
    public static void main(String[] args) {
	new Client();
    }
    Client(){
        setTitle("Client");
	setSize(400, 200);
        setVisible(true);
	setLayout(new FlowLayout());
	lbl = new JLabel("Enter a string:");
        jt = new JTextField(20);
        send = new JButton("Send");
	add(lbl);
	add(jt);
	add(send);
	validate();
        send.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent ae) {
                try{
                    Socket s = new Socket("localhost", 1234);
                    DataOutputStream out = new DataOutputStream(s.getOutputStream());
                    out.writeUTF(jt.getText());
		    jt.setText("");
                    s.close();
                }catch(Exception e){System.out.println(e);}
            }
        });
    }
}

class Server extends JFrame{
    JTextArea jta;
    String newline = System.lineSeparator();
    public static void main(String[] args) {
	new Server();
    }
    Server(){
        setTitle("Server");
        setSize(400, 200);
        setVisible(true);
        jta = new JTextArea("Waiting for message..."+newline);
        add(jta);
	validate();
	try{
		ServerSocket ss = new ServerSocket(1234);
		while(true){
			Socket s = ss.accept();
	                DataInputStream in = new DataInputStream(s.getInputStream());
               		String msg = in.readUTF();
		        jta.append("Received: "+msg+" ("+check(msg)+")"+newline);
               		s.close();
                }
	}catch(Exception e){System.out.println(e);}
    }
    String check(String msg){
	StringBuffer rmsg = new StringBuffer(msg);
	rmsg.reverse();
	return msg.equalsIgnoreCase(new String(rmsg)) ? "It is a palindrome" : "It is not a palindrome";
    }
}
