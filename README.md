# topaztrainmetrics

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4451826.svg)](https://doi.org/10.5281/zenodo.4451826)

Plot metrics from a [Topaz](https://github.com/tbepler/topaz) training run.

## Installation

```
$ pip install topaztrainmetrics
```

## Usage

```
$  topaztrainmetrics --help
Usage: topaztrainmetrics [OPTIONS] <file>

  Plot validation metrics from a Topaz training run.

  <file> is the results.txt file from standalone Topaz or the
  model_plot.star file from Topaz run within RELION.

Options:
  -l, --loss                Plot loss.
  -g, --gepenalty           Plot GE penalty.
  -p, --precision           Plot precision.
  -t, --tpr                 Plot true/false positive rates.
  -c, --auprc               Plot area under precision/recall curve (default).
  -x, --xaxis [iter|epoch]  X axis (iter or epoch; default: iter).
  -o, --output TEXT         File name to save the plot (optional: with no file
                            name, simply display plot on screen without saving
                            it; recommended file formats: .png, .pdf, .svg or
                            any format supported by matplotlib).

  -h, --help                Show this message and exit.
```
