![banner](./images/knobs.jpeg)
# *Live DJ Assist: Using Spotify to Build a Recommendation System for DJ'ing Electronic Dance Music*
Author: [Paul Lindquist](https://www.linkedin.com/in/paul-lindquist/)

## Background
Electronic dance music is overwhelmingly created with computers and plugins rather than instruments and live recordings. It's typically distributed digitally, opting for high-quality .wav, .aiff and .mp3 files over CDs and vinyl. As such, thousands of new songs are released every day. This presents a challenge for any DJ or music curator seeking to keep their library current without drowning in new releases. To complicate matters further, the music isn't centralized. Releases are sold on numerous online stores like [Beatport](https://www.beatport.com/), [Juno Download](https://www.junodownload.com/), [Traxsource](https://www.traxsource.com/) and [Bandcamp](https://bandcamp.com/) or given away for free on platforms like [Soundcloud](https://soundcloud.com/). Crate digging has long since moved to the digital space and it's easy to get overwhelmed.

Like any other genre of music, electronic dance music has, for years, been categorized by sub-genres. Generally, the sub-genres were defined by features like tempo (beats per minute/BPM), mood and the instrument samples used. Orchestral strings weren't heavily utilized in Jungle music, Trance rarely dipped below 122 beats per minute, etc. But as the music evolved and artists implemented elements from different sub-genres, classifying songs became both cumbersome and inaccurate. There needed to be a new way to analyze songs irrespective of sub-genres. Enter Spotify...

After acquiring music intelligence and data platform *The Echo Nest* in 2014, Spotify began integrating algorithm-based audio analysis, resulting in songs being tagged with audio features such as valence, energy, tempo, etc. Through their [Web API](https://developer.spotify.com/documentation/web-api/), they permit the extraction of these features when calling songs to build out datasets. Along with the tagged sub-genre, this allows for a more detailed categorization and comparison of songs.

## Overview
This project solely focused on electronic music within Spotify's database. Common sub-genres categorized by both [Every Noise at Once](https://everynoise.com/) and Spotify's own [genre seeds](https://developer.spotify.com/console/get-available-genre-seeds/) within their [recommendation API](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-recommendations) were used to narrow the final dataset.

Spotify was chosen as the singular data-gathering platform for a few reasons:
1. It's the world's most popular music streaming service with a database of over 70 million songs
2. The algorithm-based audio analysis (song features) provided unmatched opportunity for song comparison and recommendation
3. Their [Web API](https://developer.spotify.com/documentation/web-api/) is accessible and well-documented
4. Songs are tagged with identifiers like ID and URI for organized tracking

The following Spotify audio features were extracted and used as features for determining similarity for recommendation. Refer to the [documentation](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-audio-features) for an in-depth explanation of each:
- Acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo (BPM) and valence

Musical features like key and mode were purposefully omitted because there are separate applications (e.g. [Mixed in Key](https://mixedinkey.com/)) that can hard-tag songs with that information, making it available during song selection while DJ'ing. Also, and perhaps more importantly, making recommendations based on the key can lead to songs sounding too similar. 

I served as my own stakeholder for this project. Personal domain knowledge was used to determine validity of the recommendations. I've DJ'ed electronic music for 13 years and have been a fan of the genre since the 90s.

## Objective
TBD

## Data
Data was aggregated from multiple sources:
- API calls of Spotify's [Web API](https://developer.spotify.com/documentation/web-api/) using their [genre seeds](https://developer.spotify.com/console/get-available-genre-seeds/)
- A [raw dataset](https://www.kaggle.com/nikitricky/every-noise-at-once?select=songs.csv) of approx. 500k songs referencing [Every Noise at Once](https://everynoise.com/)'s *[The Sound of Everything](https://open.spotify.com/playlist/69fEt9DN5r4JQATi52sRtq)* Spotify playlist
- [Multiple](https://www.kaggle.com/christinobarbosa/spotify-dataset?select=Spotify_dataset.csv) [Kaggle datasets](https://www.kaggle.com/vatsalmavani/spotify-dataset?select=data) that contained necessary genre tagging and audio feature listings (energy, danceability, etc.)

## Methods
This project exclusively used content-based filtering to build a recommendation system. Similarity was calculated using K-Nearest Neighbors (KNN), cosine similarity and sigmoid kernel. Exploratory data analysis and visualizations were conducted on the final, cleaned data.

## Results
TBD

## Conclusions
TBD

## Next Steps
TBD

## For More Information
Please review the full analysis in my Jupyter Notebook or presentation deck.

For additional questions, feel free to [contact me](https://www.linkedin.com/in/paul-lindquist/).

## Respository Structure
```
├── data                                <- Source data .csv files
├── images                              <- Exported Notebook visualizations
├── README.md                           <- The top-level README for reviewers of this project
├── main_notebook.ipynb                 <- Technical and narrative documentation in Jupyter Notebook
└── project_presentation.pdf            <- PDF version of project presentation
```
