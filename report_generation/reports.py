import os

operations = ['[INSERT', '[UPDATE', '[DELETE', '[READ']

def generate_report(folder):
  result_string = []
  error_string = []
  for app in ['auction2']:
    result_string += ['********************** app ' + app + '***************************']
    # for workload in ['workloadax', 'workloadbx', 'workloadcx']:
    for workload in ['workloadax', 'workloaday', 'workloadaz', 'workloadbx', 'workloadby', 'workloadbz', 'workloadcx', 'workloadcy', 'workloadcz']:
      result_string += ['--------------------- workload ' + workload]
      gran = 1
      for mode in range(1, 8):
        # for placement in ['cent']: #, 'clust', 'dist']:
        for placement in ['cent', 'clust', 'dist']:
          number_of_ops = 0
          exec_time = 0
          lock_config = str(gran)+'-'+str(mode)+'-'+placement
          for replica in ['paris', 'tokyo', 'singapore', 'capetown', 'newyork']:
            number_of_ops_rep = 0
            exec_time_rep = 0
            file_name = os.path.join(folder, 'wlogs', app, workload, lock_config, replica+'.txt')
            with open(file_name) as f:
              for line in f.readlines():
                # print(line)
                if line.startswith(tuple(operations)):
                  parts = [x.strip() for x in line.split(',')]
                  if 'FAILED' in parts[0]:
                    # handle it
                    pass
                  if parts[1] == 'Operations':
                    ops = int(parts[2])
                    number_of_ops_rep += ops 
                    # print(line)
                  elif parts[1] == 'AverageLatency(us)':
                    if parts[2] != 'NaN':
                      exec_time_rep += ops * float(parts[2])
                    # print(line)
              # print('replica ' + replica)
              # print('operations ' + str(number_of_ops_rep))
              # print('exec time ' + str(exec_time_rep))
            number_of_ops += number_of_ops_rep
            exec_time += exec_time_rep
          if number_of_ops < 4990:
            error_string += [workload + ' ------- ' + lock_config + ' operations ' + str(number_of_ops)]
          if number_of_ops > 0:
            latency = exec_time / number_of_ops / 1000.0
          else:
            latency = 0
          result_string += ['lock config ' + lock_config + '------' + 'operations ' + str(number_of_ops) + '------' + 'exec time ' + str(exec_time) + '------' + 'average latency(ms) ' + str(latency)]
  result_file = os.path.join(folder, 'report.txt')
  with open(result_file, 'w') as rf:
    for r in result_string:
      rf.write(r + '\n') 
  error_file = os.path.join(folder, 'error.txt')
  with open(error_file, 'w') as ef:
    for e in error_string:
      ef.write(e + '\n') 



# folder = os.path.join('/', 'Users', 'snair', 'works', 'YCSB', 'wlogs')
folder = os.path.join('/', 'Users', 'snair', 'works', 'cc-experiment', 'results', 'small22')
generate_report(folder)