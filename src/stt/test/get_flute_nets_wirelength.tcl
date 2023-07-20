# flute for net with 250 pins
source "stt_helpers.tcl"

set file $env(file)

set output $env(output)

set tree_dir $env(tree_dir)
file mkdir $tree_dir

set nets [read_nets $file]

set sum 0

set lengths {}

set start [clock milliseconds]
set idx 0
foreach net $nets {
    set net_wl [get_flute_net_wirelength $net "$tree_dir$idx.txt"]
    set sum [expr $sum + $net_wl]
    lappend lengths $net_wl
    incr idx
}
set end [clock milliseconds]
set runtime [expr $end - $start]
set runtime [expr $runtime / 1000.0]

# dump file
set output_file [open $output "w"]
foreach length $lengths {
    puts $output_file "$length"
}

set len [llength $nets]

set avg [expr $sum * 1.0 / $len]

puts "avg wirelength $avg"
puts "Running time: $runtime second"

exit