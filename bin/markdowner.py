#!/usr/local/bin/python3

import inspect, sys, re, yaml
from os import getlogin, makedirs, pardir, path, system
from pathlib import Path
from json_ref_dict import RefDict, materialize

dir_path = path.dirname( path.abspath(__file__) )

from bycon import * #BYC, read_schema_file
import byconServices

################################################################################

def main():
    """
    """

    input_yaml_path = path.join( dir_path, pardir, "src", "requests")
    generated_docs_path = path.join( dir_path, pardir, "docs", "generated")

    #>------------------------------------------------------------------------<#

    """
    """

    file_pars = {
        "requestParameterComponents":{
            "headline": "Request Parameter Definitions",
            "chapters": {
                "$defs": "Argument Definitions"
            },
        },
        "requestPatterns": {
            "headline": "Request Patterns Definitions",
            "chapters": {
                "$defs": "Request Patterns"
            }
        }
    }


    for d_k, d_v in file_pars.items():
        o = {}
        ofp = path.join(input_yaml_path, f'{d_k}.yaml' )
        with open(ofp) as od:
            o = yaml.load(od, Loader=yaml.FullLoader)

        # prjsonnice(o)

        pp_f = path.join(generated_docs_path, f"{d_k}.md")

        ls = [f'# {d_v.get("headline")}']

        for chapter, title in d_v.get("chapters").items():
            pp = o.get(chapter, {})
            ls.append(f'## {title}')
            for pk, pi in pp.items():
                ls.append(f'### `{pk}` \n')

                for pik, piv in pi.items():
                    if type(piv) is dict:
                        js = '  \n'
                        ls.append(f'**{pik}:**  \n')
                        ls.append(js.join([f'    - `{k}`: `{v}`    ' for k, v in piv.items()]))                    
                    elif type(piv) is list:
                            js = '`\n* `'
                            piv = f'\n* `{js.join([str(x) for x in piv])}`    '
                            ls.append(f'**{pik}:** {piv}    ')
                    elif "default" in pik or "pattern" in pik and len(str(piv)) > 0:
                        ls.append(f'**{pik}:** `{piv}`    ')
                    elif "description" in pik:
                        ls.append(f'**{pik}:**\n')
                        piv = piv.replace("*", "    \n*")
                        ls.append(f'{piv}    ')
                    else:
                        ls.append(f'**{pik}:** {piv}    ')
                    ls.append(f'\n')
                ls.append(f'\n')

        pp_fh = open(pp_f, "w")
        pp_fh.write("\n".join(ls).replace("\n\n", "\n").replace("\n\n", "\n"))
        pp_fh.close()

################################################################################
################################################################################
################################################################################

if __name__ == '__main__':
    main()
