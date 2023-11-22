import rdflib
g = rdflib.Graph()
g.parse(location='ontology.ttl')
qres = g.query(query_object='PREFIX owl: <http://www.w3.org/2002/07/owl#>\nSELECT ?o WHERE {\n\t<https://example.org/example-ontology-stub> owl:versionInfo ?o .\n}\n')
print(qres[0].o)
