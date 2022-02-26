#!/bin/bash
# Download Deeplearning Models

output_dir=cached
mkdir -p $output_dir

# Kobert 
wget -P $output_dir https://www.dropbox.com/s/xpb2jmpjdzmo64m/kobert_monologg.pt

# Others...