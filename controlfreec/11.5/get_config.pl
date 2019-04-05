#!/usr/bin/perl

die  print "perl $0 <length> <chrdir> <normal_bam> <tumor_bam><threads>\n" unless @ARGV==5;

$length=shift;
$chrdir=shift;
$normal=shift;
$tumor=shift;
$threads=shift;

open OUT,">file.cfg";
print OUT "[general]\nchrLenFile = $length\nploidy = 2\nchrFiles = ./GRCh38_everyChrs\nmaxThreads = $threads\noutputDir = ./\nsambamba = /usr/local/bin/sambamba\nsamtools = /usr/bin/samtools\ncoefficientOfVariation = 0.062\n\n[sample]\nmateFile = $tumor\ninputFormat = BAM\nmateOrientation = FR\n\n[control]\nmateFile = $normal\ninputFormat = BAM\nmateOrientation = FR\n";