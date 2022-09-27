import itertools
import networkx as nx
from networkx.readwrite import json_graph
import matplotlib
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Graph

import collatz


if __name__=="__main__":
  num_max=1000
  G = nx.DiGraph()
  elist = collatz.collatz_dict_le(num_max).items()
  print(elist)
  G.add_edges_from(elist)

  nx.nx_agraph.write_dot(G,"docs/collatz.dot")
  # pos = nx.nx_agraph.graphviz_layout(G)
  # pos = nx.nx_agraph.graphviz_layout(G, prog="dot")

  # G=nx.spring_layout(G)
  # nx.draw(G)

  # nx.write_graphml(G, "docs/collatz.graph.xml")
  # plt.savefig("docs/collatz.png")

  # g_data = json_graph.node_link_data(G)
  # for n in g_data["nodes"]:
  #   n["symbolSize"] = 40
  #   n["name"]=n["id"]
  #   if n["id"]==1:
  #     n["fixed"]=True
  
  # print(g_data)
  # c = (
  #   # Graph(init_opts=opts.InitOpts(width="100%",height="100%"))
  #   Graph()
  #   .add("", g_data['nodes'], g_data['links'], repulsion=8000,)
  #   .set_global_opts(title_opts=opts.TitleOpts(title=f"collatz first {num_max}"))
  #   .render("docs/graph_base.html")
  # )

