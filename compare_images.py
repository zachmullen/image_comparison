import argparse
import json
import nibabel
import numpy as np


def compare_images(test, truth):
    test_nib_img = nibabel.load(test)
    truth_nib_img = nibabel.load(truth)
    test_img = test_nib_img.get_data()
    truth_img = truth_nib_img.get_data()

    test_img = test_img.astype(np.bool)
    truth_img = truth_img.astype(np.bool)

    intersection = np.logical_and(test_img, truth_img)
    union = np.logical_or(test_img, truth_img)
    jaccard = intersection.sum() / float(union.sum())

    return {'Jaccard': jaccard}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='compare_images', description='compute similarity of two binary images')

    parser.add_argument('--test', help='The path to the test image.', required=True)
    parser.add_argument('--truth', help='The path to the ground truth image.', required=True)
    args = parser.parse_args()

    print(json.dumps(compare_images(args.test, args.truth)))
