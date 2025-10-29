# ====================================================
# FOL Resolution Refutation (Instantiated KB)
# Prove: John likes Peanuts
# ====================================================

import copy

# --------------------------
# Utility functions
# --------------------------

def literal_to_str(lit):
    if lit[0] == "~":
        return f"¬{lit[1]}({', '.join(lit[2:])})" if len(lit) > 2 else f"¬{lit[1]}"
    else:
        return f"{lit[0]}({', '.join(lit[1:])})" if len(lit) > 1 else str(lit[0])

def clause_to_str(clause):
    return " ∨ ".join([literal_to_str(l) for l in clause]) if clause else "∅"

def remove_duplicates(clause):
    unique = []
    for l in clause:
        if l not in unique:
            unique.append(l)
    return unique

# --------------------------
# Resolution of two clauses
# --------------------------

def resolve(ci, cj):
    resolvents = []
    for di in ci:
        for dj in cj:
            # Check for complementary literals
            if di[0] == "~" and di[1:] == dj:
                new_clause = [x for x in ci if x != di] + [x for x in cj if x != dj]
                resolvents.append(remove_duplicates(new_clause))
            elif dj[0] == "~" and dj[1:] == di:
                new_clause = [x for x in ci if x != di] + [x for x in cj if x != dj]
                resolvents.append(remove_duplicates(new_clause))
    return resolvents

# --------------------------
# Resolution procedure
# --------------------------

def resolution(kb):
    print("🔍 Starting Resolution Proof...\n")
    step = 1
    new_clauses = []
    seen = []

    while True:
        pairs = [(kb[i], kb[j]) for i in range(len(kb)) for j in range(i+1, len(kb))]
        added_new = False
        for ci, cj in pairs:
            resolvents = resolve(ci, cj)
            for res in resolvents:
                if res in seen or res in kb:
                    continue
                seen.append(res)
                print(f"Step {step}: Resolve ({clause_to_str(ci)}) and ({clause_to_str(cj)})")
                print(f"  → Resolvent: {clause_to_str(res)}\n")
                step += 1
                added_new = True
                if res == []:
                    print("✅ Empty clause derived → John likes Peanuts is PROVED.\n")
                    return True
                new_clauses.append(res)
        if not added_new:
            print("❌ No new clauses — cannot derive contradiction.\n")
            return False
        kb.extend(new_clauses)
        new_clauses = []

# --------------------------
# Knowledge Base (fully instantiated, proper literal format)
# --------------------------

KB = [
    [["~", "Food", "Apple"], ["Likes", "John", "Apple"]],
    [["~", "Food", "Vegetable"], ["Likes", "John", "Vegetable"]],
    [["~", "Food", "Peanuts"], ["Likes", "John", "Peanuts"]],
    [["Food", "Apple"]],
    [["Food", "Vegetable"]],
    [["Food", "Peanuts"]],
    [["~", "Likes", "John", "Peanuts"]]  # Negated goal
]

# --------------------------
# Run proof
# --------------------------

resolution(copy.deepcopy(KB))
