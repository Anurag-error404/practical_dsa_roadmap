import pytest

from graph import FlowGraph
from ford_fulkerson import max_flow
from min_cut import min_cut


def test_source_equals_sink_rejected():
    # TODO: Source equals sink — degenerate case, should be rejected as invalid input
    ...


def test_no_path_max_flow_zero():
    # TODO: No path exists from source to sink at all — max flow is 0
    ...


def test_cycles_handled_via_residual_graph():
    # TODO: A graph containing cycles — Ford-Fulkerson must handle this correctly via the
    #       residual graph, not loop forever
    ...


def test_zero_capacity_edges_ignored():
    # TODO: Zero-capacity edges — should behave as if the edge doesn't exist
    ...


def test_max_flow_equals_min_cut_capacity():
    # TODO: Verify max-flow value equals min-cut capacity (the max-flow min-cut theorem) as a
    #       built-in correctness check
    ...
