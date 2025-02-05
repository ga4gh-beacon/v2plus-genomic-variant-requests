# Request Pattern: `BV2rangeRequest`

Beacon Range Queries are supposed to return matches of any variant with at least partial overlap of the sequence range specified by `referenceName`, `start` and end `parameters`. Additional qualifiers such as `variantType` or length of the affected sequence can be used to further restrict the returned results. For this request type `start` and `end` with a single position are used, _i.e._ a subset of the `start` and `end` specifications.

## Find variants overlapping an approximate sequence location
### Solution `g_variant` with range indicated by single `start` and `end` positions (`BV2rangeRequest`) and `variantType`
Here sequence variants at a specifiied region on chromosome 2 are matched by using single start and end positions to indicate the genomic *range*.
CAVE: Since no variant type is indicated such a query can potentially match a large number of variants, depending on the beacon's content and query interpretation (e.g. "any" overlap of a CNV could be matched unless the variant type is required for CNV queries).
### Request 
**assemblyId:** `GRCh38`    
**referenceName:** `17`    
**start:** 
* `345675`        
**end:** 
* `345681`        
