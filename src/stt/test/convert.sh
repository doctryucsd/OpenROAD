points=(50 100 200 500 800 1000 2000 5000)
dist="mix-normal"
path="/home/chy036/NN-Steiner/points"

for i in "${!points[@]}"; do
    num=${points[$i]}
    cmd="python convert.py \
    $path/point${num}_10000x10000-$dist-100-pt/ \
    ./test_sets/${num}_10000x10000-$dist.nets"
    echo $cmd
    $cmd
done