points=(50 100 200 500 800 1000 2000 5000)

path="/home/chy036/NN-Steiner/points"

dist="normal"

for i in "${!points[@]}"; do
    num=${points[$i]}
    set=${num}_10000x10000-$dist
    cmd="python convert_tree.py $path/point${set}-100-pt/ \
    ./trees/flute${set} ./results/flute${set}"
    echo $cmd
    $cmd
done