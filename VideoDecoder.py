import cv2
import logging
import os
import random
import string
def rand_string(length):
    """Generates a random string of numbers, lower- and uppercase chars"""
    rand_str = ''.join(random.choice(
            string.ascii_lowercase
            + string.ascii_uppercase
            + string.digits)
            for i in range(length))
    return rand_str

def length_of_video(video_path):
    """small helper function"""
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length

def extracting_frames(video_path, save_path, skip_frames = 30):
    """
    Extract frames from video and save as jpg
    args
    ---

    video_path : path to video_path
    save_path : save_directory for extracted imags
    skip_frames: save every "X" frames

    """

    print('******ENTERING EXTRACTING PHASE**********')

    #C:\temp\video.mp4 = C:temp\.video.mp4
    _, file_name = os.path.split(video_path)

    #alex.mp4 = alex, .mp4
    file_name_without_ext = os.path.splitext(file_name)[0]

    # check length
    length = length_of_video(video_path)
    if length == 0:
        print('Length is 0, exiting extracting phase')
        return 0
    print('Length is ' + str(length) + ' frames')

    cap = cv2.VideoCapture(video_path)
    count = 0 #keep count of frames
    random_string = rand_string(5) # for naming

    #text first frame : matrix
    ret, frame = cap.read() #ret & frame returned correctly
    test_file_path = os.path.join(
        save_path,
        file_name_without_ext[:6]+\
        '{}_{}.jpg'.format(random_string, count))
    print('Test_file_path =', test_file_path)

    success = cv2.imwrite(test_file_path, frame)  #creates and renames new image within the path
    if success == True:    #if os.path.isfile(test_file_path):

        print('Saving Test Frame was Successful,' +
            'Continuing Extraction Phase')


        count += 1
        while ret:
            ret, frame = cap.read()
            if ret and count % skip_frames == 0:
                cv2.imwrite(os.path.join(
                    save_path,
                    file_name_without_ext[:6]+
                    '{}_{}.jpg'.format(random_string, count)), frame)
                count+= 1
                print(count)
            else:
                count += 1
    else:
        print('Problem with Saving Test Frame cv2 encoding, cannot save file')
        return 0

    cap.release()
    print('*********FINISHED EXTRACTION***********')

if __name__ == "__main__":
    public_movies = ["glaive - detest me (official video).mp4"]
    save_path = "output"
    for movie in public_movies:
        print('movie: ' + movie)
        extracting_frames(movie, save_path, skip_frames = 30)
