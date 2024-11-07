/*
How to run
==========
save the file as filetransfer.java (filename can be anything)
Command Prompt 1 (go to the location the file is saved)
javac *.java
java Server

Command Prompt 2 (go to the location the file is saved)
java Client

select file_to_send.txt which will be there in the file location
(any file can be sent)
*/

import java.io.*;
import java.net.*;
import javax.swing.*;
import java.awt.event.*;

class Client extends JFrame {
	JTextArea jta;
	JButton send;
	JFileChooser jc;
	static String newline = System.lineSeparator();
	Client(){
		setTitle("File Client");
		setSize(400, 300);
		setVisible(true);
		jta = new JTextArea();
		send = new JButton("Send File");
		jc = new JFileChooser();
		send.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e){
				int op = jc.showOpenDialog(null);
				if(op == JFileChooser.APPROVE_OPTION)
					sendFile(jc.getSelectedFile());
			}
		});
		add(new JScrollPane(jta), "Center");
		add(send, "South");
		validate();
	}
	void sendFile(File f) {
		try{
			Socket s = new Socket("localhost", 5000);
			jta.setText("Connected to server"+newline);
			FileInputStream fin = new FileInputStream(f);
			OutputStream out = s.getOutputStream();

			byte[] buffer = new byte[1024];
			int bytesRead;
			while ((bytesRead = fin.read(buffer)) != -1){
				for (int i = 0; i < bytesRead; i++){
					byte plainByte = buffer[i];
					byte cipherByte = (byte) ((plainByte + 3) % 256);
					jta.append("Plain Text: " + plainByte + " (" + (char) plainByte + ") -> Cipher Text: " + cipherByte + " (" + (char) cipherByte + ")"+newline);
					buffer[i] = cipherByte;
				}
				out.write(buffer, 0, bytesRead);
			}
			fin.close();
			out.close();
			s.close();
			jta.append("File encrypted and sent successfully"+newline);
		}catch(Exception e){System.out.println(e);}
	}
	public static void main(String[] args){
		try{
			FileWriter fout = new FileWriter("file_to_send.txt");
			fout.write("Hello World"+newline+"Hello To JAVA");
			fout.close();
			new Client();
		}catch(Exception e){System.out.println(e);}
	}
}

class Server extends JFrame{
	JTextArea jta;
	String newline = System.lineSeparator();
	Server(){
		setTitle("File Server");
		setSize(400, 300);
		setVisible(true);
        	jta = new JTextArea();
        	add(new JScrollPane(jta));
		validate();
        	try{
            		ServerSocket ss = new ServerSocket(5000);
            		jta.append("Server is listening on port 5000"+newline);
	    		for(int n=1;n<=10;n++){
            			Socket s = ss.accept();
            			jta.setText("Client connected"+newline);
            			InputStream in = s.getInputStream();
            			FileOutputStream fout = new FileOutputStream("received_file_"+n+".txt");

            			byte[] buffer = new byte[1024];
            			int bytesRead;
            			while ((bytesRead = in.read(buffer)) != -1){
                			for (int i = 0; i < bytesRead; i++){
                    				byte cipherByte = buffer[i];
                    				byte plainByte = (byte) ((cipherByte - 3 + 256) % 256);
                    				jta.append("Cipher Text: " + cipherByte + " (" + (char) cipherByte + ") -> Plain Text: " + plainByte + " (" + (char) plainByte + ")"+newline);
                    				buffer[i] = plainByte;
                			}
                			fout.write(buffer, 0, bytesRead);
            			}
            			fout.close();
	            		in.close();
        	    		s.close();
	            		jta.append("File received and decrypted successfully"+newline);
			}
			ss.close();
        	}catch(Exception e){System.out.println(e);}
	}
	public static void main(String[] args){
		new Server();
	}
}