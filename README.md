
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
We will develop an adaptive filter ([1]):

1. Noise removal filter (Wiener filter).

We will take the dataset of songs, add the following effects to them by making their copies:

1. Convolving with different audio impulse responses to simulate different environments.
1. Adding white noise.
1. Adding various effects like delay, reverb and distortion by creating even more copies.

This will be our new dataset upon which training will be performed.

Recorded audio will go through the Wiener noise filter first. Then, we will calculate its spectrogram and identify acoustic fingerprints. Now, we feed these fingerprints into a deep neural network which will tell us the index of the song which that audio clip most likely corresponds to.

**Deliverables**:
* A .ipynb notebook detailing the variability analysis of songs with added effects and the development of the signature recognition system.
* A GitHub repository containing the source code and documentation of the project.
* An oral presentation in class.

**How to Use Files**:
* Convolution.py can be used to convolve any two "*.wav" files to create another one.
* Distortion.py can be used to add either tanh distortion or clipping distortion or both to any audio file.
* WeinerFilter.py can be used to filter out noise from any signal.
* "Robust Music Recognition.ipynb" is the main recognizer's implementation.
    * Create your own dataset of audio files in a "./Data" folder.
    * Create a "Train" folder inside it.
    * Copy the "Impulses" folder into the "Data" folder. Feel free to add your own impulse responses as well. Some good samples are available at [link 1](https://www.pro-tools-expert.com/production-expert-1/free-impulse-responses-excellent-for-sound-design-and-post-production), [link 2](https://github.com/RoyJames/room-impulse-responses), [link 3](https://bedroomproducersblog.com/2014/05/22/free-boss-gt-8-reverb-impulse-response-pack-animus-invidious/), [link 4](https://sonicstate.com/news/2023/03/31/free-impulse-response-pack-/) and so on...
    * Run the notebook.

**Dataset to be used**:
* We used our own dataset of 10 songs for this project.

**References**:
1. Ahmed, S., Afroz, F., Tawsif, A., & Huq, A. (2015). CANCELLATION OF WHITE AND COLOR NOISE WITH ADAPTIVE FILTER USING LMS ALGORITHM.
