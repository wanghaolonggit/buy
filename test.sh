#!/bin/bash
sleep 40;
step=1  #间隔的秒数，不能大于60
for ((i=0;i<60;i=(i+step)));do
    /usr/bin/php  /Users/wanghaolong/Code/buy/buy.php  >>  /Users/wanghaolong/Code/buy/test.log
    sleep $step
done
exit 0