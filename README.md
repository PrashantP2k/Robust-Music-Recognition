
**Team Name**:
<span style="font-family: 'Papyrus';"> Kurtosis </span>

**Team Members**:
* Prashant Pandey 190108040 EEE bachelors
* Manchikatla Navya Sri 190102050 ECE bachelors
* Chanshu Kumar 190102019 ECE bachelors
* Chelsi Rawat 190101031 CSE bachelors
* Parag Panigrahi 190101111 CSE bachelors

**Project Title**:
Robust Music Recogniction

**Objective**:
The objective of this project is to recognize songs from small recorded clips using signal processing techniques, with the aim of developing an automated song system.

**Background**:
Often times when we attend some public event, we come across someone playing some songs on speakers. Sometimes we wish to know which song is being played. In order to do that, there is an application by the name of [Shazam](https://www.shazam.com/home). Shazam calculates the spectrogram of the recoded audio, performs acoustic fingerprinting on it and then creates a time-invariant hash-map to decide which song it is from the database.

We decide to use more signal processing to create a more robust audio recognition system. Shazam will not be able to recognize songs in low SNR environments. Also, if the recorded audio has added effects, as are added in songs nowadays, then Shazam fails to recognize such songs.

**Methodology**:
We will develop two adaptive filters ([1]):

1. White noise remover.
1. Pink noise remover.

We will take the dataset of songs, add the following effects to them by making their copies:

1. Convolving with different audio impulse responses to simulate different environments.
1. Adding white and pink noises of different amplitudes.
1. Adding various effects like delay, reverb and distortion by creating even more copies.

This will be our new dataset upon which training will be performed.

Recorded audio will go through white and pink noise filters first. Then, we will calculate its spectrogram and identify acoustic fingerprints. Now, we feed these fingerprints into a deep neural network which will tell us the index of the song which that audio clip most likely corresponds to.

**Deliverables**:
* A .ipynb notebook detailing the variability analysis of songs with added effects and the development of the signature recognition system.
* A GitHub repository containing the source code and documentation of the project.
* An oral presentation in class.

**Dataset to be used**:
* We have our own dataset of about 200 GB of songs which we shall be using for this project.

**References**:
1. Ahmed, S., Afroz, F., Tawsif, A., & Huq, A. (2015). CANCELLATION OF WHITE AND COLOR NOISE WITH ADAPTIVE FILTER USING LMS ALGORITHM.
