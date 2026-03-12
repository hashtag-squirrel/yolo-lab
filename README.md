# Object Detection using YOLO

This project was developed for educational purposes.

The main objective is to gain hands-on experience with the end-to-end workflow of a real computer vision project. This includes dataset collection, annotation, model training, and evaluation in a collaborative development environment.

The model is trained to detect three everyday objects:

- red cup
- blue bottle
- phone

## Dataset collection

Images for the dataset were collected from multiple sources in order to increase variability and improve the robustness of the trained model.

For objects that were easily accessible, such as the blue bottle and the phone, a large number of images were captured manually using different devices and under varying conditions. This includes variations in lighting, background clutter, object orientation, scale, and distance from the camera.

To further expand the dataset and introduce additional visual diversity, publicly available images were gathered from online sources such as [Pexels](https://www.pexels.com/), [Unsplash](https://unsplash.com/), and [Pixabay](https://pixabay.com/), as well as through Google Image Search.

Combining self-captured and externally sourced images helped ensure a broader distribution of visual contexts and reduced the risk of overfitting to a narrow set of environments.

At a later stage, we also added a second dataset with augmented images from Roboflow to see if this would perform better.

## Labelling of images in the dataset

All images in the dataset were annotated using [Roboflow](https://roboflow.com/).

Manual annotation was used for the entire dataset to ensure consistent labeling quality across all classes. In most cases, objects were annotated using axis-aligned bounding boxes, which is the standard annotation format for YOLO-based object detection models.

In a small number of images where objects overlapped significantly or had irregular visible shapes, polygon segmentation was used during annotation to more accurately capture the object extent. These annotations were later converted to bounding box representations for training.

This mixed annotation approach helped improve labeling precision while maintaining compatibility with the YOLOv8 training pipeline.

### Examples of labelled images

Original image                            |  Labelled image
:----------------------------------------:|:-------------------------:
![Unlabelled phone image](docs/205.jpg)   |  ![Labelled phone image](docs/205-labelled.png)
![Unlabelled cup image](docs/089.jpg)     |  ![Labelled cup image](docs/089-labelled.png)
![Unlabelled bottle image](docs/113.jpg)  |  ![Labelled bottle image](docs/113-labelled.png)

## Training results

We tried training our model for different numbers of epochs, ranging from 3 for the initial tests up to 100 epochs. As expected, the performance differed vastly between the different tries.

### Confusion matrix analysis

Dataset   | 20 epochs                                       |  50 epochs                                      |  100 epochs
:--------:|:-----------------------------------------------:|:-----------------------------------------------:|:-------------------------:
Original  | ![20 original](docs/cm-20epochs-original.png)   | ![50 original](docs/cm-50epochs-original.png)   |  X
Augmented | ![20 augmented](docs/cm-20epochs-augmented.png) | ![50 augmented](docs/cm-50epochs-augmented.png) | ![100 original](docs/cm-100epochs-augmented.jpg)

To evaluate the effect of training duration and data augmentation, several training runs were performed using different numbers of epochs. Experiments were conducted on both the original dataset and an augmented version of the dataset. Training was carried out for 20 and 50 epochs on the original dataset, and for 20, 50, and 100 epochs on the augmented dataset.

1. Performance on the original dataset

    When training on the original dataset, the model shows moderate class recognition performance after 20 epochs. The confusion matrices indicate that the model is already able to correctly detect bottles and cups in a significant portion of cases, while phone detection remains more challenging. A relatively large share of objects is still classified as background, which suggests that the model has not yet learned sufficiently robust object representations.

    Increasing the training duration to 50 epochs improves class discrimination slightly. The model becomes more confident in detecting cups and bottles, and the number of correct detections increases. However, confusion with the background class remains a major source of error. This indicates that the limited variability of the original dataset may restrict further improvements, even with longer training.

2. Performance on the augmented dataset

    Training on the augmented dataset leads to more stable and generally improved performance. After 20 epochs, the model already shows comparable or better recognition rates than the original dataset at the same training length. Data augmentation appears to help the model generalize better to different object appearances and environments.

    At 50 epochs, the confusion matrices show clearer separation between classes. In particular, cup detection improves significantly, and the model makes fewer background misclassifications compared to earlier runs. Bottle recognition remains relatively consistent, while phone detection still presents some difficulty, likely due to higher visual variability and smaller object size in some images.

    Extending training to 100 epochs further strengthens performance for certain classes, especially the cup class, which achieves the highest correct classification rates in the experiments. However, the improvement is not uniform across all classes. Some confusion between phones and background remains, suggesting that additional data or more targeted augmentation strategies may be required.

#### General observations

Across all experiments, the background class represents the dominant source of misclassification. This is common in object detection tasks when objects appear small, partially occluded, or under challenging lighting conditions. The results suggest that both dataset diversity and sufficient training time are important factors for achieving robust detection performance.

Overall, the augmented dataset combined with longer training provides the best results. These findings highlight the importance of data augmentation in improving model generalization and reducing overfitting when working with relatively small custom datasets.

### Comparison results

## Performance in real world scenarios

