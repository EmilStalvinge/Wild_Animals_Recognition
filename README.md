# Wild Animals Recognition

We have a number of camera traps set up in the swedish forest. Movement triggers
them and they take an image. 

<p align="center">
<img src="https://user-images.githubusercontent.com/50867974/116964542-0f8a3400-acac-11eb-8eb6-9b5a93ddc081.jpg" width="500">
</p>

<p align="center">
<img src="https://user-images.githubusercontent.com/50867974/116964539-0ef19d80-acac-11eb-87ba-550813e1ef87.jpg" width="500">
</p>

## A model was first pretrained on around 50k annotated images from different camera trap datasets
### Datasets used
<p align="center">
<img src="https://user-images.githubusercontent.com/50867974/116964938-fa61d500-acac-11eb-85fa-a6dd9dd201c4.png" width="500">
</p>

- ENA24 dataset. Yousif, Hayder and Kays, Roland and He, Zhihai, Dynamic Programming Selection of Object Proposals for Sequence-Level Animal Species Classification in the Wild, electronic dataset, IEEE Transactions on Circuits and Systems for Video Technology, viewed 06 February 2020
- ECCT18 dataset. Caltech Camera Traps-29, viewed 12 February 2020 <https://beerys.github.io/CaltechCameraTraps>
- Missouri dataset. Zhang, Z., He, Z., Cao, G., & Cao, W. (2016). Animal detection from highly cluttered natural scenes using spatiotemporal object region proposals and patch verification. IEEE Transactions on Multimedia, 18(10), 2079-2092, viewed 15 February 2020
- KTH DatasetHeydar Maboudi Afkham, Alireza Tavakoli Tar ghi, Jan-oluf Eklundh, and Andrzej Pronobis In Proceedings of the International Conference on Pattern Recognition (ICPR08), Tampa, FL, USA, viewed 28 January 2020 <http://www.csc.kth.se/~heydarma/Datasets.html>
- Google images. Google images, Google, viewed on 18 Febuary 2020 <https://www.google.com/search?q=moose+camera+trap&tbm=isch>

## Models trained
<p align="center">
<img src="https://user-images.githubusercontent.com/50867974/116965164-75c38680-acad-11eb-8e9d-1860adda6f87.png" width="500">
</p>

### Then applied to data from our cameras (see images above)
Transfer learning can be tricky. From the few samples we tried of our own data it wasclear that the best model did not work aswell on our own data. While it had a high accuracy on the training and test data-set the introduction of data from a slightly different source made it not work as well. As we had very few samples from our own data we where not able to train it enough to adapt on our cameras.
We have to wait for more data from our cameras to come.  Another problem can be our simple preprocessing The bounding boxes were of vastly different ratios between height and width. When the images were then resized to a 128x128 or 256x256 square image this would have led to distorted animals as they were stretched or squeezed some into a square.

