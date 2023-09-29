# About

A RDF-based vocabulary for Manchester Syntax.

## Background

Manchester Syntax is a human-readable syntax used to represent and work with knowledge expressed in the Web Ontology Language (OWL). OWL is a semantic web language designed for expressing ontologies, which are formal representations of knowledge about a specific domain. These ontologies are used to enable computers to understand and reason about the semantics of information on the web.

Manchester Syntax provides a more user-friendly and compact way to write OWL expressions and axioms. It's particularly useful for ontology engineers and domain experts who want to create, publish and maintain OWL ontologies, as it makes the language more accessible.

Transforming OWL to Manchester Syntax currently involves either manually translating one to the other, or using transformation functions in tools and libraries like Protégé and [OWL API](https://github.com/owlcs/owlapi). These functions are usually written in traditional programming languages.

Unfortunately, there is currently no RDF-based vocabulary that can map OWL to Manchester Syntax automatically. Having a RDF-based vocabulary for Manchester Syntax would through its semantics add to the understandability, auditability and maintainability of the mapping. In addition, it offers the benefit to an ontology engineer or domain expert of actually working with RDF when modeling RDF, and not through some arbitrary programming language or black box software function. Last but not least, RDF is all about re-usability; having Manchester Syntax available as a set of data offering interoperability and semantics is in line with the goals of the Semantic Web and the knowledge graph technology underneath it. 

## Ontology of the Manchester Syntax

The ontology of the Manchester Syntax consists of shapes according to the SHACL-format. 

It has NodeShapes for the following class constructs:

1. A class definition (owl:Class);
2. A restriction class with the property owl:allValuesFrom
3. A restriction class with the property owl:someValuesFrom
4. A restriction class with the property owl:hasValue
5. A restriction class with the property owl:cardinality
6. A restriction class with the property owl:maxCardinality
7. A restriction class with the property owl:cardinality
8. A restriction class with the property owl:minCardinality
9. A subclass of some other class (rdfs:SubClassOf property)
10. An equivalent class of some other class (owl:equivalentClass)
11. A class that is the union of other classes (owl:unionOf)
12. A class that is the intersection of other classes (owl:intersectionOf)
13. A class that consists of the enumeration of individuals (owl:oneOf)

Still to be done:

14. Object properties
15. Datatype properties
16. ..?

### Example

For a good explanation of the vocabulary and the provided tooling in the repository, let's first revisit OWL constructs and the equivalents in Manchester Syntax, according to the standard, taken from [The Manchester OWL Syntax, Horridge et al, 2006](https://ceur-ws.org/Vol-216/submission_9.pdf).

| OWL Constructor     | DL Syntax       | Manchester OWL S. | Example                    |
|:-------------------:|:---------------:|:-----------------:|:--------------------------:|
| intersectionOf      | C u D           | C AND D           | Human AND Male             |
| unionOf             | C t D           | C OR D            | Man OR Woman               |
| complementOf        | ¬ C             | NOT C             | NOT Male                   |
| oneOf               | {a} t {b}...    | {a b ...}         | {England Italy Spain}      |
| someValuesFrom      | ∃ R C           | R SOME C          | hasColleague SOME Professor|
| allValuesFrom       | ∀ R C           | R ONLY C          | hasColleague ONLY Professor|
| minCardinality      | ≥ N R R         | MIN 3             | hasColleague MIN 3         |
| maxCardinality      | ≤ N R R         | MAX 3             | hasColleague MAX 3         |
| cardinality         | = N R R         | EXACTLY 3         | hasColleague EXACTLY 3     |
| hasValue            | ∃ R {a}         | R VALUE a         | hasColleague VALUE Matthe  |



[insert here RDF triples with manchestersyntax information]



# Tools and dependencies

This repository comes with a, fairly primitive, Python-based tool to transform OWL into Manchester Syntax.

1. manchestersyntax.py

## manchestersyntax.py

The tool manchestersyntax.py is used to read OWL ontologies and express them in Manchester Syntax.

### How to use manchestersyntax.py

A. Install all necessary libraries:

	1. pip install os
	1. pip install pyshacl
	2. pip install rdflib

B. Place one or more OWL-ontologies in the input folder in \manchestersyntax\Tools\Input. 

C. Run the script in the command prompt by typing: 

```
python manchestersyntax.py
```

D. Go to the output folder in \manchestersyntax\Tools\Output and grab your Turtle-file(s) (*.ttl). 
