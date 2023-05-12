# flute for net with 250 pins
source "stt_helpers.tcl"

set file "test_sets/point800.nets"

set output "outputs/flute800.txt"

set nets [read_nets $file]

set sum 0

set lengths {}

foreach net $nets {
    set net_wl [get_flute_net_wirelength $net]
    set sum [expr $sum + $net_wl]
    lappend lengths $net_wl
}

# dump file
set output_file [open $output "w"]
foreach length $lengths {
    puts $output_file "$length"
}

set len [llength $nets]

set avg [expr $sum * 1.0 / $len]

puts "avg wirelength $avg"