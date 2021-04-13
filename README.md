# Cardiac TdP Risk Stratification Modelling of Anti-Infective Compounds including Chloroquine and Hydroxychloroquine

Dominic G. Whittaker, Rebecca A. Capel, Maurice Hendrix, Xin Hui S. Chan, Neil Herring, Nicholas J. White, Gary R. Mirams, Rebecca-Ann B. Burton.

## Requirements

Processing and plotting the simulation data in this repository requires installation of python 3 and certain libraries within. We recommend installing packages and running the scripts in a virtual environment to avoid version conflicts. In order to do this, follow these steps:

- `virtualenv folder_name` (or `virtualenv --python=python3 folder_name` if you have both python 2 and 3). If `virtualenv` is not recognised you may need to call it as `python -m virtualenv folder_name` or (`python -m virtualenv folder_name`). If that doesn't work you may need to install virtualenv first with `pip install virtualenv`.
- activate the virtual environment with `source folder_name/bin/activate` (or `folder_name/Scripts\activate` on Windows)
- now get the source code from git: `git clone https://github.com/CardiacModelling/risk-stratification-anti-malarials.git`
- install the required packages by typing `pip install -r requirements.txt`

## Generating the data

The simulations in this paper use the [ApPredict](https://chaste.cs.ox.ac.uk/trac/wiki/ApPredict) tool. In order to facility reproducibility we have published the exact version of the tool used to Docker Hub. In order to generate the data used in the paper, install [Docker](http://docker.com/). If you are on Windows you may have to set Docker to use Linux containers. After installing Docker run the following command:

- `docker run -it cardiacmodelling/appredict-in-papers:brute_force_0.0.1 /bin/bash`

The first time you run this, this will download the relevant Docker image and it will log into a virtual environment where you can run the following commands: 

- `cd apps/ApPredict/`

We also recommend activating a screen session if using Linux as it may take many hours to generate the simulation data, which are produced by typing a command which tells ApPredict which ion channels to block and by which amount for each drug/combination. For example, the data for hydroxychloroquine are generated by typing

- `./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.25 --pic50-spread-herg 0.139 --pic50-cal 4.57 --pic50-spread-cal 0.181 --pic50-iks 5.03 --pic50-spread-iks 0.127 --plasma-conc-high 100 --plasma-conc-count 19 --plasma-conc-logscale True --no-downsampling True --credible-intervals 60 70 80 90 95 --brute-force 1000 --output-dir HCQ &> testoutput/HCQ.txt &`

which runs the simulation in detached mode and stores the data in `testoutput/HCQ/` and console output in `testoutput/HCQ.txt`. For a full list of the commands used to generate simulation data for all drugs and combinations see [commands](./commands). Once the data have been generated, inside the directory in which you wish to store the data (outside the Docker container) run:

- `docker container list` and note the `CONTAINER ID`
- `docker cp CONTAINER ID:/home/appredict/apps/ApPredict/testoutput .` 

For convenience we have already stored all of the simulation data in `testoutput`.

## Plotting the figures

In order to generate Figure 1 from the paper, simply type:

- `python Figure1.py` (or `python3 Figure1.py` if you have both python 2 and 3 installed).
- Figures 2 and supplementary Figures S1 and S2 can be rendered using the same command (i.e. `python Figure2.py`, `python FigureS1.py` and `python FigureS2.py`).
- Pre-generated and saved figures used in the paper can be found in [Figures/](./Figures).

## Acknowledging this work

If you publish any work based on the contents of this repository please cite ([CITATION file](CITATION)):

Whittaker, D. G., Capel, R. A., Hendrix, M., Chan, X. H. S., Herring, N., White, N. J., Mirams, G. R., Burton, R. A. B.
(2021).
[Cardiac TdP Risk Stratification Modelling of Anti-Infective Compounds including Chloroquine and Hydroxychloroquine](https://royalsocietypublishing.org/doi/10.1098/rsos.210235).
_Royal Society Open Science_, **8**: 210235.
