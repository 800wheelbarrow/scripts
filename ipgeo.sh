#!/bin/bash
cp /var/log/auth.log* .
gunzip *.gz
cat auth.log* > combined.txt
grep -oE '((1?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.){3}(1?[0-9][0-9]?|2[0-4][0-9]|25[0-5])' combined.txt > ips.txt
sort ips.txt | uniq -u > ipsfiltered.txt
sed -i '1iquery' ipsfiltered.txt
head -n 100 ipsfiltered.txt > ipsfiltered2.txt
python csv2json.py -i ipsfiltered2.txt -o ipstosubmit.json -f pretty
curl ip-api.com/batch --data '@ipstosubmit.json' > result.txt
python -m json.tool result.txt > finalresults.output
rm auth.log*
rm *.txt
