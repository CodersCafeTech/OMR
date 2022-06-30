# OMR

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

<img src = "https://github.com/CodersCafeTech/OMR/blob/main/assets/Answer_Key.jpg" width="400px" height="px">
|:--:| 
| **Answer Key** |

|![Answer_Key_Coordinates.jpg](https://github.com/CodersCafeTech/OMR/blob/main/assets/Answer_Key_Coordinates.jpg)|
|:--:| 
| **Answer Key With Coordinates** |

|![Answer_Sheet.jpg](https://github.com/CodersCafeTech/OMR/blob/main/assets/Answer_Sheet.jpg)|
|:--:| 
| **Answer Sheet** |

|![Answer_Sheet_Coordinates.jpg](https://github.com/CodersCafeTech/OMR/blob/main/assets/Answer_Sheet_Coordinates.jpg)|
|:--:| 
| **Answer Sheet With Coordinates** |

|![Final_Marks.jpg](https://github.com/CodersCafeTech/OMR/blob/main/assets/Final_Marks.jpg)|
|:--:| 
| **Final Marks** |

<img src = "https://github.com/CodersCafeTech/OMR/blob/main/assets/Final_Marks.jpg" width="300px" height="300px">








