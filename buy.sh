#!/bin/bash
step=1  #间隔的秒数，不能大于60
for ((i=0;i<10;i=(i+step)));do
    /usr/bin/php  /Users/wanghaolong/Code/buy/buy.php
    sleep $step
done
exit 0