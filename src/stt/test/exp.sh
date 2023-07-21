# points=(50 100 200 500 800 1000 2000 5000)
points=(50)

for i in "${!points[@]}"; do
    num=${points[$i]}
    export file="test_sets/${num}_10000x10000.nets"
    export output="outputs/flute${num}_10000x10000.txt"
    export tree_dir="trees/flute${num}_10000x10000/"
    cmd="../../../build/src/openroad get_flute_nets_wirelength.tcl"
    echo $cmd
    $cmd
done

set file "test_sets/50_10000x10000.nets"

set output "outputs/flute50_10000x10000.txt"

set tree_dir "trees/flute50_10000x10000/"