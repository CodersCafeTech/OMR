# Optical Mark Recognition (OMR) with FOMO
![OMR_DEVICE.jpg](https://usercdn.edgeimpulse.com/project116250/dfa6e4c14eb869241178963e713b0c6650d78433206ca9b0c8af02a33aa2476c)
## Story
Are you fed up with slow and expensive OMR readers? We've got your back. FOMR is a fast, reliable, and cheap OMR reader that can read your OMR sheet faster than the blink of your eye.

FOMO (Faster Objects, More Objects) is a novel machine learning algorithm that brings object detection to highly constrained devices. So let's use FOMO to build a cheap, faster, and flexible OMR reader. 

## Why FOMO?
FOMO is apt in our scenario for these reasons,
1. FOMO works better if the objects have a similar size, and in our case, all the marked dots have a very similar size
2. FOMO is designed to be small and amazingly fast, so we can use a microcontroller with limited processing capacity, which makes the device cheap and faster

## How Does It Work?
To make the FOMR flexible, we use a marked answer key to identify the answers. Those answers are compared with other answer sheets to find the marks in other answer sheets. 

To read the marks,
1. Place your answer key and read the answers.
2. Identify the position of answers in terms of co-ordinates using FOMO
3. Now place the answer sheet and read the marked options
4. Identify the position of markings in terms of co-ordinates
5. Compare the position of each marking to the postion of answers in the answer key
6. For each correct detection, add the marks
7. Print the final marks

![Answer_Key.jpg](https://usercdn.edgeimpulse.com/project116250/16da0834bcff2cf66f20db44e70c5912864699bdf69b4887e187586132efd062)

![Answer_Key_Coordinates.jpg](https://usercdn.edgeimpulse.com/project116250/9003ab586e4065f533c54296cc3cd2392b7a36407a495c16dc749ee62f3915a4)

![Answer_Sheet.jpg](https://usercdn.edgeimpulse.com/project116250/a3c0da1f66d8534215d4a1ea9f06eaa14072fa0da85c6708ce266af6862bbb2a)

![Answer_Sheet_Coordinates.jpg](https://usercdn.edgeimpulse.com/project116250/3d9bfa7a3001f3703a0233f98870b4cfd3e1e3119c899588be2755e6332a1af5)

![Final_Marks.jpg](https://usercdn.edgeimpulse.com/project116250/ed708959d7c2eeb49e6041cb91c9f69eb45fb06bb1658709ea378fed1a6bcb11)


## Model Generation
Every machine learning model needs data,  for acquiring data we stretched to the data acquisition tab.
For data sampling , we used a Raspberry pi with the camera module.
Actually here we are going to make a object detection model that can recognise black dot in the sheets.For getting more accuracy ,we also collected the individual dots(zoomed image) in addition to the groups and also we tried different orinetations.So we sampled 70 images(consist of 375 items) and is split in between test and training set.  

![Data.png](https://usercdn.edgeimpulse.com/project116250/fb285017d4d439566591af1abdcaee43dbbb5ba20ee5936f63d3bb017472f957)  

After the data acquisition, we started labelling the collected data.The fact is that here we have only one class in this model.The data acquisition is over, it's time for feature extraction.To generate features, we first need to create an impulse. For this project we have been using 96x96 images and resized by means of "Fit to shortest axis".
Then we added a processing block and learning block to complete the impulse.  

![impulse.png](https://usercdn.edgeimpulse.com/project116250/9eb34ac176c0815c5c7f665ee85d3fb34d62447c32f0883d2c42ae9ae10416df)   

We used gray scale image as the color depth for configuring the processing block and we think the FOMO won't work on RGB data. Then we generated the features for the data. The feature explorer window is shown below. 

![feature_explorer.png](https://usercdn.edgeimpulse.com/project116250/74be0df1ecd1f3b75bfd97577c14aa2727a69644dc4b30a2e53895346b66f093)  

With all data processed it's time to start training our FOMO model . The model will take an image as input and output objects detected using centroids. For our case, it will show centroids of dots detected on the mark sheets.These are our neural network settings.     

![neural network settings_.png](https://usercdn.edgeimpulse.com/project116250/e7a6fb1f6147b6bc0d6279e321246a04d33982cb5c9abd37a4afd60815b7df5b)

We have trained the FOMO object detection model with a accuracy of 87%. The below confusion matrix shows our model is Good Fit.   

![confusion matrix.png](https://usercdn.edgeimpulse.com/project116250/720efb1c38cc5f8179cd024f89efe16134bf07fd8a76971ed3c4f6b3d83ced32)

With the model trained let's try it out on some test data. When collecting the data we split the data up between a training and a testing dataset. The model was trained only on the training data, and thus we can use the data in the testing dataset to validate how well the model will work in the real world. This will help us ensure the model has not learned to overfit the training data, which is a common occurrence. To validate our model, we will go to Model testing and select Classify all.  
The results are surpising !! We hit 100% accuracy on real world data which shows that it is a functional model.    

![model_testing.png](https://usercdn.edgeimpulse.com/project116250/5457fd6b20301eb9a6c7b0b0b3f4a1e7fd67b0fcb165f5ec5de772ebba7b0fda)

## Hardware        
The Raspberry Pi 3B is the powerful development of the extremely successful credit card-sized computer system. The brain of the system is Raspberry Pi. All major processes are carried out by this device.  

![rpi3_3_cnkiu6fD0V.jpeg](https://usercdn.edgeimpulse.com/project116250/98f47cacf0569387b1d1c43ba2e36dc56bebe0f22f0f24dd880fadfe46954300) 

To set this device up in Edge Impulse, run the following commands:  
``sudo apt update
  sudo apt upgrade
  curl -sL https://deb.nodesource.com/setup_12.x | sudo bash -
  sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools  gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
  npm config set user root && sudo npm install edge-impulse-linux -g --unsafe-perm ``

Also we enabled the camera by running `` sudo raspi-config`` which is actually a prime thing to do.  
Here I am using the REES52 5 Megapixel 160° degrees Wide Angle Fish-Eye Camera for the object detection. Due to its high viewing angle, it can cover more area than the normal camera module.  

![camera_module_VK6TOIfB2N.jpg](https://usercdn.edgeimpulse.com/project116250/28703b8e3c37675afd7e47942c28987af0418927e7a4ace873240854152e339b)  

We can connect the raspberry pi to the edge impulse by running this command ``edge-impulse-linux``. In this way we collected the data for the model generation. 

Then we used Linux sdk for running the model in the raspberry pi. For running the linux sdk put these commands in the terminal.  
`` sudo apt-get install libatlas-base-dev libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev    pip3 install edge_impulse_linux -i https://pypi.python.org/simple ``  
For powering the Raspberry Pi we used 5V 2A adapter.

### Device Setup    

![OMR2.jpg](https://usercdn.edgeimpulse.com/project116250/7f0517b2c3be7184470927a13174445667bc8777ab53522e385eb763b2fca1aa)

For setting up the OMR reader, we repurposed the old case used in AutoBill project. That's actually suits very well for this project. For proper reading of the mark sheets we fixed the camera module on the top side. We also marked the space for the mark sheets underneath the camera module. All the sheets would be placed in the markings, other wise the logic won't work as expected. In this project we made a custom size OMR sheets in which the object detection works very well.  

![device3.jpg](https://usercdn.edgeimpulse.com/project116250/f893cacb4d1554c1f38e73f0806e5d133ea34f9da2afe9c1df98c4454dc4933e)   
![device4.jpg](https://usercdn.edgeimpulse.com/project116250/0dea973ccfe79234548ae0f6316fd8b713837ae013f96dd0a2e0b529c45aaa24)

## Working Demo

[![Click to Play](https://usercdn.edgeimpulse.com/project116250/9921b5f10c4b8ad5af9fcf92364f8d299ae3826a3e3a8894047f42b9914fc5e9)](https://vimeo.com/725731228)

## Code

All the source files are availabe in the github repository. Grab it from [here](https://github.com/CodersCafeTech/OMR)
