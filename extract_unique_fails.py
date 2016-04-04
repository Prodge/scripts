"""
From the first '=====' to 'Ran xx tests in xx secs':
    Between each '====':
        Build the lines into 'this_output'
    Upon reaching each '====':
        Dump this_output into fails if its new
"""

import sys

output_file = sys.argv[1]

with open(output_file, "r") as f:
    fails = []
    run_times = []
    this_output = ''
    in_results = False
    for line in f:
        if line == '======================================================================\n':
            if in_results:
                if this_output not in fails:
                    fails.append(this_output)
                this_output = ''
            else:
                in_results = True
        if 'Ran ' in line and ' tests in ' in line:
            in_results = False
            run_times.append(line.split(' ')[-1][:-2])
        if in_results:
            this_output += line

average_run_time = sum(float(time) for time in run_times) / float(len(run_times))

#Print fails
errors = 0
failures = 0
for fail in fails:
    if 'ERROR: ' in fail:
        errors +=1
    else:
        failures +=1
    print fail


#Print stats
print "Unique Errors/Failures: ", len(fails)
print "Unique Errors: ", errors
print "Unique Failures: ", failures
print "Average Run Time: {}s or {}m".format(int(average_run_time), int(average_run_time / float(60)))

