import plotly.express as px
import pandas
import numpy as np


def seq(float1, float2):
    start = float1
    stop = float2 + float1
    step = float1

    float_range_array = np.arange(start, stop, step)
    float_range_list = list(float_range_array)
    float_range_list = [round(x, 6) for x in float_range_list]
    float_result_list = [round(x**x, 6) for x in float_range_list]
    int_step_list = [x for x in range(1, len(float_result_list)+1)]
    return float_result_list, int_step_list


def main():
    sequenz, steps = seq(0.001, 0.99)
    print(sequenz, steps)
    graph = px.scatter(x=sequenz, y=steps)
    graph.show()


if __name__ == '__main__':
    main()
