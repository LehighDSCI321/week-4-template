import subprocess
import re
import pytest

@pytest.fixture
def graph():
    from student_code import VersatileDigraph
    return VersatileDigraph()

def test_successor_on_edge(graph):
    '''Test -doutegree'''
    graph.add_node("A", 10)
    graph.add_node("B",20)
    graph.add_node("C",30)
    graph.add_edge("A","B",edge_name='left')
    graph.add_edge("A","C",edge_name='right')
    soe=graph.successor_on_edge("A","right")
    assert soe == "C"

