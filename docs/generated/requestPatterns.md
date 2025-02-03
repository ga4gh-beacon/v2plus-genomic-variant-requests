# Request Patterns Definitions
## Request Patterns
### `g_variant` 
**description:**
This represents the generic collection of variant parameters allowed in Beacon v2 requests.    
**type:** object    
**properties:**  
    - `assemblyId`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/Assembly'}`      
    - `referenceName`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/RefSeqId'}`      
    - `referenceBases`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/ReferenceBases'}`      
    - `alternateBases`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/AlternateBases'}`      
    - `variantType`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/VariantType'}`      
    - `start`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/Start'}`      
    - `end`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/End'}`      
    - `geneId`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/GeneId'}`      
    - `aminoacidChange`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/AminoacidChange'}`      
    - `genomicAlleleShortForm`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/GenomicAlleleShortForm'}`      
    - `variantMinLength`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/VariantMinLength'}`      
    - `variantMaxLength`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/VariantMaxLength'}`    
**examples:**  
    - `$ref`: `../examples/g_variant.yaml#/examples`    

### `GenomicVariationQuery` 
**description:**
This represents the generic collection of variant parameters supported in Beacon v2+ requests.     
**type:** object    
**properties:**  
    - `requestType`: `{'const': 'GenomicVariationQuery'}`      
    - `referenceAccession`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/RefgetAccession'}`      
    - `start`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/SequenceStart'}`      
    - `end`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/SequenceEnd'}`      
    - `sequence`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/Sequence'}`      
    - `copyChange`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/CopyChange'}`      
    - `adjacencyAccession`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/AdjacencyAccession'}`      
    - `adjacencyStart`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/AdjacencyStart'}`      
    - `adjacencyEnd`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/AdjacencyEnd'}`      
    - `geneId`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/GeneId'}`      
    - `aminoacidChange`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/AminoacidChange'}`      
    - `genomicAlleleShortForm`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/GenomicAlleleShortForm'}`      
    - `variantMinLength`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/VariantMinLength'}`      
    - `variantMaxLength`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/VariantMaxLength'}`    

### `BV2alleleRequest` 
**type:** object    
**properties:**  
    - `requestType`: `{'description': 'Note: The `requestType` parameter had not been defined for Beacon v2.0 and therefore in _senso stricto_ is not part of requests only relying on v2 parameters.', 'const': 'BV2alleleRequest'}`      
    - `assemblyId`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/Assembly'}`      
    - `referenceName`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/RefSeqId'}`      
    - `start`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/Start'}`      
    - `referenceBases`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/ReferenceBases'}`      
    - `alternateBases`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/AlternateBases'}`    
**required:** 
* `referenceName`
* `start`
* `alternateBases`        

### `BV2bracketRequest` 
**description:**
A typical Beacon v2 request for matching variations where start and end fall in a genomic range. Here, the approximate or varying positions for variation start and end are queried through brackets, _i.e._ by using 2 values for `start` and `end` each. This is a typical scenario in querying for CNVs where the `variantType` parameter indicates the relative change in genomic copy number through either VCF derived string parameters or, preferably, EFO terms (pls. refer to the class definition.)    
**type:** object    
**properties:**  
    - `requestType`: `{'const': 'BV2bracketRequest'}`      
    - `assemblyId`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/Assembly'}`      
    - `referenceName`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/RefSeqId'}`      
    - `start`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/Start'}`      
    - `end`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/End'}`      
    - `variantType`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/VariantType'}`      
    - `variantMinLength`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/VariantMinLength'}`      
    - `variantMaxLength`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/VariantMaxLength'}`    
**required:** 
* `referenceName`
* `start`
* `end`
* `variantType`        

### `VariantIdRequest` 
**type:** object    
**properties:**  
    - `requestType`: `{'const': 'VariantIdRequest'}`      
    - `variantId`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/VariantId'}`    

### `AminoacidChangeRequest` 
**type:** object    
**properties:**  
    - `requestType`: `{'const': 'AminoacidChangeRequest'}`      
    - `aminoacidChange`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/AminoacidChange'}`      
    - `geneId`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/GeneId'}`    
**required:** 
* `aminoacidChange`        

### `GenomicAlleleShortFormRequest` 
**type:** object    
**properties:**  
    - `genomicAlleleShortForm`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/GenomicAlleleShortForm'}`    

### `VQSsequenceRequest` 
**type:** object    
**properties:**  
    - `requestType`: `{'const': 'VQSsequenceRequest'}`      
    - `referenceAccession`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/RefgetAccession'}`      
    - `start`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/SequenceStart'}`      
    - `end`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/SequenceEnd'}`      
    - `sequence`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/Sequence'}`    
**required:** 
* `referenceAccession`
* `start`
* `sequence`        

### `VQScopyChangeRequest` 
**description:**
A typical Beacon v2.n request for copy number variations (CNVs) queries approximate positions for CNV start and end regions through use of the `Range` type. The `copyChange` parameter indicates the relative change in genomic copy number (pls. refer to the class definition.)    
**type:** object    
**properties:**  
    - `requestType`: `{'const': 'VQScopyChangeRequest'}`      
    - `referenceAccession`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/RefgetAccession'}`      
    - `start`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/SequenceStart'}`      
    - `end`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/SequenceEnd'}`      
    - `copyChange`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/CopyChange'}`      
    - `variantMinLength`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/VariantMinLength'}`      
    - `variantMaxLength`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/VariantMaxLength'}`    
**required:** 
* `referenceAccession`
* `start`
* `end`
* `copyChange`        

### `VQSadjacencyRequest` 
**description:**
A typical Beacon v2.n request for sequence adjacency queries, e.g. for the retrieval of chromosomal translocation events or sequence fusions. TODO: In VRS v2 there is an implicit sequence directionality from the use of either start or end parameters for either side of the adjacency. This might be problematic on the query side where in many instances just the approximate position of the (fused) breakpoints maight be of interest. This needs additional clarification (e.g. use of integer `start` and `end`, `adjacencyStart` and  `adjecencyEnd` parameters to indicate direction independent matching).    
**type:** object    
**properties:**  
    - `requestType`: `{'const': 'VQSadjacencyRequest'}`      
    - `referenceAccession`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/RefgetAccession'}`      
    - `start`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/SequenceStart'}`      
    - `end`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/SequenceEnd'}`      
    - `adjacencyAccession`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/AdjacencyAccession'}`      
    - `adjacencyStart`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/AdjacencyStart'}`      
    - `adjacencyEnd`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/AdjacencyEnd'}`    

### `VQSgeneIdRequest` 
**description:**
A typical Beacon v2.n request for gene queries, e.g. for the retrieval of all variants in a gene or variants restricted by additional parameters such as CNV type (`copyChange`) or length of the affected sequence. TODO: Evaluate to split into more basic `GeneIdRequest` and specialized
      requests requiring an effect component.    
**type:** object    
**properties:**  
    - `requestType`: `{'const': 'VQSgeneIdRequest'}`      
    - `geneId`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/GeneId'}`      
    - `copyChange`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/CopyChange'}`      
    - `variantMinLength`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/VariantMinLength'}`      
    - `variantMaxLength`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/VariantMaxLength'}`      
    - `molecularEffect`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/molecularEffect'}`      
    - `clinicalRelevance`: `{'$ref': './common/requestParameterComponents.yaml#/$defs/clinicalRelevance'}`    
**required:** 
* `geneId`        

### `BV2multivarsRequest` 
**description:**
This multi variant query is a collection of individual variant queries based on the Beacon v2 parameters (`g_variant`). Status: Proposed for evaluation for Beacon v2.n or v3.0 (but potentially
        skipped in favor of the `VQSmultivarRequest` queries).    
**type:** object    
**properties:**  
    - `requestType`: `{'const': 'BV2multivarsRequest'}`      
    - `variantLogic`: `{'description': 'The logic to apply to the set of variants in the query. The default is to apply the AND logic, meaning that all **samples** (i.e. biosamples, individuals or analyses) must fulfil the query criteria: * with a (default) AND logic and "biosamples" as requested entity \n  `biosample_id` values from the individual variant query responses\n  will be intersected\n* with an OR logic and "analyses" as requested entity `analysis_id`\n  values from the individual variant query responses will be concatenated\nNote: The `variantLogic` parameter is not defined in the current\n      `requestParameterComponents.yaml` file yet due to the very experimental\n      and tentative nature of this proposal.', 'type': 'string', 'enum': ['AND', 'OR'], 'default': 'AND'}`      
    - `queries`: `{'type': 'array', 'items': {'$ref': '#/$defs/g_variant'}}`    

### `VQSmultivarRequest` 
**description:**
This multi variant query is a collection of individual variant queries based on the Beacon v2+ "VQS" query patterns. Status: Proposed for evaluation for Beacon v2.n or v3.0    
**type:** object    
**properties:**  
    - `requestType`: `{'const': 'VQSmultivarRequest'}`      
    - `variantLogic`: `{'type': 'string', 'enum': ['AND', 'OR'], 'default': 'AND'}`      
    - `queries`: `{'type': 'array', 'items': {'anyOf': [{'$ref': '#/$defs/VQSsequenceRequest'}, {'$ref': '#/$defs/VQScopyChangeRequest'}, {'$ref': '#/$defs/VQSadjacencyRequest'}, {'$ref': '#/$defs/GeneIdRequest'}, {'$ref': '#/$defs/VariantIdRequest'}, {'$ref': '#/$defs/AminoacidChangeRequest'}, {'$ref': '#/$defs/GenomicAlleleShortFormRequest'}]}}`    
