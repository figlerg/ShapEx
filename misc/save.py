import csv
import os

from tqdm import tqdm


# creates 'positive' and 'negative' directories and saves traces inside
def save_to_csv(traces, positive, dir_string):
    directory_label = {True: 'Positive', False: 'Negative'}
    new_dir_string = dir_string + os.sep + directory_label[positive]
    os.makedirs(new_dir_string, exist_ok=True)

    counter = 1
    # for numbering the examples

    for trace in tqdm(traces, desc='saving traces and settings to csv files'):
        label = 'trace_' + str(counter)

        # write data to csv file

        with open(new_dir_string + os.sep + label + '.csv',
                  'w') as csv_file:
            file_writer = csv.writer(csv_file, delimiter=',',
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(['time', label])

            for i in range(len(trace[0])):
                pair = (trace[0][i], trace[1][i])
                file_writer.writerow(pair)

        # write parameters to csv file so one can check which params were used
        with open(new_dir_string + os.sep + label + '_settings.csv',
                  'w') as settings_csv_file:
            file_writer = csv.writer(settings_csv_file, delimiter=',',
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)

            n_params = len(trace[3])
            file_writer.writerow([trace[3][i][0] for i in range(n_params)])
            file_writer.writerow([trace[3][i][1] for i in range(n_params)])

            pass

        counter += 1
