#!/usr/bin/env python

import sys
if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
    sys.stderr.write('Quick and dirty vcf sample rename.  Pipe STDIN vcf and name of sample to use as arg\n'
                     'Usage: ' + sys.argv[0] + ' <new_sample_name>\n')
    exit(1)
sname = sys.argv[1]

f = 0
for line in sys.stdin:
    if line[0:6] == '#CHROM' and f == 0:
        old = line.rstrip('\n').split('\t')
        sys.stderr.write('Replacing ' + old[9] + ' with ' + sname + '\n')
        old[9] = sname
        sys.stdout.write('\t'.join(old) + '\n')
        f = 1
    elif f == 0:
        sys.stdout.write(line)
    else:
        sys.stdout.write(line)
        break
for line in sys.stdin:
    sys.stdout.write(line)
