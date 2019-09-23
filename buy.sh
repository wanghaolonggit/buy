date=`date +%F | sed 's/-//g'``date +%T | sed 's/://g'`
git branch $date  1
git checkout $date