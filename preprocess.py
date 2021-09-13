import networkx as nx
from string import punctuation

def coauthorshipNetwork(df,mincoauthor=10):
    G = nx.Graph()
    id_name = {}

    for index,row in df.iterrows():
        authors = [author.lower() for author in row['Authors'].split(',') if author != '']
        ids = [id for id in row['Author(s) ID'].split(';') if id != '']
        
        for i in range(len(ids)):
            if (ids[i] not in id_name):
                id_name[ids[i]] = authors[i]

        coauthors = nx.complete_graph(len(ids))
        id_mapping = {i:id for i,id in enumerate(ids)}
        coauthors = nx.relabel_nodes(coauthors,id_mapping)
        
        G.add_edges_from(coauthors.edges())
    
    node_size = []
    node_text = []
    to_remove = []
    for node in G.nodes:
        if G.degree(node) < mincoauthor:
            to_remove.append(node)
        else:
            node_size.append(G.degree(node))
            node_text.append(id_name[node] + ' (' + str(G.degree(node)) + ' coautores)')
    
    G.remove_nodes_from(to_remove)

    #to_remove = [node for node,degree in dict(G.degree()).items() if degree <= mincoauthor]
    #G.remove_nodes_from(to_remove)
    pos = nx.spring_layout(G,k=0.1)
    
    edge_x = []
    edge_y = []
    for edge in G.edges:
        x0,y0 = pos[edge[0]]
        x1,y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    node_x = []
    node_y = []
    for node in G.nodes:
        node_x.append(pos[node][0])
        node_y.append(pos[node][1])

    return node_x, node_y, edge_x, edge_y, node_size, node_text

def keywordsNetwork(df,mincokeywords=10):
    G = nx.Graph()
    data = {}
    for index,row in df[df["Author Keywords"].notna()].iterrows():
        curr_keywords = []
        for keyword in row["Author Keywords"].split(";"):
            temp = keyword.lower()
            for punc in punctuation:
                temp = temp.replace(punc, " ").replace("  "," ")
            curr_keywords.append(temp.strip())
            
        cokeywords = nx.complete_graph(len(curr_keywords))
        id_mapping = {i:id for i,id in enumerate(curr_keywords)}
        cokeywords = nx.relabel_nodes(cokeywords,id_mapping)
        
        G.add_edges_from(cokeywords.edges())
    
    node_size = []
    node_text = []
    to_remove = []
    for node in G.nodes:
        if G.degree(node) < mincokeywords:
            to_remove.append(node)
        else:
            node_size.append(G.degree(node))
            node_text.append(node + ' (' + str(G.degree(node)) + ' co-keywords)')
    
    G.remove_nodes_from(to_remove)

    pos = nx.spring_layout(G)
    
    edge_x = []
    edge_y = []
    for edge in G.edges:
        x0,y0 = pos[edge[0]]
        x1,y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    node_x = []
    node_y = []
    for node in G.nodes:
        node_x.append(pos[node][0])
        node_y.append(pos[node][1])
    
    return node_x, node_y, edge_x, edge_y, node_size, node_text