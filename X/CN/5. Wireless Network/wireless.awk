BEGIN {
	rec=sen=drp=0
	res=start=end=0.0
}

{
	if($1 == "s")sen++
	if($1 == "r"){
		if(rec==0)start = $2
		rec++		
		res += $8
		end = $2
	}
	if($1 == "D")drp++
}

END {
	print("")
	print("Wireless-Network")
	print("Number Of Packets Sent : ", sen)
	print("Number Of Packets Recieved : ", rec)
	print("Number Of Packets Dropped  : ", drp)
	print("Start Of Simulation (in sec) : ", start)
	print("End Of Simulation (in sec)   : ", end)
	print("Total Throughput : ",((res*8) / ((end-start)*1000000))," Mbps")
	print("Packet Delivery Ratio: ",rec*100/sen,"%")
}
