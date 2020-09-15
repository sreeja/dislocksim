import os

operations = ['[INSERT', '[UPDATE', '[DELETE', '[READ']

def generate_report(folder):
  for app in ['auction1']:
    for workload in ['workloadax']: #, 'workloaday', 'workloadaz', 'workloadbx', 'workloadby', 'workloadbz', 'workloadcx', 'workloadcy', 'workloadcz']:
      gran = 1
      for mode in range(1, 2):
        for placement in ['cent']: #, 'clust', 'dist']:
          number_of_ops = 0
          exec_time = 0
          for replica in ['paris', 'tokyo', 'singapore', 'capetown', 'newyork']:
            number_of_ops_rep = 0
            exec_time_rep = 0
            file_name = os.path.join(folder, app, workload, str(gran)+'-'+str(mode)+'-'+placement, replica+'.txt')
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
                    print(line)
                  elif parts[1] == 'AverageLatency(us)':
                    if parts[2] != 'NaN':
                      exec_time_rep += ops * float(parts[2])
                    print(line)
              print('replica ' + replica)
              print('operations ' + str(number_of_ops_rep))
              print('exec time ' + str(exec_time_rep))
            number_of_ops += number_of_ops_rep
            exec_time += exec_time_rep
          print('app ' + app)
          print('workload ' + workload)
          print('lock config ' + str(gran)+'-'+str(mode)+'-'+placement)
          print('operations ' + str(number_of_ops))
          print('exec time ' + str(exec_time))
          print('average latency(ms) ' + str(exec_time / number_of_ops / 1000.0))



folder = os.path.join('/', 'Users', 'snair', 'works', 'YCSB', 'wlogs')
# folder = os.path.join('/', 'Users', 'snair', 'works', 'cc-experiment', 'result', 'wlogs')
generate_report(folder)