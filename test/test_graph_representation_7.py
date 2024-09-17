import subprocess
import re
import pytest

@pytest.fixture
def graph():
    from student_code import VersatileDigraph
    return VersatileDigraph()

def test_out_degree(graph):
    '''Test -doutegree'''
    graph.add_node("A", 10)
    graph.add_node("B",20)
    graph.add_node("C",30)
    graph.add_edge("A","B")
    graph.add_edge("C","B")
    indeg=graph.out_degree("A")
    assert indeg == 1

