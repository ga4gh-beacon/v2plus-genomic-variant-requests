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
    This is a very specific script to generate markdown files from yaml files.
    Don't look at the code.
    """

    schemas_yaml_path = path.join( dir_path, pardir, "src", "requests")
    examples_yaml_path = path.join( schemas_yaml_path, "examples")
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

    request_pattern_ids = []

    for d_k, d_v in file_pars.items():
        o = {}
        ofp = path.join(schemas_yaml_path, f'{d_k}.yaml' )
        with open(ofp) as od:
            o = yaml.load(od, Loader=yaml.FullLoader)

        # prjsonnice(o)

        pp_f = path.join(generated_docs_path, f"{d_k}.md")

        ls = [f'# {d_v.get("headline")}']

        ls.append(f'\n{o.get("description", "")}\n')

        for chapter, title in d_v.get("chapters").items():
            pp = o.get(chapter, {})
            ls.append(f'## {title}\n')
            for pk, pi in pp.items():

                # very special
                if d_k == "requestPatterns":
                    request_pattern_ids.append(pk)

                ls.append(f'### `{pk}` \n')

                ls = __add_md_parameter_lines(ls, pi)

        pp_fh = open(pp_f, "w")
        pp_fh.write("\n".join(ls).replace("\n\n", "\n").replace("\n\n", "\n").replace("\n#", "\n\n#"))
        pp_fh.close()

################################################################################

def __add_md_parameter_lines(lines, parameter):

    for pik, piv in parameter.items():
        if type(piv) is dict:
            js = '  \n'
            lines.append(f'**{pik}:**  \n')
            lines.append(js.join([f'    - `{k}`: `{str(v).replace("{", "").replace("}", "")}`    ' for k, v in piv.items()]))                    
        elif type(piv) is list:
            js = '`\n* `'
            piv = f'\n* `{js.join([str(x) for x in piv])}`    '
            lines.append(f'**{pik}:** {piv}    ')
        elif "default" in pik or "pattern" in pik and len(str(piv)) > 0:
            lines.append(f'**{pik}:** `{piv}`    ')
        elif "description" in pik:
            lines.append(f'#### {pik}\n')
            piv = piv.replace("*", "    \n*")
            lines.append(f'{piv}    ')
        else:
            lines.append(f'**{pik}:** {piv}    ')
        lines.append(f'\n')

    return lines

################################################################################
################################################################################
################################################################################

if __name__ == '__main__':
    main()
