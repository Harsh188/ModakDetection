# ModakDetection

## Summary ##

When given the task of having to develop a modak detection software using tensorflow/keras/pytorch, I was first overwhelemed since I had no prior knowledge with working with such libraries. I decided that this program would behave somewhat similar to the face-recognition software I wrote in openCV and decided to take up the challange. A majority of the first day was spent reasearching about object-detection using tensorflow as well as getting it set up on my laptop. This was also the longest process since I was trying to develop a base model in my head on how to proceed with the assignment. After finding a tutorial on youtube I decided to follow his steps inorder to create my own modak detection software while following his guidelines. This is where I ran into several issues with the new Tensorflow 2.0 update. After going through github issues and stackover flow I managed to solve a majority of the software problems. Little did I know that when it came time for testing, the test.py file I was using had several compatiability issues. Overall, I would say that this assignment helped me learn a lot of new things. Although I failed to get the model working on time, I will surely be working on this project trying to get it to work.

## Steps: ##

### 1. Data Collection ###

#### Step1: Downloading images ####

To collet images for training and testing, I used a chrome extention to download all of the image results for "modak"
After doing so I transfered about 20% of the images gathered into the test folder and the rest into the train folder.

#### Step2: Labeling images ####

To label all of the images I used the labelImg software on github. The link to that can be found here: https://github.com/tzutalin/labelImg

#### Step3: xml to csv #### 

The contents of the labeled images were all stored in xml files. In order to use these points indicating the location of the object, I had to convert all of the xml files to csv. I used a python script to achive this task.

### 2. Augmentation ### 

A majority of the images from google were already repeats of themselves in different orientations. Inorder to save time I decided to skip the process and move on to the training.

### 3. Training the model ###

#### Step1: Model selection ####

In order to make it easy on myself, I decided to use a pretrained rcnn model. I valued accuracy more than speed since I was making a specific object detection model.

#### Step2: Training ####

When it came time to train my model, I ran into several software issues. I tried to use TF2 with existing github libraries to train my model however TF2 was not compatible with any of the code provided. 

### 4. Tuning the model ###