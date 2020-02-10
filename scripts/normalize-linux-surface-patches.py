#!/usr/bin/python3

import argparse, os, re, sys

# process command line arguments
parser = argparse.ArgumentParser()
parser.add_argument( "-r", "--rename", help="rename files instead of just printing out what would be renamed", action="store_true" )
args = parser.parse_args()
  
# gather patches
files = []
for name in os.listdir( '.' ):
  m = re.search( r'^\d{4}-(.+\.patch$)', name )
  if m is not None: files.append( [ m.group( 1 ), name ] )

# sort by name without the XXXX- prefix
files.sort( key = lambda x: x[0] )

# use 2001 as the first prefix number
num = 2001

# print or rename
if args.rename:
  for pair in files:
    os.rename( pair[1], f"{num}-{pair[0]}" )
    num = num + 1
  
  print( f"{len( files )} files renamed." )
else:
  print( "Following renames would happend if --rename option was used:" )
  
  for pair in files:
    print( f"{pair[1]} -> {num}-{pair[0]}" )
    num = num + 1
