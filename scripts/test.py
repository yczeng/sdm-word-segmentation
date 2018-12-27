import sdm as sdmlib

bits = 1000
sample = 1000000
scanner_type = sdmlib.SDM_SCANNER_OPENCL

# Generate an address space with 1,000,000 random 1,000-bit bitstrings.
address_space = sdmlib.AddressSpace.init_random(bits, sample)

# Generate 1,000,000 counters initialized with value zero in the RAM memory.
counter = sdmlib.Counter.init_zero(bits, sample)

# Create a file to store the 1,000,000 counters initialized with value zero.
# You do not need to provide file extension, because it will generate two files
# and automatically included the extension for you.
#counter = sdmlib.Counter.create_file('sdm-10w', bits, sample)

# Create an SDM with the generated address space and counter.
# The scans will be performed using the OpenCL scanner.
sdm = sdmlib.SDM(address_space, counter, 451, scanner_type)

v = []
for i in range(10):
    print(i)
    # Generate a random 1,000-bit bitstring.
    b = sdmlib.Bitstring.init_random(1000)

    # Write the bitstring to the SDM.
    sdm.write(b, b)
    v.append(b)
print(len(v), "bitstring wrote into memory.")

# Copy the bitstring from v[0].
# We have to make a copy because the flip_random_bits function changes the bitstring itself.
b = sdmlib.Bitstring.init_from_bitstring(v[0])
b.flip_random_bits(400)

# Read the bitstring from the SDM and checks the distance from the retrieved bitstring and v[0].
c = sdm.read(b)
print('Distance', c.distance_to(v[0]))

# Save the address space into the file 'sdm-10w.as'.
# The recommended extension for an address space is '.as'.

# Although we have used 10w as an indication of 10 writes to the memory, the
# address space is not affected by the writes. It is just a reference to help us
# remeber that this address space has been used together with the counters.
#address_space.save('sdm-10w.as');