points=(50    100   200   500   800   1000  2000  5000)
canvas=(10000 10000 10000 10000 10000 10000 10000 40000)
# points=(8000 10000 20000)
# points=(100000)
dist="mix-normal"

for i in "${!points[@]}"; do
    num=${points[$i]}
    range=${canvas[$i]}
    set=${num}_${range}x${range}
    export file="test_sets/$set-$dist.nets"
    export output="outputs/flute$set-$dist.txt"
    export tree_dir="trees/flute$set-$dist/"
    cmd="../../../build/src/openroad get_flute_nets_wirelength.tcl"
    echo $cmd
    $cmd
done
