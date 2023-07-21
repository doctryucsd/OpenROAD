points=(50 100 200 500 800 1000 2000 5000)

for i in "${!points[@]}"; do
    num=${points[$i]}
    cmd="python convert_tree.py /home/chy036/NN-Steiner/points/point${num}_10000x10000-100-pt/ ./trees/flute${num}_10000x10000 ./results/flute${num}_10000x10000"
    echo $cmd
    $cmd
done