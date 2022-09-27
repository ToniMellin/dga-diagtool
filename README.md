# DGA diagtool

A dash based transformer oil dissolved gas analysis (DGA) diagnostic tool. When given DGA gas values, the tool calculates ratios, compares values against typical values and provides diagnostic method analysis results (Rogers ratio, Doernenburg, IEC ratios, Duval triangles).

**Use at your own caution.** **The author assumes no liability for the usage of the tool.** **Always consult a transformer expert when diagnosing a possible fault in a transformer.**

## Disclaimer

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**

## Installation

Clone the repository

Install needed libraries to python 3.8+ with pip:

```text
pip install -r requirements.txt
```

## Usage

Run app_dga_diagtool.py using python with needed libraries installed and a browser should open up where you can input DGA sample gas values. Press **calculate** to determine ratios, diagnostic method results and comparison to typical values.

## Features

### Single sample diagnostic

- The tool calculates ratios and provides diagnostic method analysis results with given values (Rogers ratio, Doernenburg, IEC ratios, Duval triangle 1, Duval triangle 4 and Duval triangle 5)
- If values are omitted, ratios or diagnostic method results that need the omitted values will not produce results, but any ratios or methods that have sufficient data to calculate will be provided
- The tool will compare gas values against standard typical values (IEC 60599, IEEE C57.104 & Cigre TB 771) and indicate if they are exceeded
- Duval triangle 1 sample plotting, with additional Duval triangles 4 and 5 samples plotted if applicable

### Multiple sample diagnostic

- Sample data graphing in an interactive plotly graph
- The tool calculates ratios and provides diagnostic method analysis results with given values (Rogers ratio, Doernenburg, IEC ratios, Duval triangle 1, Duval triangle 4 and Duval triangle 5)
- If values are omitted, ratios or diagnostic method results that need the omitted values will not produce results, but any ratios or methods that have sufficient data to calculate will be provided
- Typical values comparison with a summary table
- Duval triangle 1 multi sample plotting, with additional Duval triangles 4 and 5 samples plotted if applicable

## TODO (Future feature ides)

- Add IEC 60599 95% typical values
- Cigre typical values comparison that includes n2/o2 ratio typicals
- internal logging (with on/off) +logging download
- Online monitor data
- Rate of change comparisons (IEC / IEEE / Cigre) for multiple samples
- Analysis from trends
- uncertainty analysis of samples
- duval triangle uncertainty limits
- Duval pentagons
- Ester options
