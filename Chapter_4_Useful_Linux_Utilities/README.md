# Exersises :

##  Define what IOPS is and explain the difference between throughput:


IOPS- Input Output Operation per Second. Measures the 'operations' of read and write per second (e.g. 1 ping request per second) . This are often used in AWS services like Databases (e.g. Casandra). Throughput- measures the numbers of bits that has been read and written per second. This are often used to measure the aomunt of data that has been transferred (e.g. data transferred  per second)

## Name a limitation with fdisk for creating partitions that parted doesn’t have: 

Disk Size above 2TB (>2GB) is not possible to use using FDISK (<2TB).

 parted and gparted can process disk size above this size(>2TB).

## Name three tools that can provide disk information:

fdisk - used for manipulating partition <2 TB

sfdisk - works like fdisk witgh more options

parted - use for manipulating partition > 2TB

df - repors file system and prints the disk usage

lsblk -  prints information including name, type, mountpoint concerning all available or particular mounted block device(s) excluding RAM disks.

blkid - a utility that locates or displays block device attributes (NAME=value pair) such as device or partition name, label, its filesystem type among others.

hwinfo -  generally prints detailed information about system hardware.

pydf - can be an alternative to df. Easy interface and more straightforward.

# What can SSH Tunnel can do? Why is it useful?

SSH - Using for sending information from private networks to public net (Internet) using encapsulation. Since tunneling does modify and repackage the content of the data to be transferred,  usually through the use of encryption, then it can mask the real information of the traffic as it run through the ssh tunnel. 

# Tutorial: Accessing server via android

https://monovm.com/blog/how-to-connect-to-linux-vps-server-via-android/

