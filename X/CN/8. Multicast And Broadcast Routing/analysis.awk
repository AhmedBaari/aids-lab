BEGIN{
	r1=d1=total=0
	ratio=tp1=0.0
}

{
	if($1 =="r" && $5=="cbr")r1++
	if($1 =="d" && $5=="cbr")d1++
}

END{
	total = r1+d1
	ratio = (r1)*100/total
	tp1 = (r1+d1)*8/1000000
	print("")
	print("Packets Received:",r1)
	print("Packets Dropped:",d1)
	print("Packets Delivery Ratio:",ratio,"%")
	print("UDP Throughput:",tp1,"Mbps")
}
