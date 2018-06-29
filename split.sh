#splits pcap file into tcp streams, saves them in directory
#usage: ./split.sh pcapfile.pcap savedir
mkdir $2
for stream in $(tshark -r $1 -T fields -e tcp.stream | sort -n | uniq)
do
    #numero dello stream
    echo $stream
    tshark -r $1 -w $2/stream-$stream.cap -Y "tcp.stream==$stream"
done
