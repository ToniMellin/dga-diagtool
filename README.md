# DGA diagtool
A dash based dissolved gas analysis (dga) diagnostic tool. When given all DGA gas values, the tool calculates ratios and provides diagnostic method analysis results (Rogers ratio, Doernenburg, IEC ratios, Duval triangle 1).
**Use at your own caution.**

## Installation

Clone the repository

Install needed libraries to python 3.8+ with pip: 

```
pip install -r requirements.txt
```

## Usage

Run app_dga_diagtool.py with needed libraries installed and a browser should open up where you can input DGA sample gas values. Press **calculate** to determine ratios, diagnostic method results and comparison to typical values


## Features
- When given all DGA gas values, the tool calculates ratios and provides diagnostic method analysis results (Rogers ratio, Doernenburg, IEC ratios, Duval triangle 1)
- The tool will analyse gas values against standard typical values (IEC 60599 & IEEE C57.104) and indicate if they are exceeded 
- Duval triangle 1 sample plotting



## TODO
- Add IEEE C57.104-2008 conditions 3 & 4
- Add IEEE C57.104-2019 checkup
- Add duval triangle 4 analysis and plotting
- Add duval triangle 5 analysis and plotting

