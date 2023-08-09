points=(50 100 200 500 800 1000 2000 5000)
# points=(50)
dist="mix-normal"

for i in "${!points[@]}"; do
    num=${points[$i]}
    export file="test_sets/${num}_10000x10000-$dist.nets"
    export output="outputs/flute${num}_10000x10000-$dist.txt"
    export tree_dir="trees/flute${num}_10000x10000-$dist/"
    cmd="../../../build/src/openroad get_flute_nets_wirelength.tcl"
    echo $cmd
    $cmd
done