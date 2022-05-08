# DGA diagtool

A dash based transformer oil dissolved gas analysis (DGA) diagnostic tool. When given DGA gas values, the tool calculates ratios, compares values against typical values and provides diagnostic method analysis results (Rogers ratio, Doernenburg, IEC ratios, Duval triangle 1).

**Use at your own caution.** **The author assumes no liability for the usage of the tool.** **Always consult a transformer expert when diagnosing a possible fault in a transformer.**

## Disclaimer

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**

## Installation

Clone the repository

Install needed libraries to python 3.8+ with pip: 

```
pip install -r requirements.txt
```

## Usage

Run app_dga_diagtool.py using python with needed libraries installed and a browser should open up where you can input DGA sample gas values. Press **calculate** to determine ratios, diagnostic method results and comparison to typical values.

## Features

- The tool calculates ratios and provides diagnostic method analysis results with given values (Rogers ratio, Doernenburg, IEC ratios, Duval triangle 1, Duval traingle 4 and Duval triangle 5)
- If values are omitted, ratios or diagnostic method results that need the omitted values will not produce results, but any ratios or methods that have sufficient data to calculate will be provided
- The tool will compare gas values against standard typical values (IEC 60599 & IEEE C57.104) and indicate if they are exceeded 
- Duval triangle 1 sample plotting, with additional Duval triangles 4 and 5 samples plotted if applicable

## TODO (Future feature ides)
- Add IEEE C57.104-2008 typical value conditions 3 & 4
- Cigre typical values comparison
- Multiple sample points
- Online monitor data
- Rate of change comparisons (IEC / IEEE / Cigre)
- Analysis from trends
