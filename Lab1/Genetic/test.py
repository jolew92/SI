__author__ = 'Joanna'

def check_valid(graph):
    for node,nexts in graph.iteritems():
        assert(node not in nexts) # # no node linked to itself
        for next in nexts:
            assert(next in graph and node in graph[next]) # A linked to B implies B linked to A

def check_solution(graph, solution):
    if solution is not None:
        for node,nexts in graph.iteritems():
            assert(node in solution)
            color = solution[node]
            for next in nexts:
                assert(next in solution and solution[next] != color)

def find_best_candidate(graph, guesses):
    if True: #optimised
        # Optimisations are to be put here. Ideas would be to take the node with the most uncolored neighboors or the one with the smallest possible number of colors or both
        candidates_with_add_info = [
            (
            -len({guesses[neigh] for neigh in graph[n] if neigh     in guesses}), # nb_forbidden_colors
            -len({neigh          for neigh in graph[n] if neigh not in guesses}), # minus nb_uncolored_neighbour
            n
            ) for n in graph if n not in guesses]
        candidates_with_add_info.sort()
        candidates = [n for _,_,n in candidates_with_add_info]
    else:
        candidates = [n for n in graph if n not in guesses]
        candidates.sort() # just to have some consistent performances
    if candidates:
        candidate = candidates[0]
        assert(candidate not in guesses)
        return candidate
    assert(set(graph.keys()) == set(guesses.keys()))
    return None

nb_calls = 0

def solve(graph, colors, guesses, depth):
    global nb_calls
    nb_calls += 1
    n = find_best_candidate(graph, guesses)
    if n is None:
        return guesses # Solution is found
    for c in colors - {guesses[neigh] for neigh in graph[n] if neigh in guesses}:
        assert(n not in guesses)
        assert(all((neigh not in guesses or guesses[neigh] != c) for neigh in graph[n]))
        guesses[n] = c
        indent = '  '*depth
        print "%sTrying to give color %s to %s" % (indent,c,n)
        if solve(graph, colors, guesses, depth+1):
            print "%sGave color %s to %s" % (indent,c,n)
            return guesses
        else:
            del guesses[n]
            print "%sCannot give color %s to %s" % (indent,c,n)
    return None


def solve_problem(graph, colors):
    check_valid(graph)
    solution = solve(graph, colors, dict(), 0)
    print solution
    check_solution(graph,solution)


WA  = 'western australia'
NT  = 'northwest territories'
SA  = 'southern australia'
Q   = 'queensland'
NSW = 'new south wales'
V   = 'victoria'
T   = 'tasmania'

australia = { T:   {V               },
              WA:  {NT, SA         },
              NT:  {WA, Q, SA       },
              SA:  {WA, NT, Q, NSW, V},
              Q:   {NT, SA, NSW   },
              NSW: {Q, SA, V         },
              V:   {SA, NSW, T     } }


AL = "Alabama"
AK = "Alaska"
AZ = "Arizona"
AR = "Arkansas"
CA = "California"
CO = "Colorado"
CT = "Connecticut"
DE = "Delaware"
FL = "Florida"
GA = "Georgia"
HI = "Hawaii"
ID = "Idaho"
IL = "Illinois"
IN = "Indiana"
IA = "Iowa"
KS = "Kansas"
KY = "Kentucky"
LA = "Louisiana"
ME = "Maine"
MD = "Maryland"
MA = "Massachusetts"
MI = "Michigan"
MN = "Minnesota"
MS = "Mississippi"
MO = "Missouri"
MT = "Montana"
NE = "Nebraska"
NV = "Nevada"
NH = "NewHampshire"
NJ = "NewJersey"
NM = "NewMexico"
NY = "NewYork"
NC = "NorthCarolina"
ND = "NorthDakota"
OH = "Ohio"
OK = "Oklahoma"
OR = "Oregon"
PA = "Pennsylvania"
RI = "RhodeIsland"
SC = "SouthCarolina"
SD = "SouthDakota"
TN = "Tennessee"
TX = "Texas"
UT = "Utah"
VT = "Vermont"
VA = "Virginia"
WA = "Washington"
WV = "WestVirginia"
WI = "Wisconsin"
WY = "Wyoming"

united_stated_of_america = {
    AL: {GA, FL, TN, MS},
    AK: {},
    AZ: {CA, NV, UT, CO, NM},
    AR: {MO, OK, TX, LA, TN, MS},
    CA: {OR, NV, AZ},
    CO: {WY, NE, KS, OK, NM, AZ, UT},
    CT: {},
    DE: {},
    FL: {AL, GA},
    GA: {SC, NC, TN, AL, FL},
    HI: {},
    ID: {WA, MT, OR, WY, UT, NV},
    IL: {WI, IA, MO, KY, IN, MI},
    IN: {MI, WI, IL, KY, OH},
    IA: {MN, SD, NE, MO, WI, IL},
    KS: {NE, CO, OK, MO},
    KY: {IN, IL, MO, TN, OH, WV, VA},
    LA: {AR, TX, MS},
    ME: {},
    MD: {},
    MA: {},
    MI: {IL, WI, IN, OH},
    MN: {ND, SD, IA, WI},
    MS: {TN, AR, LA, AL},
    MO: {IA, NE, KS, OK, AR, IL, KY, TN},
    MT: {ID, WY, SD, ND},
    NE: {SD, WY, CO, KS, MO, IA},
    NV: {OR, ID, UT, AZ, CA},
    NH: {},
    NJ: {},
    NM: {AZ, UT, CO, OK, TX},
    NY: {},
    NC: {GA, TN, SC, VA},
    ND: {MT, SD, MN},
    OH: {MI, IN, KY, WV},
    OK: {KS, CO, NM, TX, AR, MO},
    OR: {WA, ID, NV, CA},
    PA: {},
    RI: {},
    SC: {GA, NC},
    SD: {ND, MT, WY, NE, MN, IA},
    TN: {KY, MO, AR, MS, MO, AL, GA, NC},
    TX: {OK, NM, AR, LA},
    UT: {ID, NV, WY, CO, AZ, NM},
    VT: {},
    VA: {WV, KY, NC},
    WA: {OR, ID},
    WV: {OH, VA, KY},
    WI: {MN, IA, IL, MI, IN},
    WY: {MT, SD, NE, CO, UT, ID},
}

# Can't be bothered to complete the East part of the map - removing unused nodes (keeping them is also a good way to test your algorithm and see if still works)
united_stated_of_america = {n:neigh for n,neigh in united_stated_of_america.iteritems() if neigh}

colors  = {'r', 'g', 'b', 'y'}

solve_problem(australia, colors)
solve_problem(united_stated_of_america, colors)
print nb_calls