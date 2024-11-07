BEGIN{
st1=ft1=0
throughput1=0
delay1=flag1=data1=0
}
 
{
if($1=="r"&&$4==5){
data1+=$6
if(flag1==0){
st1=$2
flag1=1}
if(flag1==1){
ft1=$2}}
}

END{
delay1=ft1-st1
throughput1=data1/delay1
print("")
print("**********HTTP***********")
print("Start time =",st1) 
print("End time =",ft1) 
print("Data:",data1) 
print("Throughput:",throughput1) 
print("Delay:",delay1) 
}
