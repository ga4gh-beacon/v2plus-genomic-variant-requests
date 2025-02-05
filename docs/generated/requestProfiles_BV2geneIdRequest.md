# Request Pattern: `BV2geneIdRequest`

A typical Beacon v2.n request for gene queries, e.g. for the retrieval of all variants in a gene or variants restricted by additional parameters such `variantType` or length of the affected sequence. TODO: Evaluate to split into more basic `GeneIdRequest` and specialized
      requests requiring an effect component.

## Query for a deletion involving TP53
### Solution `g_variant` with `geneId` (`BV2geneIdRequest`)
Query for a deletion involving TP53 by using the HUGO name to specify the gene. This request does not provide coordinates so on the server side matching has to be performed from annotated variants or by retrieving the gene's coordinates and creating internally a type of range request.
### Request 
**geneId:** `TP53`    
**variantType:** `DEL`    
