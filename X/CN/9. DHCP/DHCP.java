/*
How to run
==========
save the file as DHCP.java (filename can be anything)
Command Prompt 1 (go to the location the file is saved)
javac *.java
java Server

Command Prompt 2 (go to the location the file is saved)
java Client
*/

import java.io.*;
import java.net.*;
import java.util.*;

class Server{
	static int SERVER_PORT = 4900;
	static String SERVER_IP = "127.0.0.1"; // Change to your server's IP
	static String IP_ALLOCATIONS_FILE = "ip_allocations.txt";
	static List<String> availableIpAddresses = new ArrayList<>();
	static Map<String, String> ipAllocations = new HashMap<>();

	public static void main(String[] args){
		loadIpAllocations(); // Load IP allocations from file (if available)
		initializeIpAddresses();

		try{
			DatagramSocket socket = new DatagramSocket(SERVER_PORT);
			while(true){
				byte[] receiveData = new byte[1024];
				DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
				socket.receive(receivePacket);
				
				InetAddress clientAddress = receivePacket.getAddress();
				String macAddress = extractMacAddress(receiveData);
				String allocatedIp = allocateIpAddress(macAddress);

				byte[] responseData = createDHCPResponse(macAddress, allocatedIp);
				DatagramPacket responsePacket = new DatagramPacket(responseData, responseData.length, clientAddress, receivePacket.getPort());
				socket.send(responsePacket);

				System.out.println("Allocated IP " + allocatedIp + " to client with MAC " + macAddress);
				saveIpAllocations();
			}
		}catch(Exception e){
			e.printStackTrace();}
	}

	private static void initializeIpAddresses(){
		for(int i = 2; i <= 254; i++)
			availableIpAddresses.add("192.168.1." + i);
	}

	private static String extractMacAddress(byte[] data){
		return "00:11:22:33:44:55";
	}

	private static String allocateIpAddress(String macAddress){
		if(availableIpAddresses.isEmpty())
			return "No available IP addresses";
		Random random = new Random();
		int index = random.nextInt(availableIpAddresses.size());
		String allocatedIp = availableIpAddresses.remove(index);
		ipAllocations.put(macAddress, allocatedIp);
		return allocatedIp;
	}

	private static byte[] createDHCPResponse(String macAddress, String allocatedIp) {
		// Simulate creating a DHCP response with the allocated IP address
		// In a real implementation, you'd construct a proper DHCP packet
		return ("Allocated IP: " + allocatedIp).getBytes();
	}

	private static void saveIpAllocations() {
		try(ObjectOutputStream outputStream = new ObjectOutputStream(new FileOutputStream(IP_ALLOCATIONS_FILE))){
			outputStream.writeObject(ipAllocations);
			System.out.println("Saved IP allocations to " + IP_ALLOCATIONS_FILE);
		}catch (IOException e){
			e.printStackTrace();
		}
	}

	private static void loadIpAllocations() {
		try(ObjectInputStream inputStream = new ObjectInputStream(new FileInputStream(IP_ALLOCATIONS_FILE))){
			ipAllocations = (HashMap<String, String>) inputStream.readObject();
			System.out.println("Loaded IP allocations from " + IP_ALLOCATIONS_FILE);
		}catch(FileNotFoundException e){
			System.out.println(IP_ALLOCATIONS_FILE + " not found. Starting with an empty IP allocations map.");
		}catch(IOException | ClassNotFoundException e){
			e.printStackTrace();
		}
	}
}


class Client{
	static int SERVER_PORT = 4900;
	static String SERVER_IP = "127.0.0.1"; // Change to your server's IP

	public static void main(String[] args) {
		try{
			DatagramSocket socket = new DatagramSocket();
			InetAddress serverAddress = InetAddress.getByName(SERVER_IP);

			byte[] requestData = createDHCPRequest("00:11:22:33:44:55"); // Replace with your MAC address
			DatagramPacket requestPacket = new DatagramPacket(requestData, requestData.length, serverAddress, SERVER_PORT);
			socket.send(requestPacket);

			byte[] receiveData = new byte[1024];
			DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
			socket.receive(receivePacket);

			String response = new String(receivePacket.getData()).trim();
			System.out.println("Received DHCP Response: " + response);
		}catch(Exception e){
			e.printStackTrace();
		}
	}

	private static byte[] createDHCPRequest(String macAddress) {
		String request = "DHCP Request with MAC: " + macAddress;
		return request.getBytes();
	}
}