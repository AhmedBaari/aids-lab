BEGIN{
start = end = th = dly = 0
flag = data = 0
}
 
{
if($1=="r"&&$4==5){
	data+=$6
	if(flag==0){
		start=$2
		flag=1
	}	
	if(flag==1) 
		end=$2
}
}

END{
dly = end - start
th = data/dly
print("")
print("**********HTTP***********")
print("Start time:",start)
print("End time:",end)
print("Data =",data)
print("Throughput =",th)
print("Delay =",dly)
}
