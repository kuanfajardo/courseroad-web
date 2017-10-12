import json
from fancy_print import *
import requests

satt = {}

names = {}
path_keys = {}
path_sat = {}

full_sat = {}
full_path_sat = {}

real_sat = {}
real_path_sat = {}

requ_path_sat = {}

pre_req_master = {}


def tagged(subject: str, tag: str):
    obj = json.load(open("tags.json"))

    if tag not in obj:
        return False

    return subject in obj[tag]


def check(obj, classes):
    ct = obj["count"]
    required = ct == -1

    if required:
        for subject in obj["reqs"]:
            sat_val = subject in classes
            update_sat(subject,
                       sat_val,
                       obj["path"] if "path" in obj else None)

            update_full_sat(subject,
                            [subject] if sat_val else [],
                            obj["path"] if "path" in obj else None)

            update_real_sat(subject,
                            (sat_val, [subject] if sat_val else []),
                            obj["path"] if "path" in obj else None)

        return

    tag_req = "tag" in obj

    co = 0
    sat = []
    for cl in classes:
        if tag_req and tagged(cl, obj["tag"]) or not tag_req and cl in obj["reqs"]:
            co += 1
            sat += [cl]

        if co == ct:
            break

    update_sat(obj["idd"], co >= ct, obj["path"] if "path" in obj else None)
    update_full_sat(obj["idd"], sat, obj["path"] if "path" in obj else None)
    update_real_sat(obj["idd"], (co >= ct, sat), obj["path"] if "path" in obj else None)


def check_req(obj, classes, path=None):
    typ = obj['type']

    if "name" in obj:
        names[obj["idd"]] = obj["name"]

    if is_leaf(obj):
        if path is not None:
            obj.update({'path': path})

            if path[0] not in path_sat:
                path_sat[path[0]] = {}
                full_path_sat[path[0]] = {}
                real_path_sat[path[0]] = {}

            if path[0] not in path_keys:
                path_keys[path[0]] = {}

            if path[1] in path_keys[path[0]]:
                path_keys[path[0]][path[1]].add(obj["idd"])
            else:
                path_keys[path[0]][path[1]] = {obj["idd"]}

        check(obj, classes)
        return

    if typ == 'path':
        for i, path in enumerate(obj['paths']):
            check_req(path, classes, (obj["idd"], path["pid"]))
        return

    for req in obj['reqs']:
        check_req(req, classes, path)


def update_sat(key, val, path=None):
    if path is None:
        satt.update({key: val})
        return

    satt.update({key: val})

    if path[1] in path_sat[path[0]]:
        path_sat[path[0]][path[1]].update({key: val})
    else:
        path_sat[path[0]][path[1]] = {key: val}


def update_full_sat(key, val, path=None):
    if path is None:
        full_sat.update({key: val})
        return

    full_sat.update({key: val})

    if path[1] in full_path_sat[path[0]]:
        full_path_sat[path[0]][path[1]][key] = val
    else:
        full_path_sat[path[0]][path[1]] = {key: val}


def update_real_sat(key, val, path=None):
    if path is None:
        real_sat.update({key: val})
        return

    real_sat.update({key: val})

    if path[1] in real_path_sat[path[0]]:
        real_path_sat[path[0]][path[1]][key] = val
    else:
        real_path_sat[path[0]][path[1]] = {key: val}


def is_leaf(obj):
    return obj["type"] == "leaf"


def eval_path_sat(path_id):
    max_path = -1
    max_ct = -1

    for path, reqs in path_sat[path_id].items():
        ct = 0
        for req, val in reqs.items():
            if val is True:
                ct += 1

        if ct > max_ct:
            max_path = path
            max_ct = ct

    return max_path, max_ct


def eval_all_path_sat():
    all_path_sat = {}
    for path in path_keys:
        all_path_sat[path] = eval_path_sat(path)
        requ_path_sat[path] = all_path_sat[path][0]

    return all_path_sat


def complete_sat(obj):
    typ = obj["type"]

    if typ == "leaf":
        if obj["count"] != -1:
            return

        req_sat = True
        sat = []
        for subject in obj["reqs"]:
            req_sat &= satt[subject]
            sat += full_sat[subject]

        satt[obj["idd"]] = req_sat
        full_sat[obj["idd"]] = sat
        real_sat[obj["idd"]] = (req_sat, sat)

        return

    if typ == "path":
        selected_path = requ_path_sat[obj["idd"]]
        complete_sat(obj["paths"][selected_path])

        return

    if typ == "req":
        req_sat = True
        sat = []
        for req in obj["reqs"]:
            complete_sat(req)
            req_sat &= satt[req["idd"]]
            sat += full_sat[req["idd"]]

        satt[obj["idd"]] = req_sat
        full_sat[obj["idd"]] = sat
        real_sat[obj["idd"]] = (req_sat, sat)


def ts(obj, sat, level=0):
    typ = obj["type"]
    name = obj["name"] if "name" in obj else None
    reqs = obj["reqs"] if "reqs" in obj else None
    idd = obj["idd"]

    str_arr = []
    if typ == "req":
        name_str = name  # assumes each req has a name
        str_arr.append((name_str, level, sat[idd]))

        for req in reqs:
            str_arr += ts(req, sat, level + 1)

        return str_arr

    if typ == "leaf":
        ct = obj["count"]
        required = ct == -1
        tag_req = "tag" in obj

        if name:
            str_arr.append((name, level, sat[idd]))  # remove Y/N from name level
            level += 1

        if tag_req:
            str_arr.append(("* " + str(ct) + " class tagged as \'" + obj["tag"] + "\'", level, True
                            if sat[idd]
                            else False))

            return str_arr

        if required:
            for subject in reqs:
                subj_str = subject
                str_arr.append((subj_str, level, True if sat[subject] else False))

            return str_arr

        else:
            tri_str = str(obj["count"]) + " of: "
            for i, option in enumerate(obj["reqs"]):
                tri_str += option

                if i != len(obj["reqs"]) - 1:
                    tri_str += ", "

            str_arr.append((tri_str, level, sat[idd]))

            return str_arr

    if typ == "path":
        name_str = name  # assumes each path has a name
        str_arr.append((name_str, level, sat[idd]))

        level += 1
        str_arr.append(("1 of:", level, sat[idd]))

        for path in obj["paths"]:
            name_str = "PATH " + str(path["pid"])
            str_arr.append((name_str, level + 1, ""))

            for req in path["reqs"]:
                str_arr += ts(req, sat, level + 2)

        return str_arr


def cs(str_arr: list):
    print("")
    for str_line in str_arr:
        level = str_line[1]

        if level == 0:
            print_header("+---------------------------------------------------+")
            print_header("{0:^53}".format(str_line[0]))
            print_header("+---------------------------------------------------+")
            continue

        level -= 1

        if level == 0:
            print("\n-------------------------------------\n")
            out_str = "{0:" + str(level * 3 + 1) + "} {1}"
            print_message(out_str.format("", "** " + str_line[0]) + " **")
            print("")
        else:
            out_str = "{0:" + str(level * 3) + "} {1}"

            req_satisfied = str_line[2]
            if req_satisfied:
                print_success(out_str.format("", str_line[0]))
            else:
                print_failure(out_str.format("", str_line[0]))


def run(classes: set, req_file: str, show_pre_reqs=False):
    data_file = open(req_file)
    obj = json.load(data_file)

    check_req(obj, classes)

    all_path_sat = eval_all_path_sat()

    for p, sol in all_path_sat.items():
        path_id, _ = sol

        satt.update(path_sat[p][path_id])
        full_sat.update(full_path_sat[p][path_id])
        real_sat.update(real_path_sat[p][path_id])

    complete_sat(obj)
    x = ts(obj, satt)
    cs(x)

    if show_pre_reqs:
        check_all_pre_reqs(classes)


def check_all_pre_reqs(classes: set):
    all_broken_reqs = {}
    for subject in classes:
        broken_pre_reqs = check_pre_req(subject, classes)

        if not broken_pre_reqs:  # all pre reqs satisfied
            continue

        all_broken_reqs[subject] = broken_pre_reqs

    if all_broken_reqs:
        print(bold("\nUnsatisfied Pre-Requisites:\n"))
        for subject, reqs in all_broken_reqs.items():
            print(bold(subject) + ":  " + failure(pre_req_string(reqs)))
    else:
        print(bold("\nAll Pre-Requisites Satisfied!\n"))


def pre_req_string(p: list):
    req_str = ""

    for req in p:
        if len(req) == 1:
            r_s = req[0]
        else:
            r_s = ", ".join(req[:-1])
            r_s += " or " + req[-1]

        req_str += r_s + "; "

    return req_str


def check_pre_req(subject: str, classes: set):
    if subject in pre_req_master:
        return pre_req_master[subject]

    base_url = "https://mit-public.cloudhub.io/coursecatalog/v2/terms/2017FA/subjects/"
    base_url += subject

    headers = {
        "client_id": "897b5d76f69a469cb8138a8300964211",
        "client_secret": "5fee674bAd0A4b228585Bb1870c4E062"
    }

    try:
        req_json = requests.get(base_url, headers=headers).json()["item"]
    except:
        return []

    if req_json["prerequisites"] == "None":
        return True

    all_pre_reqs = parse_pre_reqs(req_json["prerequisites"])
    broken = []
    for pre_req in all_pre_reqs:
        sat = False
        for p in pre_req:
            if p in classes:
                sat = True
                continue

        if not sat:
            broken.append(pre_req)

    pre_req_master[subject] = broken
    return broken


def parse_pre_reqs(pre_req_str):
    pre_reqs = []
    for p in pre_req_str.split("; "):
        pre_req = p.split(", ")

        or_clause = pre_req.pop().split("or ")

        if or_clause[0] == "":
            or_clause.remove("")

        pre_req += [x.strip() for x in or_clause]

        pre_reqs.append(pre_req)

    return pre_reqs
