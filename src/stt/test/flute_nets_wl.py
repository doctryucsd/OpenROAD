# flute gcd
from openroad import Design, Tech
import helpers
import stt_aux
import sys

tech = Tech()
design = Design(tech)

nets = stt_aux.read_nets(sys.argv[1])

sum_ = 0
for net in nets:
    sum_ += stt_aux.get_flute_net_wirelength(design, net)

print(f"Average FLUTE wirelength: {sum_ / len(nets)}")
