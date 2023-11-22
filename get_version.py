import rdflib
g = rdflib.Graph()
g.parse(location='main/ontology.ttl')
qres = g.query(query_object='PREFIX owl: <http://www.w3.org/2002/07/owl#>\nSELECT ?o WHERE {\n\t<https://example.org/example-ontology-stub> owl:versionInfo ?o .\n}\n')
for row in qres:
    print(row.o)
    break
