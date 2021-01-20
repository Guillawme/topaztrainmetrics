import pandas as pd
import matplotlib.pyplot as plt
import click

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('file', metavar='<file>')
@click.option('-l', '--loss', 'series', flag_value='loss', help='Plot loss.')
@click.option('-g', '--gepenalty', 'series', flag_value='ge_penalty', help='Plot GE penalty.')
@click.option('-p', '--precision', 'series', flag_value='precision', help='Plot precision.')
@click.option('-t', '--tpr', 'series', flag_value=['tpr', 'fpr'], help='Plot true/false positive rates.')
@click.option('-c', '--auprc', 'series', flag_value='auprc', default=True, help='Plot area under precision/recall curve (default).')
@click.option('-x', '--xaxis', 'xaxis', default='iter', type=click.Choice(['iter', 'epoch'], case_sensitive=False), help='X axis (iter or epoch; default: iter).')
@click.option('-o', '--output', 'output_file', default='', type=str, help='File name to save the plot (optional: with no file name, simply display plot on screen without saving it; recommended file formats: .png, .pdf, .svg or any format supported by matplotlib).')
def cli(file, series, xaxis, output_file):
    """Plot validation metrics from a Topaz training run.
    
    <file> is the results.txt file from standalone Topaz or the model_plot.star file from Topaz run within RELION."""
    data = pd.read_csv(file, delim_whitespace=True, index_col=xaxis, na_values='-')
    grouped = data.groupby('split')
    if series in ['loss', 'ge_penalty', 'precision', 'auprc']:
        fig, ax = plt.subplots(ncols=1, nrows=1)
        grouped[series].plot(legend=True, ax=ax)
        ax.set_xlabel(xaxis)
        ax.set_ylabel(series)
        ax.set_title(f'{series} as a function of {xaxis}')
    elif series == ['tpr', 'fpr']:
        fig, axs = plt.subplots(ncols=2, nrows=1, sharex=True, sharey=True, figsize=(10, 5))
        fig.suptitle(f'True and false positive rates as a function of {xaxis}')
        for key, ax in zip(grouped.groups.keys(), axs.flatten()):
            grouped.get_group(key)[series].plot(legend=True, ax=ax)
            ax.set_title(f'{key}')
            ax.set_xlabel(xaxis)
        axs[0].set_ylabel('True or false positive rate')
    fig.tight_layout()
    if output_file:
        fig.figsize = (11.80, 8.85)
        fig.dpi = 300
        plt.savefig(output_file)
    else:
        plt.show()