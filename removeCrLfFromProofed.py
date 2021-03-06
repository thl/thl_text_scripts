# coding=utf-8
#
#  Removes line returns from originals of the proofed volucmes
#

from THLTextProcessing import THLSource, THLText, THLBibl  # Custom class for text processing


if __name__ == "__main__":
    for n in range(39, 104):
        fname = '{0}-FINAL-tags-cvd.txt'.format(str(n).zfill(3))
        baseurl = '/Users/thangrove/Documents/Project_Data/THL/DegeKT/ProofedVols/source-vols-latest/'
        infolder = baseurl + 'eKangyur_W4CZ5369-normalized/'
        outfolder = baseurl + 'eKangyur_W4CZ5369-normalized-nocr/'
        furl = infolder + fname
        srcobj = THLSource(furl)
        srcobj.removecrlf()
        fouturl = outfolder + fname
        print "Writing file is: {0}".format(fouturl)
        srcobj.writetext(fouturl)

