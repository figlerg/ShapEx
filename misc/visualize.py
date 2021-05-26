import datetime

import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm


def plotter(traces: list, param_intervals: dict = {}, density: int = 0, comparison_set=None, savename=None, timestep=1,
            case=0):
# TODO add things like axes, title, etc
    fig, axs = plt.subplots(nrows=1, ncols=1, constrained_layout=True, figsize=(16, 9))

    for trace in tqdm(traces, desc='Samples plotted', position=0):

        parts = splitter_helper(trace)
        if parts:  # this is for the _constraint tweak.. in case splitter_helper returns none, nothing happens for this trace
            for part in parts:
                axs.plot(part[0], part[1], 'b')
        # axs.scatter(traces[key][0][0], traces[key][1][0])
        # axs[1].plot(traces[(duration, slope, (x,y))][0],traces[(duration, slope, (x,y))][1])

        # plt.plot(traces[key][0],traces[key][1],zorder=0)
    if param_intervals and density:
        param_intervals_string_list = [param + ':' + str(param_intervals[param]) for param in param_intervals.keys()]
        param_intervals_string = ",".join(param_intervals_string_list)

        axs.set_xlabel(param_intervals_string + ', density = ' + str(density))

    if comparison_set:
        # axs.plot(np.linspace(0,100,100), np.zeros(100),'c')
        if case == 1:
            for trace in comparison_set:
                axs.plot(trace[:, 0], trace[:, 1], 'c')

        elif case == 0:
            for trace in comparison_set:
                x_vals = np.arange(len(trace))
                axs.plot(x_vals, trace, 'c')  # this is for xvals [0,1,...]

    axs.set_xlabel('time')
    axs.set_title('Pulse Specification')

    time = str(datetime.datetime.now())
    timestamp = time.replace(':', '_')  # ':' cannot be in file_path

    if savename:
        plt.savefig(savename)
    # plt.savefig(timestamp + '.jpg') # saves plot
    plt.show()

    return fig


def splitter_helper(trace):
    # this is just to get rid of unnecessary vertical lines between two letters
    # it takes the trace apart at repeating time values and returns a list of smaller traces

    # look for where the duplicates appear. this is where the two atomics are joined together
    # if trace[0] == 'discarded':
    #     return None
    between_letters = [0, ]
    for idx in range(trace[0].size):
        if idx == trace[0].size - 1:
            pass
        else:
            if trace[0][idx] == trace[0][idx + 1]:
                between_letters.append(idx + 1)

    trace_parts = []
    for idx in range(len(between_letters) - 1):
        start_idx = between_letters[idx]
        end_idx = between_letters[idx + 1]  # +1 because of python slicing (last index isnt in slice)
        trace_part = np.asarray((trace[0][start_idx:end_idx], trace[1][start_idx:end_idx]))
        trace_parts.append(trace_part)

    # handle last part separately:
    trace_parts.append(np.asarray((trace[0][between_letters[-1]:], trace[1][between_letters[-1]:])))

    return trace_parts