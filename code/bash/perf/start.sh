perf record -a -g -- sleep 60
perf script > out.perf
./stackcollapse-perf.pl out.perf > out.folded
./flamegraph.pl out.folded > kernel.svg
