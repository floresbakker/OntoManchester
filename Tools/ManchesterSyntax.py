# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 18:40:53 2023

@author: Flores Bakker

The Manchester Syntax Vocabulary models the Manchester Syntax in RDF. Manchester Syntax is a human-readable and compact syntax used to represent knowledge in the Web Ontology Language (OWL), which is a semantic web language based on RDF and used for defining and sharing ontologies. Manchester Syntax is designed to be human-readable and concise, making it easier for users to create and understand OWL ontologies. It provides an alternative to the more verbose syntax of OWL itself.

With the script ManchesterSyntax.py one can transform OWL into Manchester Syntax.

Usage: 

1. Place an arbitrary ontology (as turtle file) in the input folder.
2. In the command prompt, run 'python manchestersyntax.py'
3. Go to the output folder and grab your enriched turtle file, now including Manchester Syntax labels and definitions.


"""
import os
import pyshacl
import rdflib 
from rdflib import Namespace

# Set the path to the desired standard directory. 
directory_path = "C:/Users/Administrator/Documents/Branches/"

# namespace declaration
manchester = Namespace("https://data.rijksfinancien.nl/manchester/model/def/")

# Function to read a graph (as a string) from a file 
def readGraphFromFile(file_path):
    # Open each file in read mode
    with open(file_path, 'r', encoding='utf-8') as file:
            # Read the content of the file and append it to the existing string
            file_content = file.read()
    return file_content

# Function to write a graph to a file
def writeGraph(graph):
    graph.serialize(destination="C:/Users/Administrator/Documents/Branches/manchestersyntax/Tools/Output/"+filename_stem+"-manchestersyntax.ttl", format="turtle")

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
             

# loop through any turtle files in the input directory
for filename in os.listdir(directory_path+"manchestersyntax/Tools/Input"):
    if filename.endswith(".ttl"):
        file_path = os.path.join(directory_path+"manchestersyntax/Tools/Input", filename)
        
        # Establish the stem of the file name for reuse in newly created files
        filename_stem = os.path.splitext(filename)[0]
        

# Get the manchester syntax vocabulary and place it in a string
manchester_generator = readGraphFromFile("C:/Users/Administrator/Documents/Branches/manchestersyntax/Specification/manchestersyntax.ttl")

# Get some ontology to be transformed from OWL to Manchester Syntax. The ontology needs to be placed in the input directory.
ontology_graph = readGraphFromFile(file_path)   


# Join the manchester syntax and the ontology to be transformed into one big string.
serializable_graph_string = ontology_graph

# Create a graph of the string consisting of the manchester syntax and the ontology to be transformed 
serializable_graph = rdflib.Graph().parse(data=serializable_graph_string , format="ttl")
serializable_graph.bind("manchester", manchester)

# Inform user
print ('Creating Manchester Syntax labels and definitions...')

# Call the shacl engine with the HTML vocabulary and the document to be serialized
iteratePyShacl(manchester_generator, serializable_graph)

# Inform user
print ('Done.')
