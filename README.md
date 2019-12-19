# Heart Beat

Heart Beat is a data visualization, sonification, and analysis of infant mortality rates throughout time. I created this webpage as an entry in Stanford's CS109 project competition. 





When you visit the webpage you can first get examine the current state of infant mortality rates worldwide.
![Alt Text](https://github.com/leonbi100/heart_beat/blob/master/data/2019-12-18%2020.04.14.gif)





Next, I allow the user to listen to a sonic representation of infant mortality rate over time where the higher the worldwide the infant mortality rate the faster the heartbeat. The results are chilling!
![Alt Text](https://github.com/leonbi100/heart_beat/blob/master/data/2019-12-18%2019.58.45.gif)

The meat of the project comes next when you can condition on any specific year or metric (currently only supporting GDP and CO2 emissions) to get frequencies of this condition in a 3D representation.
![Alt Text](https://github.com/leonbi100/heart_beat/blob/master/data/2019-12-18%2020.09.53.gif)

Finally we use maximum likelihood estimation to predict the best random variable distribution that best models the data we have conditioned on.
