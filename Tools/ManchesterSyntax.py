# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 18:40:53 2023

@author: Flores Bakker


"""
import pyshacl
import rdflib 


# Function to read a graph (as a string) from a file 
def readGraphFromFile(file_path):
    # Open each file in read mode
    with open(file_path, 'r', encoding='utf-8') as file:
            # Read the content of the file and append it to the existing string
            file_content = file.read()
    return file_content

# Function to write a graph to a file
def writeGraph(graph):
    graph.serialize(destination="C:/Users/Administrator/Documents/Branches/ManchesterSyntax/manchesterDocument.ttl", format="turtle")

# Function to call the PyShacl engine so that a RDF model of an HTML document can be serialized to HTML-code.
def iteratePyShacl(manchester_generator, serializable_graph):
        
        # call PyShacl engine and apply the HTML vocabulary to the serializable HTML document
        pyshacl.validate(
        data_graph=serializable_graph,
        shacl_graph=manchester_generator,
        data_graph_format="turtle",
        shacl_graph_format="turtle",
        advanced=True,
        inplace=True,
        inference=None,
        iterate_rules=True, 
        debug=False,
        )
       
        writeGraph(serializable_graph)
             

# Get the HTML vocabulary and place it in a string
manchester_generator = readGraphFromFile("C:/Users/Administrator/Documents/Branches/ManchesterSyntax/manchestersyntax.ttl")

# Get the RDF-model of some HTML document and place it in a string. Here you can input your own RDF-model of some HTML-document.
ontology_graph = readGraphFromFile("C:/Users/Administrator/Documents/Branches/HTML voc/HTML vocabulary.ttl")   

# Join the HTML vocabulary and the RDF-model of some HTML document into a string
serializable_graph_string = ontology_graph

# Create a graph of the string containing the HTML vocabulary and the RDF-model of some HTML document
serializable_graph = rdflib.Graph().parse(data=serializable_graph_string , format="ttl")

# Inform user
print ('Instantiating manchester document...')

# Call the shacl engine with the HTML vocabulary and the document to be serialized
iteratePyShacl(manchester_generator, serializable_graph)



print ('manchester document instantiated.')
