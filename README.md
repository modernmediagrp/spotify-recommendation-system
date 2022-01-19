![banner](./images/knobs.jpeg)
# *Live DJ Assist: Using Spotify to Build a Recommendation System for DJ'ing Electronic Music*
Author: [Paul Lindquist](https://www.linkedin.com/in/paul-lindquist/)

## Background
Electronic music has a great speed advantage. The music is typically created with computers and plugins rather than instruments and live recordings. It's usally distributed digitally, opting for high-quality .wav, .aiff and .mp3 files over vinyl or CDs. As such, thousands of new songs are released every day. This presents a challenge for any DJ or music curator seeking to keep their library current without drowning in new releases. To complicate matters further, the music isn't centralized. Releases are sold on numerous online stores like [Beatport](https://www.beatport.com/), [Juno Download](https://www.junodownload.com/), [Traxsource](https://www.traxsource.com/) and [Bandcamp](https://bandcamp.com/) or given away for free on platforms like [Soundcloud](https://soundcloud.com/). Crate digging has long since moved to the digital world and it's easy to get overwhelmed.

For years, and like any other genre of music, electronic music has been categorized by sub-genres.

## Overview
This was very much a passion project. I've DJ'ed electronic music for 13 years and have been a fan of the genre since the 90s.

## Objective
TBD

## Data
Data was aggregated from multiple sources:
- API calls of Spotify's [Web API](https://developer.spotify.com/documentation/web-api/) using their [genre seeds](https://developer.spotify.com/console/get-available-genre-seeds/)
- A [raw dataset](https://www.kaggle.com/nikitricky/every-noise-at-once?select=songs.csv) of approx. 500k songs referencing [Every Noise at Once](https://everynoise.com/)'s *[The Sound of Everything](https://open.spotify.com/playlist/69fEt9DN5r4JQATi52sRtq)* Spotify playlist
- [Multiple](https://www.kaggle.com/christinobarbosa/spotify-dataset?select=Spotify_dataset.csv) [Kaggle datasets](https://www.kaggle.com/vatsalmavani/spotify-dataset) that contained necessary genre tagging and audio feature listings (energy, danceability, etc.)

## Methods
TBD

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
