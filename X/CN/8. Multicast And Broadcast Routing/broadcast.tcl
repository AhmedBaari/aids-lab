#How to run
#==========
#save this file as broadcast.tcl in desktop folder
#also save analysis.awk file in the same location
#open desktop right-click and choose 'Open in Terminal'
#run this command
#ns broadcast.tcl

#both nam and awk file will be executed automatically

set ns [new Simulator -multicast on]

set tf [open broadcast.tr w]
$ns trace-all $tf

set namfile [open broadcast.nam w]
$ns namtrace-all $namfile

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]

$ns duplex-link $n0 $n1 1Mb 10ms DropTail
$ns duplex-link $n0 $n2 1Mb 10ms DropTail
$ns duplex-link $n1 $n3 1Mb 10ms DropTail
$ns duplex-link $n2 $n4 1Mb 10ms DropTail

set mproto DM
set mrthandle [$ns mrtproto $mproto {}]

set group [Node allocaddr]

set udp [new Agent/UDP]
$ns attach-agent $n0 $udp

$udp set dst_addr_ $group
$udp set dst_port_ 0

set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp

set rcvr1 [new Agent/Null]
set rcvr2 [new Agent/Null]
set rcvr3 [new Agent/Null]
set rcvr4 [new Agent/Null]

$ns attach-agent $n1 $rcvr1
$ns attach-agent $n2 $rcvr2
$ns attach-agent $n3 $rcvr3
$ns attach-agent $n4 $rcvr4

$ns at 0.0 "$n1 join-group $rcvr1 $group"
$ns at 0.0 "$n2 join-group $rcvr2 $group"
$ns at 0.0 "$n3 join-group $rcvr3 $group"
$ns at 0.0 "$n4 join-group $rcvr4 $group"

$ns at 0.5 "$cbr start"
$ns at 2.0 "$cbr stop"

$ns at 2.5 "finish"

proc finish {} {
    global ns tf namfile
    $ns flush-trace
    close $tf
    close $namfile
    puts "Executing nam..."
    exec nam broadcast.nam &
    exec awk -f analysis.awk broadcast.tr &
    exit 0
}

$ns run

