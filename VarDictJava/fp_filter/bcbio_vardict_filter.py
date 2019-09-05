#/usr/bin/env python2
import sys
import argparse
import gzip
import utils


def is_sex(chrom):
    return chrom in ["X", "chrX", "Y", "chrY"]

def depth_freq_filter(line, tumor_index, aligner):
    """Command line to filter VarDict calls based on depth, frequency and quality.
    Looks at regions with low depth for allele frequency (AF * DP < 6, the equivalent
    of < 13bp for heterogygote calls, but generalized. Within these calls filters if a
    calls has:
    - Low mapping quality and multiple mismatches in a read (NM)
        For bwa only: MQ < 55.0 and NM > 1.0 or MQ < 60.0 and NM > 2.0
    - Low depth (DP < 10)
    - Low QUAL (QUAL < 45)
    Also filters in low allele frequency regions with poor quality, if all of these are
    true:
    - Allele frequency < 0.2
    - Quality < 55
    - P-value (SSF) > 0.06
    """
    line = line.rstrip('\n')
    if line.startswith("#CHROM"):
        headers = [('##FILTER=<ID=LowAlleleDepth,Description="Low depth per allele frequency '
                    'along with poor depth, quality, mapping quality and read mismatches.">'),
                   ('##FILTER=<ID=LowFreqQuality,Description="Low frequency read with '
                    'poor quality and p-value (SSF).">')]
        return "\n".join(headers) + "\n" + line
    elif line.startswith("#"):
        return line
    else:
        parts = line.split("\t")
        sample_ft = {a: v for (a, v) in zip(parts[8].split(":"), parts[9 + tumor_index].split(":"))}
        qual = utils.safe_to_float(parts[5])
        dp = utils.safe_to_float(sample_ft.get("DP"))
        af = utils.safe_to_float(sample_ft.get("AF"))
        nm = utils.safe_to_float(sample_ft.get("NM"))
        mq = utils.safe_to_float(sample_ft.get("MQ"))
        ssfs = [x for x in parts[7].split(";") if x.startswith("SSF=")]
        pval = utils.safe_to_float(ssfs[0].split("=")[-1] if ssfs else None)
        fname = None
        if not is_sex(parts[0]) and dp is not None and af is not None:
            if dp * af < 6:
                if aligner == "bwa" and nm is not None and mq is not None:
                    if (mq < 55.0 and nm > 1.0) or (mq < 60.0 and nm > 2.0):
                        fname = "LowAlleleDepth"
                if dp < 10:
                    fname = "LowAlleleDepth"
                if qual is not None and qual < 45:
                    fname = "LowAlleleDepth"
        if af is not None and qual is not None and pval is not None:
            if af < 0.2 and qual < 45 and pval > 0.06:
                fname = "LowFreqQuality"
        if fname:
            if parts[6] in set([".", "PASS"]):
                parts[6] = fname
            else:
                parts[6] += ";%s" % fname
        line = "\t".join(parts)
        return line

# def _lowfreq_linear_filter(tumor_index, is_paired):
#     """Linear classifier for removing low frequency false positives.
#     Uses a logistic classifier based on 0.5% tumor only variants from the smcounter2 paper:
#     https://github.com/bcbio/bcbio_validations/tree/master/somatic-lowfreq
#     The classifier uses strand bias (SBF) and read mismatches (NM) and
#     applies only for low frequency (<2%) and low depth (<30) variants.
#     """
#     if is_paired:
#         sbf = "FORMAT/SBF[%s]" % tumor_index
#         nm = "FORMAT/NM[%s]" % tumor_index
#     else:
#         sbf = "INFO/SBF"
#         nm = "INFO/NM"
#     cmd = ("""bcftools filter --soft-filter 'LowFreqBias' --mode '+' """
#            """-e  'FORMAT/AF[{tumor_index}:0] < 0.02 && FORMAT/VD[{tumor_index}] < 30 """
#            """&& {sbf} < 0.1 && {nm} >= 2.0'""")
#     return cmd.format(**locals())

vcf = gzip.open(sys.argv[1])
for line in vcf:
    res = depth_freq_filter(line, 1, "bwa")
    print(res)
