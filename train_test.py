import train_nets

# the first parameter is the number of epochs
train_nets.train_speck_distinguisher(10, num_rounds=1, depth=10)