parted --script /dev/sdc mklabel gpt
parted --script /dev/sdc mkpart primary 1 40%
parted --script /dev/sdc print
