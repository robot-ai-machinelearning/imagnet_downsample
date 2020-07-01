from PIL import Image
from argparse import ArgumentParser
import os
from multiprocessing import Pool

alg_dict = {
    'lanczos': Image.LANCZOS,
    'nearest': Image.NEAREST,
    'bilinear': Image.BILINEAR,
    'bicubic': Image.BICUBIC,
    'hamming': Image.HAMMING,
    'box': Image.BOX
}

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('-i', '--in_dir', help="Input directory with source images", required=True)
    parser.add_argument('-o', '--out_dir', help="Output directory for resized images", required=True)
    parser.add_argument('-s', '--size', help="Size of an output image (e.g. 32 results in (32x32) image)",
                        default=32, type=int)
    parser.add_argument('-a', '--algorithm', help="Algorithm used for resampling: lanczos, nearest,"
                                                  " bilinear, bicubic, box, hamming",
                        default='lanczos')

    parser.add_argument('-r', '--recurrent', help="Process all subfolders in this folder (1 lvl deep)",
                        action='store_true')
    parser.add_argument('-f', '--full', help="Use all algorithms, create subdirectory for each algorithm output",
                        action='store_true')
    parser.add_argument('-e', '--every_nth', help="Use if you don't want to take all classes, "
                                                  "if -e 10 then takes every 10th class",
                        default=1, type=int)
    parser.add_argument('-j', '--processes', help="Number of sub-processes that run different folders "
                                                  "in the same time ",
                        default=1, type=int)
    args = parser.parse_args()

    return args.in_dir, args.out_dir, args.algorithm, args.size, args.recurrent, \
           args.full, args.every_nth, args.processes

def str2alg(str):
    str = str.lower()
    return alg_dict.get(str, None)

