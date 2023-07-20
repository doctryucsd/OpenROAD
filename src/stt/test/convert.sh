points=(50 100 200 500 800 1000 2000 5000)

for i in "${!points[@]}"; do
    num=${points[$i]}
    cmd="python convert.py /home/chy036/NN-Steiner/points/point${num}_10000x10000-100-pt/ ./test_sets/${num}_10000x10000.nets"
    echo $cmd
    $cmd
done