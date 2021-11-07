# DiRe Committees

Welcome to the world of DiRe committees!

This repository contains code for executing the heuristic algorithm developed to simulate a DiRe Committee election, which guarantees diversity *and* representation in multiwinner elections.

The goal of having a DiRe committee election is to select a committee by specifying diversity and representation constraints and a voting rule in settings where candidates are divided into groups over one or more attributes (e.g., "male" and "female" candidates over "gender" attribute) and voters are divided into predefined population over one or more attributes (e.g., "California" and "Illinois" voters over "state" attribute), which may or may not be same as the candidate attributes.

To execute your own election, run Code/home.ipynb.

To execute your own election in a controlled environment, run Code/home.ipynb in a Docker environment.
* [Instructions to install Docker on Mac](https://docs.docker.com/desktop/mac/install/)
* [Instructions to install Docker on Windows](https://docs.docker.com/desktop/windows/install/)
* [How to run Jupyter Notebook on Docker](https://towardsdatascience.com/how-to-run-jupyter-notebook-on-docker-7c9748ed209f)

Once the setup is done and you are running the jupyter notebook in a setting of your choice, our simulation allows you to specify:

* the number of candidates
* the number of voters
* size of the committee
* multiwinner voting rule

Next, generate the synthetic preferences by specifying the cohesiveness factor between 0 and 1; 0 being totally cohesive and 1 being the least cohesive.

Finally, specify:
* the number of candidate attributes, groups per attribute, and the corresponding diversity constraints
* the number of voter attributes, populations per attribute, and the corresponding representation constraints

To generate figures, execute the notebooks in the "Figures" folder.
