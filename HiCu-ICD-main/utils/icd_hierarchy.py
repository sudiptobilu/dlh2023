from collections import defaultdict

root_diagnosis = ['001-139', '140-239', '240-279', '280-289', '290-319', '320-389', '390-459', '460-519', '520-579', '580-629',
                  '630-679', '680-709', '710-739', '740-759',  '760-779', '780-799', '800-999', 'V01-V91', 'E000-E999']

root_procedure = ['00-00', '01-05', '06-07', '08-16', '17-17', '18-20', '21-29', '30-34',
                  '35-39', '40-41', '42-54', '55-59', '60-64', '65-71', '72-75', '76-84', '85-86', '87-99']


def generate_code_hierarchy(codes):
    depth_dist = defaultdict(set)
    all_depth_hierarchy_dist = defaultdict(defaultdict)
    for code in sorted(codes, key=lambda x: (-len(x), x)):
        hierarchy = []
        if '.' in code:
            tmp = code.split('.')
            first = tmp[0]
            second = tmp[1]
        else:
            first = code
            second = None
        if first[0] == 'V':
            #continue
            hierarchy.append('V01-V91')
            depth_dist[0].add('V01-V91')

        elif first[0] == 'E':
            #continue
            hierarchy.append('E000-E999')
            depth_dist[0].add('E000-E999')
        else:
            if len(first) == 3:  # diagnosis code
                #continue
                for c in root_diagnosis:
                    [start, end] = c.split('-')
                    if int(start) <= int(first) and int(end) >= int(first):
                        hierarchy.append(c)
                        depth_dist[0].add(c)
                        break
            elif len(first) == 2:  # procedure code
                #continue
                for c in root_procedure:
                    [start, end] = c.split('-')
                    if int(start) <= int(first) and int(end) >= int(first):
                        hierarchy.append(c)
                        depth_dist[0].add(c)
                        break

        hierarchy.append(first + '-' + first)
        depth_dist[1].add(first + '-' + first)
        hierarchy.append(first)
        depth_dist[2].add(first)

        if second is not None:
            for i in range(len(second)):
                hierarchy.append(first + '.' + second[:i + 1])
                depth_dist[3 + i].add(first + '.' + second[:i + 1])

        if len(hierarchy) < 5:
            while len(hierarchy) < 5:
                hierarchy.append(code)
                depth_dist[len(hierarchy) - 1].add(code)

        for i in range(len(hierarchy)):
            all_depth_hierarchy_dist[i][hierarchy[i]] = hierarchy[:i + 1]
    print(depth_dist)
    ind2c = defaultdict(defaultdict)
    for depth in depth_dist.keys():
        ind2c[depth] = defaultdict(str, {i: c for i, c in enumerate(
            sorted(depth_dist[depth], key=lambda x: (-len(x), x)))})
        print("Depth " + str(depth) + ": " + str(len(depth_dist[depth])))

    return all_depth_hierarchy_dist, ind2c
