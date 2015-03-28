# movie-barcode

This python script can create a barcode given a movie or a video file. [Example](http://i.imgur.com/Xjhqn3s.jpg).

## Usage

<code>python movie_barcode.py video_filename </code>

The following parameters can be changed in source:

1. barcode_height - Defaults to 300. Change this to set the height of the barcode image manually.

2. output_file - Default behavior is to show the barcode image in a new window. Default output file is named "movie_barcode.jpg" and can be changed. <code> save_to_output_file</code> parameter needs to be set to <code>True</code>.

3. frame_skip - This parameter sets how many frames should be skipped between each target frame used to create to the barcode image. Default value is 10 and this should be changed to higher value for longer videos. Ideal value is 90 for a 2 hour long video.

