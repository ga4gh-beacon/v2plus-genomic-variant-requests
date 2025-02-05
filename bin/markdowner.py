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

    external_documantation_path = path.abspath(path.join( dir_path, pardir, pardir, "variant-query-types", "docs", "generated"))

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
        "requestProfiles": {
            "headline": "Request Profile Definitions",
            "chapters": {
                "$defs": "Request Profiles"
            }
        }
    }

    request_pattern_ids = {}

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
                if d_k == "requestProfiles":
                    request_pattern_ids.update({pk: pi.get("description", "")})

                ls.append(f'### `{pk}` \n')

                ls = __add_md_parameter_lines(ls, pi)

        pp_fh = open(pp_f, "w")
        pp_fh.write("\n".join(ls).replace("\n\n", "\n").replace("\n\n", "\n").replace("\n#", "\n\n#"))
        pp_fh.close()

    #>------------------------------------------------------------------------<#

    gv_f = path.join(generated_docs_path, f"requestProfiles_g_variant.md")
    gv_fh = open(gv_f, "w")
    gv_fh.write(f'# Beacon v2 Request Profiles\n\n')

    for rp_id, rp_desc in request_pattern_ids.items():
        rp_f = path.join(generated_docs_path, f"requestProfiles_{rp_id}.md")
        rp_fh = open(rp_f, "w")
        rp_fh.write(f'# Request Pattern: `{rp_id}`\n\n{rp_desc}')

        ex_f = path.join(examples_yaml_path, f"{rp_id}.yaml")

        if path.exists(ex_f):
            with open(ex_f) as ex_fh:
                ex_d = yaml.load(ex_fh, Loader=yaml.FullLoader)
                ex_ls = [f'## `{rp_id}` Examples']
                for ex_id, ex in ex_d["examples"].items():
                    rp_fh.write(f'\n\n{ex.get("description", "")}\n')
                    if "BV2" in rp_id:
                        gv_fh.write(f'\n\n{ex.get("description", "")}\n')
                    rq = ex.get("request", {})
                    ls = []
                    ls.append(f'### Request \n')
                    ls = __add_md_parameter_lines(ls, rq)
                    rp_fh.write("\n".join(ls).replace("\n\n", "\n").replace("\n\n", "\n").replace("\n#", "\n\n#"))
                    if "BV2" in rp_id:
                        gv_fh.write("\n".join(ls).replace("\n\n", "\n").replace("\n\n", "\n").replace("\n#", "\n\n#"))

        rp_fh.close()
    gv_fh.close()

    cmd = f'rsync -avh --delete {generated_docs_path}/ {external_documantation_path}/'
    print(cmd)

    system(f'rsync -avh --delete {generated_docs_path}/ {external_documantation_path}/')


################################################################################

def __add_md_parameter_lines(lines, parameter):

    for pik, piv in parameter.items():
        # print(f'{pik}: {type(piv)}')
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
            lines.append(f'**{pik}:** `{piv}`    ')
        lines.append(f'\n')

    return lines

################################################################################
################################################################################
################################################################################

if __name__ == '__main__':
    main()
