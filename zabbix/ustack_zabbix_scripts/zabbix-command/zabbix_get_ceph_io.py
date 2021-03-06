#!/usr/bin/env python
#
#Written by Xuchangbao

import sys
import json
import subprocess

args='ceph -s -f json'
out=subprocess.Popen(args,shell=True,stdout=subprocess.PIPE).communicate()[0]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: %s { op_per_sec | read_bytes_sec | write_bytes_sec }" \
              % sys.argv[0]
    else:
        print json.loads(out)['pgmap'][sys.argv[1]]
