BEGIN{
	r1=r2=d1=d2=total=0
	ratio=tp1=tp2=0.0
}

{
	if($1 =="r" && $4 == 3 && $5=="cbr")r1++
	if($1 =="d" && $4 == 3 && $5=="cbr")d1++
	if($1 =="r" && $4 == 5 && $5=="tcp")r2++
	if($1 =="d" && $4 == 5 && $5=="tcp")d2++
}

END{
	total = r1+r2+d1+d2
	ratio = (r1+r2)*100/total
	tp1 = (r1+d1)*8/1000000
	tp2 = (r2+d2)*8/1000000
	print("")
	print("Wired-Network")
	print("Packets Received:",r1+r2)
	print("Packets Dropped :",d1+d2)
	print("Packets Delivery Ratio:",ratio,"%")
	print("UDP Throughput:",tp1,"Mbps")
	print("TCP Throughput:",tp2,"Mbps")
}
