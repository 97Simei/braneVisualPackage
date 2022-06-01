from os import path
from visualFunctionDetail import PlotFunction

input_path = "./data/test.csv"
output_path='./data/'

def test_plot_missing_value_function():
    plot_worker = PlotFunction(
        input_path=input_path,
        title="test_sample",
        function_type='missing_value',
        target_columns='',
        output_path=output_path
    )
    plot_worker.plot_missing_value()
    assert path.exists(output_path + "_missing_value.html") is True
def test_plot_distribution_function():
    plot_worker = PlotFunction(
        input_path=input_path,
        title="test_sample",
        function_type='missing_value',
        target_columns='',
        output_path=output_path
    )
    plot_worker.plot_distribution()
    assert path.exists(output_path + "distribution.png") is True
def test_plot_correlation_function():
    plot_worker = PlotFunction(
        input_path=input_path,
        title="test_sample",
        function_type='missing_value',
        target_columns='',
        output_path=output_path
    )
    plot_worker.plot_correlation()
    assert path.exists(output_path + "heatmap.png") is True



