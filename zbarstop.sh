#!/bin/bash
tmp=/tmp/barcode.$$ # Note: security risk
zbarcam --nodisplay --prescale=300x200 > $tmp &
pid=$!
# Sleep until file has content
COUNT=0
while [[ ! -s $tmp ]] ; do
    sleep 1
    COUNT=$((COUNT+1))
    if [ COUNT == 60 ]; then
	exit
    fi
done
kill $pid
cat $tmp
rm $tmp
