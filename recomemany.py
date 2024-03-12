import face_recognition
import os
picture_of_me = face_recognition.load_image_file("am.JPG")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!


for filename in os.listdir('faces'):

    unknown_picture = face_recognition.load_image_file("faces/"+ filename)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

    if results[0] == True:
        print("TRUE! "+ filename)
    else:
        print("FALSE! "+ filename)

    
 