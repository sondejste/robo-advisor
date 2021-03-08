# Robo Advisor
An automated stock price retriever.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/sondejste/robo-advisor) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd robo-advisor
```

Use Anaconda to create and activate a new virtual environment, perhaps called "stocks-env":

```sh
conda create -n stocks-env python=3.8
conda activate stocks-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Setup

Obtain your API Key from [Alpha Vantage](https://www.alphavantage.co/) and follow input directions below.

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your API Key:

    ALPHAVANTAGE_API_KEY="YOUR_API"

## Usage

Run the game script:

```py
python app/robo_advisor.py