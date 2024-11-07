BEGIN {
recvdSize = 0
startTime = 0.5
stopTime = 5.0
}

{
event = $1
time = $2
node_id = $3
pkt_size = $6
level = $4

if (event == "s") {
if (time < startTime) {
startTime = time
}
}

if (event == "r") {
if (time > stopTime) {
stopTime = time
}
recvdSize += pkt_size
}
}

END{
print("")
printf("Average Throughput[kbps] = %.2f",(recvdSize/(stopTime-startTime))*(8/1000))
print("")
printf("StartTime = %.2f",startTime)
print("")
printf("StopTime  = %.2f",stopTime)
print("")
}
