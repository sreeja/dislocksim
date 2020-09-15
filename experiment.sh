make dockdown-cent
make dockdown-clust
make dockdown-dist

export APP=auction1
export GRANULARITY=1
export LOCKTYPE=1

make dockrun-cent
# make dockrun-clust
# make dockrun-dist


# auction1
# granularity 1, type - 1-9
# granularity 2, type - 1-3
# 12 configurations

# auction2
# granularity 1, type - 1-27
# granularity 2, type - 1-9
# 36 configurations

# auction3
# granularity 1, type - 81
# granularity 2, type - 54
# granularity 3, type - 27
# granularity 4, type - 18
# granularity 5, type - 27
# granularity 6, type - 18
# granularity 7, type - 24
# granularity 8, type - 16
# 265 configurations

# 313 configurations in total