# Request Pattern: `g_variant`

This represents the generic collection of variant parameters allowed in Beacon v2 requests.

### Query for a deletion involving TP53
#### Solution
Query for a deletion involving TP53 using the maximum extent of the gene's coding region (known from somewhere...). The deletion to be found are expected to have an overlap with the queried range; however, the extent of the overlap is not pre-defined (most endpoints woul respond to a **recommended** "any" overlap but this is not a strict requirement imposed by the schema). Here positions refer to chromosome 17 on GRCh38 as indicated by the referenceName RefSeq ID.
### `request` 
**referenceName:** refseq:NC_0000017.11    
**start:** 
* `7669608`        
**end:** 
* `7676593`        
**variantType:** DEL    


### Query for a deletion involving TP53
#### Solution
Query for a deletion involving TP53 by using the HUGO name to specify the gene. This request does not provide coordinates so on the server side matching has to be performed from annotated variants or by retrieving the gene's coordinates and creating internally a type of range request.
### `request` 
**geneId:** TP53    
**variantType:** DEL    


### Find events in TP53 or in close proximity (±~5000bp)
#### Solution
For this query the mapping position of TP53 (17:7669607-7676593) has to be known. Usually this knowledge would be provided by a front end helper and the aditional padding added manually or w/ a helper field (if frequent scenario) and the beacon itself would just receive the positional range request.
The "insertion" type is here provided through the Sequence Ontology term `SO:0000667` and for the chromosome the full, prefixed RefSeq term is being used.
### `request` 
**referenceName:** refseq:NC_0000017.11    
**start:** 
* `7664000`        
**end:** 
* `7682000`        
**variantType:** SO:0000667    
