import cv2
import numpy as np
import sys


def compute_barcode(input_file, output_file, barcode_height, frame_skip, save_to_output_file):
    vidcap = cv2.VideoCapture(input_file)

    print "Processing video file %s. This may take a while depending on the size of the video or the system performance..." % (input_file)

    frame_count = 0
    success = True
    barcode = None

    while success:
        success, image = vidcap.read()
        if frame_count % frame_skip == 0:
            if success:
                resized_image = cv2.resize(image, (1, 600))
            if barcode is None:
                barcode = resized_image
            else:
                barcode = np.hstack((barcode, resized_image))
        frame_count += 1

    if save_to_output_file:
        cv2.imwrite(output_file, barcode)
        print "Processing complete! Barcode image saved in %s" % (output_file)
    else:
        cv2.imshow("Movie Barcode Generator", barcode)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print "Usage: python movie_barcode.py <video_file_name>"
    else:
        input_file = sys.argv[1]
        save_to_output_file = False
        output_file = "movie_barcode.jpg"
        barcode_height = 300
        frame_skip = 10  # Set higher number for longer videos

        compute_barcode(input_file, output_file, barcode_height, frame_skip, save_to_output_file)
