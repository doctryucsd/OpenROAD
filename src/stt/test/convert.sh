points=(50    100   200   500   800   1000  2000  5000)
canvas=(10000 10000 10000 10000 10000 10000 10000 40000)
# points=(8000 10000 20000)
# points=(100000)
dist="mix-normal"
path="/home/chy036/NN-Steiner/points"

for i in "${!points[@]}"; do
    num=${points[$i]}
    range=${canvas[$i]}
    set=${num}_${range}x${range}
    cmd="python convert.py \
    $path/point$set-$dist-100-pt/ \
    ./test_sets/$set-$dist.nets"
    echo $cmd
    $cmd
done
